import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
RAW_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'combats.csv')
COMBAT_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'combats.csv')
POKEMON_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'pokemon.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'src', 'models', 'matchup_rf.pkl')

def load_pokemon_data(path=POKEMON_PATH):
    df = pd.read_csv(path, na_values=[], keep_default_na=False)
    df.set_index('Name', inplace=True)
    return df

def encode_matchup(row, stats_df):
    first_stats = stats_df.loc[row['First_Name']]
    second_stats = stats_df.loc[row['Second_Name']]
    #print(first_stats)

    # Feature: difference in base stats
    numeric_cols =['HP','Attack','Defense','Sp_Atk','Sp_Def','Speed']
    features = first_stats[numeric_cols] - second_stats[numeric_cols]
    #print(features)
    return pd.Series(features)

def load_and_train(
        combat_path=COMBAT_PATH,
        stats_path=POKEMON_PATH,
        save_model_path=MODEL_PATH
):
    # Load data
    stats_df = load_pokemon_data(stats_path)
    combat_df = pd.read_csv(combat_path)
    print(combat_df.head())
    print(stats_df.head())


    # Drop any missing Pokémon
    combat_df = combat_df[
        combat_df['First_Name'].isin(stats_df.index) & 
        combat_df['Second_Name'].isin(stats_df.index)
    ]

    print("Combat rows after cleaning:", len(combat_df))

    X = combat_df.apply(lambda row: encode_matchup(row, stats_df), axis=1)
    y = combat_df['Winner_bool']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    print("Validation accuracy:", clf.score(X_test, y_test))

    # Save model
    joblib.dump(clf, save_model_path)
    print(f"Model saved to {save_model_path}")

def predict_matchup(pokemon_a, pokemon_b, stats_df, model_path=MODEL_PATH):
    clf = joblib.load(model_path)
    diff = stats_df.loc[pokemon_a]['Total'] - stats_df.loc[pokemon_b]['Total']
    #prob = clf.predict_proba([diff])[0][1]  # prob A wins
    print("diff:", diff)
    print("shape:", np.shape(diff))
    return 0
