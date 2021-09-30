import mysql.connector as sql
a=sql.connect(host='localhost',user='root',passwd='parthiv12',database='parthiv')
b=a.cursor()
b.execute('select * from empl')
d=b.fetchall()
for r in d:
    print(r)
