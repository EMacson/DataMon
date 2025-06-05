import pandas as pd
from collections import defaultdict, Counter
from .type_chart import TYPE_CHART
import warnings
import math

def evaluate_team(team: list[str], df: pd.DataFrame):
    if len(team) != 6:
        raise ValueError("Team must consist of exactly 6 Pokémon names.")
    
    df = df.copy()
    df = df.set_index("Name")

    #print(df)

    missing = [p for p in team if p not in df.index]
    if missing:
        raise ValueError(f"These Pokémon were not found in the dataset: {missing}")
    
    # Slice team data
    team_df = df.loc[team].reset_index()

    # ----------------------
    # 1. Stat Aggregation
    # ----------------------
    stat_cols = ['HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed', 'Total']
    avg_stats = team_df[stat_cols].mean().round(1).to_dict()

    # ----------------------
    # 2. Type Coverage (offensive)
    # ----------------------
    all_types = set(TYPE_CHART.keys())
    coverage = set()

    #print(team_df)

    for _, row in team_df.iterrows():
        #types = [row['Type_1'], row['Type_2']] if row['Type_2'] != 'None' else [row['Type_1']]
        #if row['Type_2'] == 'None':
        #    types = [row['Type_1'], 'None']
        #else:
        #    types = [row['Type_1'], row['Type_2']]
        types = [row['Type_1'], row['Type_2']]
        #print(types)
        for t in types:
            # Add all types that this type is strong against
            if t =='None':
                break
            for opponent_type in all_types:
                #print(t)
                if TYPE_CHART[t][opponent_type] > 1:
                    coverage.add(opponent_type)

    # ----------------------
    # 3. Weaknesses (defensive)
    # ----------------------
    weaknesses = Counter()

    for _, row in team_df.iterrows():
        defending_types = [row['Type_1']]
        if row['Type_2'] != 'None':
            defending_types.append(row['Type_2'])

        for attack_type in all_types:
            multiplier = 1.0
            for defense_type in defending_types:
                try:
                    multiplier *= TYPE_CHART[attack_type][defense_type]
                except:
                    multiplier = 1.0

            if multiplier > 1.0:
                weaknesses[attack_type] += 1

    # ----------------------
    # 4. Score (basic)
    # ----------------------
    # Placeholder score: average total + coverage bonus - weakness penalty
    score = avg_stats['Total'] * 0.15 + len(coverage) * 2 - sum(v > 2 for v in weaknesses.values()) * 5
    score = round(min(score, 100), 1)

    # ----------------------
    # 5. Warnings
    # ----------------------
    warnings_list = []

    if any(v >= 3 for v in weaknesses.values()):
        for typ, count in weaknesses.items():
            if count >= 3:
                warnings_list.append(f"Weak to {typ} ({count} Pokémon)")

    dupes = team_df['Type_1'].tolist() + [t for t in team_df['Type_2'] if t != 'None']
    dupes_count = Counter(dupes)
    for typ, count in dupes_count.items():
        if count > 2:
            warnings_list.append(f"Overrepresentation of {typ} type ({count} instances)")

    # ----------------------
    # Return result
    # ----------------------
    return {
        'team_df': team_df,
        'average_stats': avg_stats,
        'type_coverage': sorted(list(coverage)),
        'weaknesses': dict(weaknesses),
        'overall_score': score,
        'warnings': warnings_list
    }

