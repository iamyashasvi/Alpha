def fibo(n):
    a = 0
    b = 1
    s =0
    arr = []
    if(n>0 and n<2):
        arr.append(a)
        arr.append(b)
        arr.append(a+b)
        return arr
    arr.append(a)
    arr.append(b)
    for i in range(1,n):
        s=a+b
        if(n<s):
            break
        arr.append(s)
        a,b=b,s
    return arr
n =50
print(fibo(n))
