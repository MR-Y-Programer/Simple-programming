'''appends input to a tuple
enter q or Q for stop an print tuple'''
t=()
a=list(t)
while True:
    inp=input('Enter your value:q-->stop:')
    if inp=='Q' or inp=='q':
        print('Ended!','Result:')
        break
    a.append(inp)
    print('Added!')
    p=tuple(a)
print(p)