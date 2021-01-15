'''
NAVHW_038: Draw a flowchart to input a number and check whether the entered number is a perfect number or not. (A perfect number - the sum of the factors less than n is equal to the number 
Example- 6 - 1+2+3 = 6)
	Sample Input:
	6
	Sample Output:
	Perfect number

	Sample Input:
	5
	Sample Output:
	Not a perfect number
'''
n=int(input())
sum1=0
a=1
while a<n:
	if n%a==0:
		sum1+=a
	a=a+1
if sum1==n:
	print(sum1,"is perfect number")
else:
	print(sum1,"is not perfect number")



