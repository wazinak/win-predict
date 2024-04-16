import pandas as pd


df = pd.read_csv("all_stat.csv")
# u_v = df['team'].unique()
# u_v = df['map_map'].unique()
# u_v = df['opponent'].unique()
# print(u_v)


commands = ['Virtus.pro', 'HAVU', 'Alliance', 'fnatic', 'G2', 'EYEBALLERS', 'ALTERNATE aTTaX', '9INE', 'GODSENT',
            'BOSS', '500', 'Astralis', 'Natus Vincere','Ninjas in Pyjamas', 'Cloud9', 'Eternal Fire', 'BESTIA',
            'ODDIK', 'Mindfreak', 'Sprout', 'PERA', 'Liquid', '3DMAX', 'Fluxo', 'Illuminar',
            'ThunderFlash', 'adalYamigos', 'Sangal', 'KOI', 'Solid', 'ARCRED', 'Rooster',
            'Monte', 'Espionage', 'FaZe', 'Nexus', 'Vantage', 'BIG', 'SINNERS', 'Metizport',
            '9 Pandas', 'BetBoom', 'Lynn Vision', 'Guild Eagles', 'PGE Turow', 'Preasy',
            'Spirit', 'AMKAL', 'GamerLegion', 'M80', 'Galorys', 'Entropiq', 'ECSTATIC',
            '1WIN', 'Party Astronauts', 'Imperial', 'Bad News Kangaroos', 'Zero Tenacity',
            'Passion UA', 'Corinthians', 'MIBR', 'ENCE', 'Vitality', 'Endpoint', 'B8', '9z',
            'FORZE', 'MOUZ NXT', 'TYLOO', 'W7M', 'Insilio', 'Case', 'BLEED', 'TheMongolz',
            'Permitta', 'Aurora', 'Space', 'Grayhound', 'Pompa', 'NRG', 'Rebels', 'Apeks',
            'MOUZ', 'Nouns', 'Into the Breach', 'Wildcard', '00NATION', 'ECLOT', 'SAW',
            'HEROIC', 'Anonymo', 'Sampi', 'Complexity', 'paiN', 'Gods Reign', 'OG',
            'RED Canids', 'IKLA', 'Sharks', 'FURIA', 'sYnck', 'FTW', 'Evil Geniuses',
            'los kogutos']
maps = ['Inferno', 'Overpass', 'Ancient', 'Mirage', 'Nuke', 'Dust2', 'Train', 'Vertigo',
        'Anubis', 'Cobblestone', 'Cache']


for command in commands:
    command_df = df[df['team'] == f'{command}']
    for command_map in maps:
        try:
            unique_map = command_df[command_df['map_map'] == f'{command_map}']
            total_played_on_unique_map = unique_map.shape[0]
            win_count_on_map = unique_map[unique_map['w_l'] == 'W'].shape[0]
            lose_count_on_map = unique_map[unique_map['w_l'] == 'L'].shape[0]
            win_percentage_on_map = (win_count_on_map / total_played_on_unique_map) * 100
            print("Процент побед команд "f"{command} на карте: {command_map} - {round(win_percentage_on_map, 2)}%")
        except ZeroDivisionError:
            print(f"На этой карте - {command_map}, команда: {command} не играла в этой статистике")
    total_matches = command_df.shape[0]
    win_count = command_df[command_df['w_l'] == 'W'].shape[0]
    loose_count = command_df[command_df['w_l'] == 'L'].shape[0]

    win_percentage = (win_count / total_matches) * 100
    print("Процент побед команд "f"{command}: {round(win_percentage, 2)}%")

