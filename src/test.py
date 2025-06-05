from analysis.team_evaluator import evaluate_team
from analysis.recommender import recommend_teammates
import pandas as pd
from models.matchup_predictor import (
    load_pokemon_data,
    load_and_train,
    predict_matchup
)

load_and_train()
# Later: use model to predict matchups
stats_df = load_pokemon_data()
#prob = predict_matchup('Gengar', 'Alakazam', stats_df)
print(f"Gengar wins vs Alakazam: {prob:.2%}")
#result = load_pokemon_data

#df = pd.read_csv('./data/processed/pokemon.csv', na_values=[], keep_default_na=False)

#team = ['Bulbasaur', 'Kakuna']

#result = recommend_teammates(team, df)
#print(result)

'''
team = ['Bulbasaur', 'Kakuna', 'Clefable', 'Camerupt', 'Palkia', 'Shieldon']

result = evaluate_team(team, df)

print(result['average_stats'])
print("Coverage:", result['type_coverage'])
print("Weaknesses:", result['weaknesses'])
print("Score:", result['overall_score'])
print("Warnings:", result['warnings'])
'''