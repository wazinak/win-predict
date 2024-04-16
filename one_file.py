import os
import pandas as pd

directory = '/Users/wazinak/Desktop/Pet Projects/win predict/game_stat'
files = os.listdir(directory)
df_list = []
for file in files:
    df = pd.read_csv(os.path.join(directory, file))
    df_list.append(df)

new_df = pd.concat(df_list, axis=0)

csv_name = 'all_stat' + '.csv'
new_df.to_csv(csv_name, index=False)