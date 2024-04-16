import pandas as pd

df = pd.read_csv('cyber_stat.csv')
UNIQUE_TEAM = df['team'].unique() # это колонка где только команда и статистика команды
UNIQUE_MAP = df['map_map'].unique()
UNIQUE_OPPONENT = df['opponent'].unique()

print(UNIQUE_TEAM)
CHECK_COMMANDS = [
    '9INE',
    'BetBoom'
]

# PROMPT = input("Напишите команду, которая вас интересует")


def main():
    for command in UNIQUE_TEAM:
        command_df = df[df['team.2'] == f'{command}']
        stat_team_df = df[df['team'] == f'{command}']
        try:
            total_matches = command_df.shape[0]
            win_count = command_df[command_df['w_l'] == 'W'].shape[0]
            win_percentage = (win_count / total_matches) * 100
            print("\nПроцент побед команд "f"{command}: {round(win_percentage, 2)}%\n")
            for index, row in stat_team_df.iterrows():
                print(f"Победа/Ничья/Поражение - {row['wins_draws_lose']}, "
                      f"карт сыграно в сумме: {round(row['maps_played'])},\n"
                      f"Сумма Убийств: {round(row['total_kills'])}, Сумма смертей: {round(row['total_death'])}, "
                      f"К/Д: {row['k_d_ratio']}\n")
        except ZeroDivisionError:
            pass
        for command_map in UNIQUE_MAP:
            try:
                unique_map = command_df[command_df['map_map'] == f'{command_map}']
                total_played_on_unique_map = unique_map.shape[0]
                win_count_on_map = unique_map[unique_map['w_l'] == 'W'].shape[0]
                win_percentage_on_map = (win_count_on_map / total_played_on_unique_map) * 100
                print("Процент побед команд "f"{command} на карте: {command_map} - {round(win_percentage_on_map, 2)}%")
            except ZeroDivisionError:
                pass
        team_df = df[df['team.1'] == f'{command}'] # это колонка только для команды со статистикой игроков команды
        for index, row in team_df.iterrows():
            print(f"Команда: {command} {row['name']} - Процент хедшота: {row['headshots_from_crew']},"
                  f" K/D: {row['k_d_ratio_from_crew']}")


if __name__ == '__main__':
    main()
