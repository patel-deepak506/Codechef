'''
NAVHW_022:: Draw a flow chart to print Hello “name” for 20 times, here “name” is entered by the user
Sample Input:
Jane Doe
Sample Output:
Hello Jane Doe
	..(18)
Hello Jane Doe
'''
n=input("name=")
counter=1
while counter<=20:
	print("Hello",n)
	counter+=1