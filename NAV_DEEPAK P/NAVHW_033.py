'''
NAVHW_033:: Write a program to input a number and check if the number is prime or not.
Sample Input:
4

Sample Output:
Not a prime number

Sample Input:
11

Sample Output:
Prime number
'''
n=int(input())
i=2
if 1<n:
	while i<n:
		if n%i==0:
			print("not a prime numbers")
			break
		i+=1
	else:
		print("prime number")
else:
	print("not prime numbers")

# t=int(input())
# for i in range(t):
#     n=int(input())
#     a=0
#     b=1
#     while b<n:
#         if n%b==0:
#             a+=b
#         b+=1
#     if a==n:
#         print("Yes",a)
#     else:
#     	print("no",a)
    


 