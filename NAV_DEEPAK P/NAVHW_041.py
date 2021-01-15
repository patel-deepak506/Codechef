n=int(input())
i=2
b=(n//2)+1
if 1<b:
	while i<=b:
		if n%i==0:
			print("not a prime numbers")
			break
		i+=1
	else:
		print("prime number")
else:
	print("not prime numbers")