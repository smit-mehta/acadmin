# The global database interface between the programs and "database.db"

from pysqlite2 import dbapi2 as sqlite

con = sqlite.connect('database.db')
cur = con.cursor()
