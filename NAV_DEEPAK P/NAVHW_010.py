'''
NAVHW_010:: Write a program to input three sides of a triangle and check if the triangle is valid. 
Sum of 2 sides should be greater than the third side which means 
a+b>c and a+c>b and c+b>a ⇒  Then triangle is possible.
'''

a=int(input("first line"))
b=int(input("second line"))
c=int(input("third line"))
if a!=0 and b!=0 and c!=0:
	if a+b>c and a+c>b and b+c>a:
		print("triangle is possible")
	else:
		print("triangle is not possible")
		
else:
	print("triangle is not possible")