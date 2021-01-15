'''
NAVHW_035:: Draw a flowchart to take a number N as input and print the sum of digits of that number.

SAMPLE INPUT
3425
SAMPLE OUTPUT
14

EXPLANATION: (3+4+2+5) = 14
'''
n=int(input())
a=0
sum1=0
while n!=0:
	sum1=n%10
	n=n//10
	a=a+sum1
print(a)

