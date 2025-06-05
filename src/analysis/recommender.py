import pandas as pd
from .team_evaluator import evaluate_team

def recommend_teammates(current_team, df, num_recommendations=3):
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
        except Exception:
            continue

    # Sort by descending score, penalizing warnings
    print(scored)
    scored.sort(key=lambda x: x[1] - len(x[2]) * 2, reverse=True)

    return scored[:num_recommendations]