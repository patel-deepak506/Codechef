n=int(input())
sum1=0
m=n
while 0<m:
	rem=m%10
	sum1=sum1*10 +rem
	m//=10
print(sum1)
if sum1==n:
	print("YES",sum1)
else:
	print("NO",sum1)