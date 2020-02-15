strg = "IAMKING"
n = 3
l = len(strg)
k = 0
j = 0
ls = ""
t = 0
while(l>0):
    k = k + n
    #if(k>len(strg)-j):
    #k = k%len(strg)
    #print(strg[k-1])
    if(k>len(strg)):
        j = k
        for i in range(len(strg)-1):
            if(i+1>n):
                t = t + 3
            print("t",t)
            if(i != t-1):
                #print(i)
                ls = ls + strg[i]
                #print(ls)
                #print()
        strg = ls
        #else:
        #    strg = strg + strg[i]
    print(strg[k-1])
    l -= 1
    #print(j)
