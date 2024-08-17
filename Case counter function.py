def casecounter(Value):
    '''prints number of upper and lower cases of {Value} -> None
    {Value}=Str'''
    d={'UPPER':0,'lower':0}
    for i in Value:
        if i.isupper():
            d['UPPER']=d['UPPER']+1
        elif i.islower():
            d['lower']=d['lower']+1
    print(d)