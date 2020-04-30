import pandas as pd
df = pd.read_json (r'games.json')
df.to_csv (r'games.csv', index = None)