

import mysql.connector as con
class ContactApp:
	
	def __init__(self):

		self.db=con.connect(host="localhost",user="root",password="root" ,database="python3")

		self.mycursor=self.db.cursor(prepared=True)

			

	def createTable(self):
		#self.mycursor.execute("create table contacts(cid integer primary key auto_increment,cname varchar(20),cnumber varchar(20))")
		pass

	
	def addContact(self):	
		name=input("Enter contact")
		num=input("Enter Number ")	
		self.mycursor.execute("insert into  contacts(cname,cnumber)values(%s,%s)",(name,num))
		self.db.commit()

	def getAllContacts(self):
		self.mycursor.execute("select * from contacts")
		data=self.mycursor.fetchall()

		for c in data:
			print(c)


obj=ContactApp()

#obj.createTable()
obj.addContact()
obj.getAllContacts()				














