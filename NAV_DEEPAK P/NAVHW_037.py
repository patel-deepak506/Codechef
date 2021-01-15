'''
NAVHW_037: Draw a flowchart to check if the given number is a strong number or not.
A strong number is a special number whose sum of the factorial of digits is equal to the original number. 
For example, 145 is a strong number. Since, 1! + 4! + 5! = 145
'''
n=int(input())
sum1=0
c=n
m=0
d=0
while n!=0:
	m=n%10
	d=m
	fact=1
	while d>0:
		fact*=d
		d-=1
	sum1+=fact
	n//=10
if sum1==c:
	print("this is a strong number")
else:
	print("This is not a strong number")