'''
NAVHW_050: Draw a flowchart to take N as input and print the following sequence.

Sample Input
9

Sample Output
10 2 20 4 30 6 40 8 50
'''
n=int(input())
a=2
c=10
while a<=n:
	print(c)
	print(a)			
	a+=2
	c+=10	
