class Bank :

	def _init_(self):
		
		self.bal=20000

	def signup(self):	

		self.firstname=input("Enter First Name")
		self.email=input("Enter Email")
		self.password=input("Enter password")


	def disp(self):
	
		print(self.firstname)
		print(self.email)
		print(self.password)

	def checkBal(self):
		print("====Your bal======",self.bal)


	def wid(self):
	
		amt=int(input("Enter the amt"))

		if(self.bal-amt<5000):
			self.checkBal()
			print("MIN BAL MUST BE 5000 you can wid max ",(self.bal-5000))	

		else:
			self.bal=self.bal-amt
			print("Wid====done")
			self.checkBal()





	def dep(self):
	
		amt=int(input("Enter amt"))
		self.bal=self.bal+amt
		print("dep===done")
		self.checkBal()

	def login(self,email,password):

		if(self.email==email and self.password == password):
			return True

		else:
			return False


user=[]

while(True):
	print("1-signup\n2-Login\n3-Exit")
	ch=int(input("Enter your choice"))

	if(ch==1):
			b=Bank()
			b.signup()
			user.append(b)

	elif(ch==2):
			 email=input("Enter email")
			 password=input("Enter password")

			 for b in user:
			 	 if(b.login(email,password) == True):
			 	 	while (True):
			 	 			print("1 - wid\n2- dep\n3- checkBal\n4- for Logout")
			 	 			ch2=int(input("enter You choice"))

			 	 			if(ch2==1):
			 	 				b.wid()	
			 	 			elif(ch2==2):
			 	 				d.dep()

			 	 			elif(ch2==3):
			 	 				b.checkBal()
			 	 			elif(ch2==4):
			 	 				break
			 	 else:
			 	     
			 	     print("Invalid login")
	elif(ch2==3):
	
			exit()

print("BYE")					 	     									
	