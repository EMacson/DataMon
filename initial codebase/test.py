import pprint

TYPES = ['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting',
         'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost',
         'Dragon', 'Dark', 'Steel', 'Fairy']

TYPE_CHART = {}

# Initialize all with 1.0 (neutral effectiveness)
for attacker in TYPES:
    TYPE_CHART[attacker] = {}
    for defender in TYPES:
        TYPE_CHART[attacker][defender] = 1.0

# Now override with 2.0, 0.5, and 0.0 based on the chart

# 2.0 (super effective)
TYPE_CHART['Fire']['Grass'] = 2.0
TYPE_CHART['Fire']['Ice'] = 2.0
TYPE_CHART['Fire']['Bug'] = 2.0
TYPE_CHART['Fire']['Steel'] = 2.0

TYPE_CHART['Water']['Fire'] = 2.0
TYPE_CHART['Water']['Ground'] = 2.0
TYPE_CHART['Water']['Rock'] = 2.0

TYPE_CHART['Grass']['Water'] = 2.0
TYPE_CHART['Grass']['Ground'] = 2.0
TYPE_CHART['Grass']['Rock'] = 2.0

TYPE_CHART['Electric']['Water'] = 2.0
TYPE_CHART['Electric']['Flying'] = 2.0

TYPE_CHART['Ice']['Grass'] = 2.0
TYPE_CHART['Ice']['Ground'] = 2.0
TYPE_CHART['Ice']['Flying'] = 2.0
TYPE_CHART['Ice']['Dragon'] = 2.0

TYPE_CHART['Fighting']['Normal'] = 2.0
TYPE_CHART['Fighting']['Ice'] = 2.0
TYPE_CHART['Fighting']['Rock'] = 2.0
TYPE_CHART['Fighting']['Dark'] = 2.0
TYPE_CHART['Fighting']['Steel'] = 2.0

TYPE_CHART['Poison']['Grass'] = 2.0
TYPE_CHART['Poison']['Fairy'] = 2.0

TYPE_CHART['Ground']['Fire'] = 2.0
TYPE_CHART['Ground']['Electric'] = 2.0
TYPE_CHART['Ground']['Poison'] = 2.0
TYPE_CHART['Ground']['Rock'] = 2.0
TYPE_CHART['Ground']['Steel'] = 2.0

TYPE_CHART['Flying']['Grass'] = 2.0
TYPE_CHART['Flying']['Fighting'] = 2.0
TYPE_CHART['Flying']['Bug'] = 2.0

TYPE_CHART['Psychic']['Fighting'] = 2.0
TYPE_CHART['Psychic']['Poison'] = 2.0

TYPE_CHART['Bug']['Grass'] = 2.0
TYPE_CHART['Bug']['Psychic'] = 2.0
TYPE_CHART['Bug']['Dark'] = 2.0

TYPE_CHART['Rock']['Fire'] = 2.0
TYPE_CHART['Rock']['Ice'] = 2.0
TYPE_CHART['Rock']['Flying'] = 2.0
TYPE_CHART['Rock']['Bug'] = 2.0

TYPE_CHART['Ghost']['Psychic'] = 2.0
TYPE_CHART['Ghost']['Ghost'] = 2.0

TYPE_CHART['Dragon']['Dragon'] = 2.0

TYPE_CHART['Dark']['Psychic'] = 2.0
TYPE_CHART['Dark']['Ghost'] = 2.0

TYPE_CHART['Steel']['Ice'] = 2.0
TYPE_CHART['Steel']['Rock'] = 2.0
TYPE_CHART['Steel']['Fairy'] = 2.0

TYPE_CHART['Fairy']['Fighting'] = 2.0
TYPE_CHART['Fairy']['Dragon'] = 2.0
TYPE_CHART['Fairy']['Dark'] = 2.0

# 0.5 (not very effective)
TYPE_CHART['Normal']['Rock'] = 0.5
TYPE_CHART['Normal']['Steel'] = 0.5

TYPE_CHART['Fire']['Fire'] = 0.5
TYPE_CHART['Fire']['Water'] = 0.5
TYPE_CHART['Fire']['Rock'] = 0.5
TYPE_CHART['Fire']['Dragon'] = 0.5

TYPE_CHART['Water']['Water'] = 0.5
TYPE_CHART['Water']['Grass'] = 0.5
TYPE_CHART['Water']['Dragon'] = 0.5

TYPE_CHART['Grass']['Fire'] = 0.5
TYPE_CHART['Grass']['Grass'] = 0.5
TYPE_CHART['Grass']['Poison'] = 0.5
TYPE_CHART['Grass']['Flying'] = 0.5
TYPE_CHART['Grass']['Bug'] = 0.5
TYPE_CHART['Grass']['Dragon'] = 0.5
TYPE_CHART['Grass']['Steel'] = 0.5

TYPE_CHART['Electric']['Grass'] = 0.5
TYPE_CHART['Electric']['Electric'] = 0.5
TYPE_CHART['Electric']['Dragon'] = 0.5

TYPE_CHART['Ice']['Fire'] = 0.5
TYPE_CHART['Ice']['Water'] = 0.5
TYPE_CHART['Ice']['Ice'] = 0.5
TYPE_CHART['Ice']['Steel'] = 0.5

TYPE_CHART['Fighting']['Poison'] = 0.5
TYPE_CHART['Fighting']['Flying'] = 0.5
TYPE_CHART['Fighting']['Psychic'] = 0.5
TYPE_CHART['Fighting']['Bug'] = 0.5
TYPE_CHART['Fighting']['Fairy'] = 0.5

TYPE_CHART['Poison']['Poison'] = 0.5
TYPE_CHART['Poison']['Ground'] = 0.5
TYPE_CHART['Poison']['Rock'] = 0.5
TYPE_CHART['Poison']['Ghost'] = 0.5

TYPE_CHART['Ground']['Grass'] = 0.5
TYPE_CHART['Ground']['Bug'] = 0.5

TYPE_CHART['Flying']['Electric'] = 0.5
TYPE_CHART['Flying']['Rock'] = 0.5
TYPE_CHART['Flying']['Steel'] = 0.5

TYPE_CHART['Psychic']['Psychic'] = 0.5
TYPE_CHART['Psychic']['Steel'] = 0.5

TYPE_CHART['Bug']['Fire'] = 0.5
TYPE_CHART['Bug']['Fighting'] = 0.5
TYPE_CHART['Bug']['Poison'] = 0.5
TYPE_CHART['Bug']['Flying'] = 0.5
TYPE_CHART['Bug']['Ghost'] = 0.5
TYPE_CHART['Bug']['Steel'] = 0.5
TYPE_CHART['Bug']['Fairy'] = 0.5

TYPE_CHART['Rock']['Fighting'] = 0.5
TYPE_CHART['Rock']['Ground'] = 0.5
TYPE_CHART['Rock']['Steel'] = 0.5

TYPE_CHART['Ghost']['Dark'] = 0.5

TYPE_CHART['Dragon']['Steel'] = 0.5

TYPE_CHART['Dark']['Fighting'] = 0.5
TYPE_CHART['Dark']['Dark'] = 0.5
TYPE_CHART['Dark']['Fairy'] = 0.5

TYPE_CHART['Steel']['Fire'] = 0.5
TYPE_CHART['Steel']['Water'] = 0.5
TYPE_CHART['Steel']['Electric'] = 0.5
TYPE_CHART['Steel']['Steel'] = 0.5

TYPE_CHART['Fairy']['Fire'] = 0.5
TYPE_CHART['Fairy']['Poison'] = 0.5
TYPE_CHART['Fairy']['Steel'] = 0.5

# 0.0 (no effect)
TYPE_CHART['Normal']['Ghost'] = 0.0
TYPE_CHART['Fighting']['Ghost'] = 0.0
TYPE_CHART['Poison']['Steel'] = 0.0
TYPE_CHART['Electric']['Ground'] = 0.0
TYPE_CHART['Ground']['Flying'] = 0.0
TYPE_CHART['Psychic']['Dark'] = 0.0
TYPE_CHART['Ghost']['Normal'] = 0.0
TYPE_CHART['Dragon']['Fairy'] = 0.0

for attacker in TYPE_CHART:
    for defender in TYPE_CHART[attacker]:
        value = TYPE_CHART[attacker][defender]
        print(f"TYPE_CHART['{attacker}']['{defender}'] = {value}")
        