class Bank:
	
	def _init_(self):
		self.bal = 20000
	def signup(self):
		self.FirstName=input("enter FirstName")
		self.email=input("enter Email")
		self.password=input("enter a password")
		self.bal = 20000
	def display(self):
		print(self.FirstName)
		print(self.email)
		print(self.password)

	def checkBal(self):
		print("===Your Bal ==>",self.bal)
	def wid(self):
		amt=int(input("enter amt"))
		if(self.bal - amt <5000):
			self.checkBal()
			print("MIN BAL MUST BE 5000 you can wid max",(self.bal-5000))
		else:
			self.bal=self.bal-amt
			print("wid====done")
			self.checkBal()

	def dep(self):
		amt=int(input("enter amt"))
		self.bal=self.bal+amt
		print("dep====done")
		self.checkBal()

	def login(self,email,password):
		if(self.email == email and self.password == password):
			return True
		else:
			return False

users=[]
while(True):
	print("1 - Signup\n2 - Login\n3 - Exit")
	ch = int(input("enter choice"))
	if(ch==1):
		b=Bank()
		b.signup()
		users.append(b)
	elif(ch==2):
		email=input("enter email")
		password=input("enter password")
		for b in users:
			if(b.login(email,password)==True):
				while(True):
					print("1 - Wid\n2 - Dep\n3 - checkBal\n4 - Logout")
					ch2 = (int(input("enter choice : ")))
					if(ch2==1):
						b.wid()
					elif(ch2==2):
						b.dep()
					elif(ch3==3):
						b.checkBal()
					elif(ch2==4):
						break
			else:
				print("Invalid Credentials!!!!!!")
	elif(ch==3):
		exit()

print("====BYE====")