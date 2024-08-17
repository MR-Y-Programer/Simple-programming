'''simple to do list
enter q in input to close and print list'''
lst=[]
x=0
while True:
    e=input('Enter your value:')
    lst.append(e)
    print('Added!')
    if e=='q':
        lst.remove('q')
        break
for i in lst:
    x=x+1
    print(x,'_',i)