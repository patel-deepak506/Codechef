'''
NAVHW_016:: Write the program to check NAVHW_014 then print NAVHW_015.
'''
a=int(input("first angle"))
b=int(input("second angle"))
c=int(input("third angle"))
if a!=0 and b!=0 and c!=0 and a+b+c==180:
	if a>=90 or b>=90 or c>=90:
		if a==90 or b==90 or c==90:
			print("right angle")
		else:
			print("obtuse angle")
	else:
		print("acute anfgle")
else:
	print("invalid triangle")