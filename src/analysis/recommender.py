import pandas as pd
from .team_evaluator import evaluate_team

def recommend_teammates(current_team, df, num_recommendations=3):
    try:
        current_team = [p for p in current_team if p]
        if len(current_team) >= 6:
            return []

        all_names = df['Name'].unique()
        candidates = [p for p in all_names if p not in current_team]

        scored = []
        test_team = current_team

        for c in candidates:
            #test_team = current_team + [c]
            test_team.append(c)
            if len(test_team) < 6:
                continue
            try:
                #print('test')
                result = evaluate_team(test_team, df)
                score = result['overall_score']
                print(score)
                warnings = result['warnings']
                scored.append((c, score, warnings))
                test_team.clear()
                test_team = current_team
            except Exception as inner_e:
                print(f"Failed evaluating team with {c}: {inner_e}")

        # Sort by descending score, penalizing warnings
        #print(scored)
        scored.sort(key=lambda x: x[1] - len(x[2]) * 2, reverse=True)
        #return [('Mega Gallade', 100, ['Weak to Fighting (3 Pokémon)']), ('Shaymin Sky Forme', 100, ['Weak to Bug (3 Pokémon)']), ('Rayquaza', 100, ['Weak to Ice (3 Pokémon)', 'Weak to Grass (3 Pokémon)'])]
        return scored[:num_recommendations]
    except Exception as outer_e:
        print("🔥 recommend_teammates failed:", outer_e)
        return []