'''
NAVHW_034:: Try to optimize/reduce the number of iterations of loop in the NAVHW_032.
'''
n=int(input())
a=1
root=n**(1/2)
while a<=root:
	if n%a==0:
		c=n//a
		print(a,c)
	a=a+1