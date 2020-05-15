a = int(input("Enter the number"))
facti=1
def fact(a):
	global facti
	i=1
	while(i<=a):
			facti=facti*i
			i=i+1

	print(facti)	
	

fact(a)				

