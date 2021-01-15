'''
NAVHW_015:: Write a program to input three angles of a triangle and check which type of triangle based on the angles - right, obtuse, acute.
'''
a=int(input("first angle"))
b=int(input("second angle"))
c=int(input("third angle"))

if a>=90 or b>=90 or c>=90:
	if a==90 or b==90 or c==90:
		print("right angle")
	else:
		print("obtuse angle")
else:
	print("acute anfgle")
