import pandas as pd
import os

RAW_PATH = './data/raw/pokemon.csv'
PROCESSED_PATH = './data/processed/pokemon.csv'

def clean_pokemon_data(input_path=RAW_PATH, output_path=PROCESSED_PATH):
    df = pd.read_csv(input_path)
    
    # Drop exact duplicate rows
    df.drop_duplicates(inplace=True)

    # Fill missing Type 2 with 'None'
    if 'Type 2' in df.columns:
        df['Type 2'] = df['Type 2'].fillna('None')

    # Remove any rows with missing values in essential stat columns
    essential_stats = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    df.dropna(subset=essential_stats, inplace=True)

    # Ensure numeric columns are of correct dtype
    for col in essential_stats:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Add Total stat column if it doesn't exist
    if 'Total' not in df.columns:
        df['Total'] = df[essential_stats].sum(axis=1)

    df.columns = [col.strip().replace(' ', '_').replace('.', '') for col in df.columns]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")
    

if __name__ == '__main__':
    clean_pokemon_data()
