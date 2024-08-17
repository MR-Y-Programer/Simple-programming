'''counts letters of input and prints them in a dictionary'''
inp=input('Enter your value:')
num={}
for i in inp:
    c=inp.count(i)
    num[i]=c
print(num)