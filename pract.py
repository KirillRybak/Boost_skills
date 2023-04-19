x = {
    'a':1111,
    'b':11,
    'c':121,
    'd':1,
}

def max(x:dict):
    one = x['a']
    for i in x:
        m = x[i]
        if m>one:
            one=m
    return one


print(max(x))



