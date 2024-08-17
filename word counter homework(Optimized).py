s=input('enter you value:')
w=s.split(' ')
n={}
for i in w:
    m=w.count(i)
    n[i]=m
print(n)