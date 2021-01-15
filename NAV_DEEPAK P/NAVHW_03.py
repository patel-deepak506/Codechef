#NAVHW_003:Draw a flow chart for finding the 2nd maximum number from 3 numbers given as input. (Without using AND / OR)

a=int(input("first number"))
b=int(input("second number"))
c=int(input("third number"))
if a<b<c:
	print("second max",b)
else:
	if a<c<b:
		print("second max",c)
	else:
		print("second max",a)