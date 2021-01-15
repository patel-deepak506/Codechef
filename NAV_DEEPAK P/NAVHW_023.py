'''
NAVHW_023:: Draw a flow chart to print the multiplication table of 2
Output:
			2 X 1 = 2
			2 X 2 = 4
			2 X 3 = 6
			2 X 4 = 8
			2 X 5 = 10
			2 X 6 = 12
			2 X 7 = 14
			2 X 8 = 16
			2 X 9 = 18
			2 X 10 = 20
'''
table=2
count=1
add=table
while count<=10:
	print(table,"X",count,"=",add)
	count+=1
	add=count*table

