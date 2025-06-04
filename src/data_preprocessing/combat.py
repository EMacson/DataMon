import pandas as pd
import os

#RAW_PATH = './../../data/raw/combat.csv'
#PROCESSED_PATH = '../../data/processed/combat.csv'

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
RAW_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'combats.csv')
PROCESSED_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'combats.csv')

def clean_combat_data(input_path=RAW_PATH, output_path=PROCESSED_PATH):
    #print(os.path.join(os.path.dirname(__file__), '../../data/raw/combat.csv'))
    df = pd.read_csv(input_path)
    
    # Drop exact duplicate rows
    df.drop_duplicates(inplace=True)

    # Remove any rows with missing values in essential stat columns
    essential_stats = ['First_pokemon','Second_pokemon','Winner']
    df.dropna(subset=essential_stats, inplace=True)

    # Ensure numeric columns are of correct dtype
    for col in essential_stats:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.columns = [col.strip().replace(' ', '_').replace('.', '') for col in df.columns]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")
    

if __name__ == '__main__':
    clean_combat_data()
