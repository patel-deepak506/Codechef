'''
NAVHW_009:: Write a program to check if the given number is divisible by 5, 11, both or none. 
If it is divisible by 5 then print 5
If it is divisible by 11 then print 11
If it is divisible by 5 and 11 then print “Both”
If it is not divisible by 5 and not divisible  11 then “none”
'''
n=int(input("number"))
if n%5==0:
	if n%11==0:
		print("both")
	else:
		print("it is divisible by 5")
else:
	if n%11==0:
		print("it is divisible by 11")
	else:
		print("none")
