##################question-2 ###############################################
#NAVHW_002:: Draw a flow chart for finding the maximum of 3 number.

a=int(input("first number"))
b=int(input("second number"))
c=int(input("third number"))
if a>b and a>c:
	print("max number",a)
else:
	if b>a and b>c :
		print("max number",b)
	else:
		print("max number",c)
