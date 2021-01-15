'''
NAVHW_025:: Draw a flow chart to print the sum of numbers from 1 to N, where N is given as an input from the user
Sample input
5  
Sample output
15
'''
n=int(input())
a=1
sum_number=0
while a<=n:
	sum_number+=a
	a+=1
print(sum_number)
