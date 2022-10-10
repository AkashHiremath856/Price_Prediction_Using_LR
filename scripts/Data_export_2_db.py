import sqlite3

con = sqlite3.connect("Bengaluru_House_Database.db")
cur = con.cursor()


def insert():
    l = []
    f = open('bengaluru_house_prices_without_dummies.csv', 'r')
    c = f.readlines()

    for i in range(1, len(c)):
        c[i] = c[i].strip('\n')
        l.append(c[i])

    f = []
    for i in range(len(l)):
        for d in (l[i].split(',')):
            f.append(d)

    i = 0
    j = 0
    for k in range(len(f)):
        j = i+4
        df = (f[i:j+1])
        print(df)
        if f[i:j+1] == []:
            break
        con.executemany(
            "INSERT INTO Bengaluru_House_Data VALUES(?,?,?,?,?)", [df])
        i = j
        i += 1

    con.commit()


insert()
# try:
#     cur.execute(
#         "CREATE TABLE Bengaluru_House_Data(location,total_sqft,bath,price,bhk)")
#     insert()

# except sqlite3.OperationalError:
#     if cur.execute('select * from Bengaluru_House_Data') == []:
#         insert()
