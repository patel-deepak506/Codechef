'''
NAVHW_055: Draw a flowchart to take N as input, followed by N elements. Take another input X and check whether it exists in the given N elements.
Sample Input:
7
1
3
4
5
34
87
990
6 (X)
Sample Output
NO
'''
n=int(input())
list1=[]
for i in range(n):
	N=int(input())
	list1.append(N)
a=1
x=int(input())
while a<=x:
	if x==list1[a]:
		print("YES")
	a+=1
print("NO")

