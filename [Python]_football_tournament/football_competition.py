"""
    Example of code of https://habr.com/ru/companies/yandex/articles/340784/ - football_tournament
"""
import pandas as pd

class TeamGoals:
    def __init__(self, score):
        self.score = score

    def first_team_goals(self):
        return self.score[0]

    def second_team_goals(self):
        return self.score[2]


class TeamWinner:
    def __init__(self, first_team_goals, second_team_goals):
        self.first_team_goals = first_team_goals
        self.second_team_goals = second_team_goals

    def win_first_team(self):
        if self.first_team_goals > self.second_team_goals:
            return 'WIN'
        elif self.first_team_goals < self.second_team_goals:
            return 'LOSE'
        return 'Draw'

    def win_second_team(self):
        if self.first_team_goals > self.second_team_goals:
            return 'LOSE'
        elif self.first_team_goals < self.second_team_goals:
            return 'WIN'
        return 'Draw'


if __name__ == '__main__':
    #input results of matches:
    list_of_matches = []
    print('Введите результат матча, если ввод закончен введите "/n"')
    while True:
        match = input()
        if match == '/n':
            break
        else:
            list_of_matches.append(match)

    df = pd.DataFrame({'match result': list_of_matches})
    df['first_team'] = df['match result'].apply(lambda x: str(x)[0:str(x).find('-') - 1])
    df['second_team'] = df['match result'].apply(lambda x: str(x)[str(x).find('-') + 2:len(str(x)) - 4])
    df['score'] = df['match result'].apply(lambda x: str(x)[len(str(x)) - 3:])

    df['first_team_goals'] = df['score'].apply(lambda x: TeamGoals(score=x).first_team_goals())
    df['second_team_goals'] = df['score'].apply(lambda x: TeamGoals(score=x).second_team_goals())

    df['who_win_1'] = df.apply(lambda row: TeamWinner(first_team_goals=row['first_team_goals'],
                                                      second_team_goals=row['second_team_goals']).win_first_team(),
                               axis=True)
    df['who_win_2'] = df.apply(lambda row: TeamWinner(first_team_goals=row['first_team_goals'],
                                                      second_team_goals=row['second_team_goals']).win_second_team(),
                               axis=True)

    df2 = df[['first_team', 'second_team', 'who_win_1', 'who_win_2']]

    df_1 = df2[['first_team', 'who_win_1', 'second_team']]
    df_1 = df_1.rename(columns={'first_team': 'main_team', 'who_win_1': 'result', 'second_team': 'competitor'})
    df_2 = df2[['second_team', 'who_win_2', 'first_team']]
    df_2 = df_2.rename(columns={'second_team': 'main_team', 'who_win_2': 'result', 'first_team': 'competitor'})
    df_all = pd.concat([df_1, df_2])
    df_all = df_all.reset_index(drop=True)
    df_matches = df_all.pivot(index='main_team', columns='competitor', values='result')

    df_goals1 = df[['first_team', 'first_team_goals', 'second_team_goals']]
    df_goals1 = df_goals1.rename(
        columns={'first_team': 'team', 'first_team_goals': 'goals_scored', 'second_team_goals': 'goals_conceded'})
    df_goals2 = df[['second_team', 'first_team_goals', 'second_team_goals']]
    df_goals2 = df_goals2.rename(
        columns={'second_team': 'team', 'second_team_goals': 'goals_scored', 'first_team_goals': 'goals_conceded'})
    df_goals = pd.concat([df_goals1, df_goals2])
    df_goals['goals_scored'] = df_goals['goals_scored'].astype(int)
    df_goals['goals_conceded'] = df_goals['goals_conceded'].astype(int)
    df_goals = pd.DataFrame({
        'scored_goals': df_goals.groupby(['team'])['goals_scored'].sum(),
        'conceded_goals': df_goals.groupby(['team'])['goals_conceded'].sum()
    })

    df_all = df_matches.merge(df_goals, left_index=True, right_index=True)
    print(df_all)


"""
    Введите результат матча, если ввод закончен введите "/n"
    a - c 0:1
    b - c 1:2
    a - b 4:5
    d - f 3:2
    a - d 2:2
    /n
                  a     b     c     d    f  scored_goals  conceded_goals
    main_team                                                           
    a           NaN  LOSE  LOSE  Draw  NaN             6               8
    b           WIN   NaN  LOSE   NaN  NaN             6               6
    c           WIN   WIN   NaN   NaN  NaN             3               1
    d          Draw   NaN   NaN   NaN  WIN             5               4
    f           NaN   NaN   NaN  LOSE  NaN             2               3
    
"""



