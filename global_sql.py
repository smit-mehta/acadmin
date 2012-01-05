from pysqlite2 import dbapi2 as sqlite
con = sqlite.connect('text.db')
cur = con.cursor()
