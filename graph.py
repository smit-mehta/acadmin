import numpy as np
from PyQt4.Qt import *
from PyQt4.Qwt5 import *
from PyQt4.Qwt5.qplt import *
from pysqlite2 import dbapi2 as sqlite
from cgpa2ex import Startcgpa2

con = sqlite.connect('text.db')
cur = con.cursor()

application = QApplication([])

numeqdict = {}

cur.execute("select * from grades")
for row in cur:
    numeqdict[row[0]] = row[1]
    

cur.execute("select max(semester) from acads")
a = cur.fetchone()
x = np.arange(1, a[0]+1, 1)

def calc_gpa(x):
    y = []

    for i in x:
        t = (int(i), )
        cur.execute("select * from acads where semester = ? and grade<>'null'", t)
        
        gpat = 0
        creditsum = 0

        for row in cur:
            gpat = gpat + row[3]*numeqdict[row[4]]
            creditsum = creditsum + row[3]

        if gpat==0:
            y.append(float(0))
        else :
            y.append(float(gpat)/creditsum)

    return y

def calc_cgpa(x):
    
    a = Startcgpa2()
    b = float(a.ui.cgpa.text())
    y = []
    
    for i in x:
        y.append(b)
    
    return y


p = Plot(
    Curve(x, calc_gpa(x), Pen(Blue, 5), Symbol(Square, Red, 10), "GPA"), 
    Curve(x, calc_cgpa(x), Pen(Green, 5), "CGPA"),
    Axis(Y1, Lin, "GPA"),
    Axis(X1, Lin, "Semesters"))

QPixmap.grabWidget(p).save('graph.png', 'PNG')
