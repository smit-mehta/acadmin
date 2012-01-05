from pysqlite2 import dbapi2 as sqlite

con = sqlite.connect('text.db')
cur = con.cursor()



"""
Create
"""
"""
cur.execute("create table acads (semester INTEGER, subjectcode VARCHAR[8], subjecttitle VARCHAR[20], credits INTEGER, grade VARCHAR, bunksallowed INTEGER, bunksdone INTEGER, attendance FLOAT, totalclasses INTEGER)")

cur.execute("create table defsem (defaultsem INTEGER)")


cur.execute("create table referencess (subjectcode1 VARCHAR[8], reference VARCHAR[25], referencepath VARCHAR[5000])")

cur.execute("create table bunk (subjectcode VARCHAR[8], day INTEGER, month INTEGER, year INTEGER, semester INTEGER)")

cur.execute("create table reminder (subjectcode VARCHAR[8], description VARCHAR[250], day INTEGER, month INTEGER, year INTEGER)")

cur.execute("create table timetable(day INTEGER, slot INTEGER, subjectcode VARCHAR[8], semester INTEGER)")
cur.execute("create table days (days INTEGER)")
cur.execute("create table timeslots (slots VARCHAR[25])")

cur.execute("create table grades (grade VARCHAR[4], numeq FLOAT)")

cur.execute("create table timetableflag (flag INTEGER)")
cur.execute("create table cgflag (flag INTEGER)")


"""
"""
delete
"""


cur.execute("delete from timetableflag")
cur.execute("delete from cgflag")
cur.execute("delete from acads")
cur.execute("delete from referencess")
cur.execute("delete from bunk")
cur.execute("delete from reminder")
cur.execute("delete from timetable")
cur.execute("delete from days")
cur.execute("delete from timeslots")
cur.execute("delete from grades")
cur.execute("delete from defsem")
cur.execute("insert into defsem values(0)")

con.commit()





