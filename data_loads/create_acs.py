import util_functions as uf

# This script creates the CaBi System information AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE acs (
        acs_id bigserial PRIMARY KEY,
        year integer,
        datanum integer,
        serial integer,
        hhwt integer,
        stateicp integer,
        statefip integer,
        county  integer,
        countyfips integer,
        metarea numeric,
        metaread numeric,
        city integer,
        citypop integer,
        gq integer,
        pernum integer,
        perwt integer,
        sex integer,
        age integer,
        race integer,
        raced integer,
        citizen integer,
        racesing numeric,
        racesingd numeric,
        racamind integer,
        racasian integer,
        racblk integer,
        racpacis integer,
        racwht integer,
        racother integer,
        empstat integer,
        empstatd integer,
        labforce integer,
        wkswork1 numeric,
        inctot integer,
        ftotinc integer,
        incwage integer,
        pwstate2 integer,
        tranwork integer,
        carpool integer,
        riders integer,
        trantime integer,
        qtrantim integer,
        qtranwor integer)
    """)
    conn.commit()