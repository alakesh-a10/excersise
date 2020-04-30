import sqlite3 as sql
#open("test.db", 'w').close()
con=sql.connect("test.db")
#con.execute("create table stu(rno int, name text, cls int)")
while True:
    r=int(input("Enter roll no : "))
    n=input("Enter name : ")
    cl=int(input("Enter class(numeric) : "))
    t=(r,n,cl)
    con.execute('insert into stu values(?, ?, ?)', t)
    x=input("Do you wish to enter more?(y/n)")
    if x.lower()=='y':
        continue
    else:
        break
con.commit()
con.close()
print("Data in the table\n|##################################|\n\n", sep=' ', end='n', file=sys.stdout, flush=False)
con=sql.connect("test.db")
q=con.cursor()
q.execute("select * from stu")
for data in q:
    print(data)
print(q)
con.close()
