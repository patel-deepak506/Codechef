'''
NAVHW_049: Draw a flowchart to print the following sequence.
        *
      * *
    * * *
  * * * *
* * * * *
'''
n=int(input())
# a=1
# while a<=n:
# 	b=a
# 	while b<+n:
# 		print("*",end=" ")
# 		b+=1
# 	k=1
# 	while k
for i in range(1,n+1):
	print(" "*(n-i),"*"*i)