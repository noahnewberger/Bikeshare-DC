import time
import util_functions as uf
from psycopg2 import sql

uf.set_env_path()
conn, cur = uf.aws_connect()

snip = sql.SQL(', ').join(sql.Identifier(n) for n in ['foo', 'bar', 'baz'])
print(snip.as_string(conn))

import sys
sys.exit()
# CREATE TABLE on AWS
TIMESTR = time.strftime("%Y%m%d_%H%M%S")
numeric_cols = "col1 integer, col2 integer"
db_name = "final_db_" + TIMESTR
print(sql.SQL("CREATE TABLE {}(date date PRIMARY KEY,{})").format(sql.Identifier(db_name), sql.Identifier(numeric_cols)).as_string(conn))
