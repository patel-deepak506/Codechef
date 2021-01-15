'''
NAVHW_014:: Write a program to input three angles of a triangle and check if that triangle is possible to form?
[hint: Sum of all the angles must be equal to 180 degrees]
'''
a=int(input("first angle"))
b=int(input("second angle"))
c=int(input("third angle"))
if a!=0 and b!=0 and c!=0 and a+b+c==180:
	if 	a+b+c==180:
		print("triangle is possible")
	else:
		print("triangle is not possible")
else:
	print("invalid triangle")
