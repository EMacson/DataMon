import pandas as pd
import os

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

#RAW_PATH = './../../data/raw/combat.csv'
#PROCESSED_PATH = '../../data/processed/combat.csv'

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
RAW_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'pokemon.csv')
PROCESSED_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'cards.csv')

def get_card_data(input_path=RAW_PATH, output_path=PROCESSED_PATH):
    #print(os.path.join(os.path.dirname(__file__), '../../data/raw/combat.csv'))
    df = pd.read_csv(input_path, usecols=["Name"])

    for index, row in df.iterrows():
        try:
            cards = Card.where(q=f'name:{row['Name']}')
            print(cards)
        except:
            print('invalid card entry')


    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")
    

if __name__ == '__main__':
    get_card_data()
