#The program reads in a sequence of natural numbers and computes the number of entries, the sum, the average and the minimum.
x=input("Input:")
x=int(x)
n=0
s=0
a=0
m=x
while(x!=-1):
    n=n+1
    s=s+x
    if(m>x):
        m=x
    x=input("Input:")
    x=int(x)
if(n==0):
    a=-1
    m=-1
else:
    a=s/n
print('Number of Entries:') 
print(n)
print('Sum:')
print(s)
print('Average:')
print(a)
print('Minimum:')
# it looks like I learned how to use git today
