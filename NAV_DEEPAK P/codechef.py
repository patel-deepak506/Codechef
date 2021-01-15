##################question-2 ###############################################
#NAVHW_002:: Draw a flow chart for finding the maximum of 3 number.

# a=int(input("first number"))
# b=int(input("second number"))
# c=int(input("third number"))
# if a>b and b>c:
# 	print("max number",a)
# elif b>a and b>c:
# 	print("max number",b)
# else:
# 	print("max number",c)

#NAVHW_003:Draw a flow chart for finding the 2nd maximum number from 3 numbers given as input. (Without using AND / OR)

# a=int(input("first number"))
# b=int(input("second number"))
# c=int(input("third number"))
# if a<b<c:
# 	print("second max",b)
# elif a<c<b:
# 	print("second max",c)
# else:
# 	print("second",a)

#NAVHW_004: Draw a flow chart for swapping two numbers without using 3rd/temp variable. (Without using a,b = b,a)

# a=int(input("first number"))
# b=int(input("second number"))
# a=a-b
# b=b+a
# a=b-a
# print(a,b)

#NAVHW_005:: Write a program to take two numbers A and B as input from the user and print the number less than A which completely divides the number.

# a=int(input("first number"))
# b=int(input("second number"))
# c=a%b
# d=a-c
# print(d)


# a=int(input("first number"))
# sum1=1
# while 0<a:
# 	rem=a%10
# 	sum1*=rem
# 	a=a//10

# print(sum1)

n=int(input("first number"))
a=1
d=0
b=n**(1/2)
while a<b:
	b%a==0
	d=n//a
	a=a+1
if d==n:
	print("prime")
else:
	print("not prime")


