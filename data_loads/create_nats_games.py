import util_functions as uf

# This script creates the Nationals Schedule 2010-2018 AWS Table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE nats_games(
        game_datetime timestamp PRIMARY KEY,
        game_nbr integer
    )
    """)
    # TODO add game attendance
    conn.commit()
