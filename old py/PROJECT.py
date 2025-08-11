import mysql.connector as m

a=m.connect(user='root',host='localhost',password='clash')
mycursor=a.cursor()
mycursor.execute("create database if not exists hotel")
mycursor.execute("use hotel")
mycursor.execute("create table if not exists checkin(days varchar(50),names varchar(20),aadhar varchar(20),date varchar(20),typenumber varchar(20))") 
mycursor.execute("create table if not exists checkout(typenumber varchar(20),guests int,fare int,days int,tbill int,date varchar(20))")
a.commit()
           
           
   
