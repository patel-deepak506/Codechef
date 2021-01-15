a=[1,5,8,9]
b=[1,3,5,6,12,7]
i=0
for j in b:
	while i<len(a):
		if a[i]>=j:
			a.insert(i,j)
			break
		i+=1
print(a)
