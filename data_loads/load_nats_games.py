import mlbgame
import pandas as pd
import util_functions as uf


def pull_nats_schedule():
    # Define Years of Interest (2010-2018)
    years = [year for year in range(2010, 2018 + 1)]
    # Pull all games from MLBGAME API
    schedule = mlbgame.games(years, home='Nationals')
    return schedule


def extract_game_info(schedule):
    # Extract game information from schedule
    results = []
    games = mlbgame.combine_games(schedule)
    for game in games:
        game_overview = mlbgame.overview(game.game_id)
        if (game_overview.game_type != 'S'):  # Game Type, should be == 'R' for regular season
            if hasattr(game_overview, 'game_nbr'):
                game_nbr = game_overview.game_nbr
            else:
                game_nbr = 1
            game_datetime = game.date
            columns = ['game_datetime', 'game_nbr']
            results.append(pd.DataFrame.from_records([(game_datetime, game_nbr)], columns=columns))
            print("game at {} processed".format(game_datetime))
    return results


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    # Pull Games in Nationals Schedule
    schedule = pull_nats_schedule()
    # Concatentate one big dataframe
    combined_df = pd.concat(extract_game_info(schedule), axis=0)
    # Drop duplicates because API sometimes pushes out same game twice
    combined_df.drop_duplicates(inplace=True)
    print(combined_df)
    # Output dataframe as CSV
    outname = "nats_games_2010_2018"
    combined_df.to_csv(outname + ".csv", index=False, sep='|')
    # Load to Database
    uf.aws_load(outname, "nats_games", cur)
    # Commit changes to database
    conn.commit()
