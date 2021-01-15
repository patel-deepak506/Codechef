'''
NAVHW_006::  Write a program to take a number as input from the user and print
“Bingo” - If the number is even and >200
“Ringo” - If the number is odd and <200 
“CodeChef” - for any other number
'''

n=int(input("number"))
if n%2==0:
	if n>200:
		print("Bingo")
	else:
		print("CodeChef")
else:
	if n<200:
		print("Ringo")
	else:
		print("CodeChef")