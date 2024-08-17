def letcounter(Value):
    '''counts and prints letters of {Value} -> None
    {Value}=Str'''
    l={}
    for i in Value:
        e=Value.count(i)
        l[i]=e
    print(l)