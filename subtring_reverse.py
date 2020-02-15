def arr(list2):
    list3 = []
    newls = []
    l2 = len(list2)
    for i in range(len(list2)):
        list3 = list2[len(list2)-1-i][::-1]
        #list3.append(list2[i][j])
        newls.append(list3)
        #print(newls)
    return newls
list2 = [[8,1,4],[7,9,2],[3,1],[4,8]]
print(list2)
list4 = arr(list2)
print(list4)
# comment optimise
