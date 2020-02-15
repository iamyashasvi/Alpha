def divide_num(ls):
    lss = []
    for i in range(len(ls)):
        lss.append(float(ls[i]/2))
    return lss
ls = [2,4,6,8,10]
print(divide_num(ls))
