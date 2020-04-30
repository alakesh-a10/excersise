print("View the test.db file")
import sqlite3 as sql
con=sql.connect("school.db")
c=con.execute("select count(*) from student where Class=? and section= ?",('XII','COMMERCE'))
for data in c:
   print(data)
con.close()
