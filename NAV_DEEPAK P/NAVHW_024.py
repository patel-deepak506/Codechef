'''
NAVHW_024:: Draw a flow chart to take input n, print its multiplication table. 
Sample input:
	5
Sample output:
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
'''
table=int(input())
count=1
add=table
while count<=10:
	print(table,"X",count,"=",add)
	count+=1
	add=count*table
