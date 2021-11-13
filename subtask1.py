# Calculate the closest square number smaller or equal to n.
n=input("Input:")
n=int(n)
q=0
r=0
while(n>=r*r): 
	r=r+1
	r=r-1
	q=r*r
	print(q)
