''' Fetch data from database table and writing it in a csv file'''

import sqlite3
import csv
print("########~Welcome to data download Module~########")
x=input("Enter the class : ")
y=input("Enter Section : ")
x=x.upper()
y=y.upper()
con=sqlite3.connect("school.db")
result=con.execute("Select * from student where Class=? and Section=?",(x,y))
if result:
    fname=x+y+'.csv'
    h=['Admission Number','Name','Class','Section','Mobile Number']
    with open(fname,'w',newline='') as file:
        write=csv.DictWriter(file, fieldnames=h)
        write.writeheader()
        for x in result:
            write.writerow({h[0]:x[0],h[1]:x[1],h[2]:x[2],h[3]:x[3],h[4]:x[4]})
    file.close()
    con.close()
    print("Data stored successfully in \""+fname+"\" file")
else:
    print("Didnot Found any record in database")
