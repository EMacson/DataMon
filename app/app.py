# app/app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit.components.v1 as components
from src.analysis.team_evaluator import evaluate_team
from src.analysis.recommender import recommend_teammates

def plot_radar(stats_dict):
    categories = list(stats_dict.keys())
    values = list(stats_dict.values())

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Average Stats',
        line=dict(color='royalblue')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, max(values) + 20])
        ),
        showlegend=False
    )

    return fig

def plot_weakness_heatmap(weakness_dict):
    df = pd.DataFrame({
        "Type": list(weakness_dict.keys()),
        "Count": list(weakness_dict.values())
    })

    fig = px.bar(df, x="Type", y="Count", color="Count", color_continuous_scale="reds")
    fig.update_layout(title="Team Weaknesses", xaxis_title="Type", yaxis_title="# Pokémon Weak To This Type")
    return fig

def type_tag_cloud(type_list):
    html = "<div style='display: flex; flex-wrap: wrap;'>"
    for t in type_list:
        html += f"<span style='margin: 4px; padding: 6px 10px; background-color: #f0f0f0; border-radius: 10px;'>{t}</span>"
    html += "</div>"
    components.html(html, height=100)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/pokemon.csv", na_values=[], keep_default_na=False)

df = load_data()
pokemon_names = df['Name'].unique()

st.title("🔍 Pokémon Team Evaluator")

st.markdown("Enter your team of 6 Pokémon to see stats, type coverage, weaknesses, and an overall score.")

team = []
for i in range(6):
    name = st.selectbox(
        f"Pokémon {i + 1}",
        options=[""] + list(pokemon_names),  # Add empty string as default
        key=f"poke_{i}"
    )
    if name:
        team.append(name)

if st.button("Evaluate Team"):
    try:
        results = evaluate_team(team, df)

        st.subheader("📊 Average Stats")
        st.json(results['average_stats'])

        st.subheader("🎯 Type Coverage (Offensive)")
        st.write(", ".join(results['type_coverage']))

        st.subheader("🛡️ Weaknesses (Defensive)")
        st.write(results['weaknesses'])

        st.subheader("🏆 Overall Score")
        st.metric(label="Score", value=results['overall_score'])

        if results['warnings']:
            st.subheader("⚠️ Warnings")
            for w in results['warnings']:
                st.warning(w)

        st.subheader("📋 Team Summary")
        st.dataframe(results['team_df'])

        st.subheader("📊 Average Stats (Radar Chart)")
        st.plotly_chart(plot_radar(results['average_stats']), use_container_width=True)

        st.subheader("🔥 Team Weaknesses (Bar Heatmap)")
        st.plotly_chart(plot_weakness_heatmap(results['weaknesses']), use_container_width=True)

        st.subheader("🎯 Type Coverage")
        type_tag_cloud(results['type_coverage'])

    except ValueError as e:
        st.error(str(e))

 #---- Teammate Recommendations ----#
if st.button("Generate Team"):
    if len(team) < 6:
        st.subheader("🧠 Recommended Teammates")
        recs = recommend_teammates(team, df)

        for name, score, warnings in recs:
            st.markdown(f"**{name}** — Score: {score:.1f}")
            if warnings:
                for w in warnings:
                    st.caption(f"⚠️ {w}")
    else:
        st.info("Team is full — no recommendations needed.")