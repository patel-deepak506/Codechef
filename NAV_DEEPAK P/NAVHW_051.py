'''
AVHW_051: Draw a flowchart to take N as input and print the following sequence till N.
Sample Input 
9
Sample Output 
1 13 7 10 26 8 100 39 9
'''
n=int(input())
a=1
b=13
c=7
while c<=n:
	print(a)
	print(b)
	print(c)
	a=a*10
	b=b*2
	c=c+1