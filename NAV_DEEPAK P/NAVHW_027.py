'''
NAVHW_027:: Draw a flow chart to get a number ‘n’ as input. Then input n numbers. Then for each of the n numbers, print “even” if the number is even or and odd if the number is odd.
	
Sample input:
	7
	1
	4
	23
	95
	1203
	403
	84
	Sample output:
	Odd
	Even
	Odd
	Odd
	Odd
	Odd
	Even
'''
n=int(input())
a=1
while a<=n:
	num=int(input())
		if num%2==0:
			print("even")
		else:
			print("odd")
	a=a+1