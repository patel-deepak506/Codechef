'''
NAVHW_011:: Write a program that takes a number n and checks if the number is an odd multiple of 3.
Example
	n = 24
		Not odd multiple of 3.
	n = 21
		Odd multiple of 3
'''

n=int(input("line"))
if n%3==0:
	if n%2!=0:
		print("Odd multiple of 3")
	else:
		print("Not odd multiple of 3")
