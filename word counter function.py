def wordcounter(Value):
    '''counts and prints words of {Value} -> None
    {Value}=Str'''
    f={}
    e=Value.split()
    for i in e:
        z=e.count(i)
        f[i]=z
    print(f)