'''
NAVHW_054: Write a program to store the names of 25 people in your classroom, in reverse order.
	
	Input:
Ram
	Shyam
	Sam
	Ravi
	Pallavi

	Output:
	Pallavi
	Ravi
	Sam
	Shyam
	Ram
'''
n=int(input())
lst=[]
counter=1
while counter<=n:
	name=input()
	lst.append(name)
	counter+=1
print( )
i=n-1
while i>=0:
	print(lst[i])
	i-=1

