from analysis.team_evaluator import evaluate_team
from analysis.recommender import recommend_teammates
import pandas as pd

df = pd.read_csv('./data/processed/pokemon.csv', na_values=[], keep_default_na=False)

team = ['Bulbasaur', 'Kakuna']

result = recommend_teammates(team, df)
print(result)

'''
team = ['Bulbasaur', 'Kakuna', 'Clefable', 'Camerupt', 'Palkia', 'Shieldon']

result = evaluate_team(team, df)

print(result['average_stats'])
print("Coverage:", result['type_coverage'])
print("Weaknesses:", result['weaknesses'])
print("Score:", result['overall_score'])
print("Warnings:", result['warnings'])
'''