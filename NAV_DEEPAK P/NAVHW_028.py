'''
NAVHW_028:: Draw a flow chart to input two numbers and print the HCF of them.
'''
n=int(input())
t=int(input())
a=0
while a<=n:
	a=a+1
	if t%a==0 and n%a==0:
		print("it is HCF number",a)
	else:
		print("not HCF number",a)
