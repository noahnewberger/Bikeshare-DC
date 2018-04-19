import mlbgame
import pandas as pd
import util_functions as uf


# Define Years of Interest (2010-2018)
years = [year for year in range(2010, 2018 + 1)]

results = []
for year in years:
    # Pull all games from MLBGAME API
    schedule = mlbgame.games(year, 4, home='Nationals')

    games = mlbgame.combine_games(schedule)
    for game in games:
        print(game.game_id)
        game_overview = mlbgame.overview(game.game_id)
        print(vars(game_overview))
        continue
        game_attendance = int(game_overview.attendance.replace(",", ""))

        if (game_overview.game_type != 'S'):  # Game Type, should be == 'R' for regular season
            if hasattr(game_overview, 'game_nbr'):
                game_nbr = game_overview.game_nbr
            else:
                game_nbr = 1
            game_datetime = game.date
            columns = ['game_datetime', 'game_nbr', 'game_attendance']
            results.append(pd.DataFrame.from_records([(game_datetime, game_nbr, game_attendance)], columns=columns))
            print("game at {} processed".format(game_datetime))



