# 41. Автомобильный гараж: список владельцев, список автомобилей, список сторожей, журнал прихода и ухода автомобилей.
import sqlite3
con=sqlite3.connect('Avto_garage.db')
cursorObj=con.cursor()
def create():
    cursorObj.execute(
        'CREATE TABLE Owners(id integer primary key autoincrement,name text)')
    con.commit()
    cursorObj.execute("CREATE TABLE listOFcars(id integer primary key,name text)")
    con.commit()
    cursorObj.execute("CREATE TABLE listOFwatchmen(id integer primary key,name text)")
    con.commit()
    #журнал прихода
    cursorObj.execute("CREATE TABLE ArrivaLog(date text)")
    con.commit()
    #журнал ухода
    cursorObj.execute("CREATE TABLE DepartureLog(date text)")
def intoValueDB(value):
    cursorObj.execute('insert into Owners(name) values(?)',value)
    con.commit()
create()
s = input()
value = s.split()
while (str(value[0]) != str(0)):
    intoValueDB(value)
    s = input()
    value = s.split()
con.close()