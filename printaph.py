def printaph(list1):
    z = len(list1)
    maxx = 0
    #ls = []
    for i in range(len(list1)):
        if(maxx<len(list1[i])):
            maxx = len(list1[i])
    #print(maxx)
    for i in range(maxx):
        for j in range(len(list1)):
            if(len(list1[j])<maxx):
                if(len(list1[j])+i>=maxx):
                    print(list1[j][maxx-i-1],end="")
                else:
                    print(" ",end="")
            elif(len(list1[j])==maxx):
                print(list1[j][maxx-i-1],end="")
        print(" ")
list1 = ["VIKAS","KINGKHAN","AMAN"]
printaph(list1)
