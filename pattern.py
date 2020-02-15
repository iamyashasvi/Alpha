n = 9
l1 = n*2
b = True
k =0
while(l1-1>0):
    if(b==True and n>1):
        for i in range(2*n):
            print(n,end="")
        n -= 1
        print("")
    elif(n==1):
            print(n,end="")
            b =False
            n += 1
            print("")
    else:
        for i in range(2*n-1):
            print(n,end="")
        n +=1
        print("")
    l1 -= 1


# if(k>len(strg)):
#     j = k
#     for i in range(len(strg)):
#         t = i
#         if(i+1 > n):
#             t = t + 3
#         print("t",t)
#         if(i != t-1):
#             #print(i)
#             ls = ls + strg[i]
#             #print(ls)
#             #print()
