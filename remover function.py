def remover(Value,Start,Stop):
    '''removes Strings of {Value} from {Start} to {Stop} indexs.
    then concats remaining strings. -> None
    {Value}=Str ,{Start}=int ,{Stop}=int'''
    inp=Value
    S=Start
    St=Stop
    if St>100:
        print(inp)
    else:
        v=inp[0:S]
        n=inp[St+1:]
        print(v+n)