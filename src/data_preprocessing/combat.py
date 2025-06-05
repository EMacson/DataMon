import pandas as pd
import os

#RAW_PATH = './../../data/raw/combat.csv'
#PROCESSED_PATH = '../../data/processed/combat.csv'

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
RAW_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'combats.csv')
PROCESSED_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'combats.csv')
POKEMON_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'pokemon.csv')

def clean_combat_data(input_path=RAW_PATH, output_path=PROCESSED_PATH, pokemon_path=POKEMON_PATH):
    #print(os.path.join(os.path.dirname(__file__), '../../data/raw/combat.csv'))
    df = pd.read_csv(input_path)
    pokemon_set = pd.read_csv(pokemon_path)
    
    # Drop exact duplicate rows
    df.drop_duplicates(inplace=True)

    # Remove any rows with missing values in essential stat columns
    essential_stats = ['First_pokemon','Second_pokemon','Winner']
    df.dropna(subset=essential_stats, inplace=True)

    # remove any row where the winner is not the first or second pokemon

    # Ensure numeric columns are of correct dtype
    for col in essential_stats:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.columns = [col.strip().replace(' ', '_').replace('.', '') for col in df.columns]

    df = df.merge(
        pokemon_set.add_prefix('First_'),
        left_on='First_pokemon',
        right_on='First_#',
        how='left'
    )

    df = df.merge(
        pokemon_set.add_prefix('Second_'),
        left_on='Second_pokemon',
        right_on='Second_#',
        how='left'
    )

    df = df.merge(
        pokemon_set.add_prefix('Winner_'),
        left_on='Winner',
        right_on='Winner_#',
        how='left'
    )

    #df = df[['First_pokemon', 'First_#', 'Second_pokemon', 'Second_#', 'Winner']]
    df = df[['First_pokemon', 'First_Name', 'Second_pokemon', 'Second_Name', 'Winner', 'Winner_Name']]

    '''
    for _, row in df.iterrows():
        pokemon1 = row['First_pokemon']
        pokemon2 = row['Second_pokemon']
        winner = row['Winner']

        if pokemon1 in pokemon_set.index and pokemon2 in pokemon_set.index and winner in pokemon_set.index:
            row['First_pokemon'] = pokemon_set.loc[pokemon1, 'Name']
            row['Second_pokemon'] = pokemon_set.loc[pokemon2, 'Name']
            row['Winner'] = pokemon_set.loc[winner, 'Name']
        else:
            # remove row
            pass
    '''

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")
    

if __name__ == '__main__':
    clean_combat_data()
