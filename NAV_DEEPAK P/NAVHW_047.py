'''
NAVHW_047: Draw a flowchart to print the following sequence.

*
* *
* * *
* * * *
* * * * *
'''
n=int(input())
a=1
while a<=n:
	b=1
	while b<=a:
		print("*",end=" ")
		b=b+1
	print("\n")
	a=a+1
