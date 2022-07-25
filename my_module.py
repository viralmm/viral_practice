def number(x,y, *num):
    s= x + y
    for i in num:
        s += i
    return s

def firoz(a,b, *num):
    v= a + b
    if len(num):
        y = num[:2]
        for i in y:
            v -= i
    return v

def hello(): 
    print('hello') 

def viral(x,y):
    return x + y




