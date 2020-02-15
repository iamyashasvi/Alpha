#sum of adject number
def matrixx(sze):
    newarr1 = [[input() for _ in range(sze)] for _ in range(sze)]
    return newarr1



sze = int(input("Enter the size"))
newarr = matrixx(sze)
print(newarr)
summ = 0
r = int(input("Enter the row"))
c = int(input("Enter the column"))
#summ = int(newarr[r][c])
#for i in range(sze):
#    for j in range(sze):
#if(c-1>=0):
#    summ += int(newarr[r][c-1])
#if(c+1<=sze-1):
#    summ += int(newarr[r][c+1])
#if(r+1<=sze-1):
#    summ += int(newarr[r+1][c])
#if(r-1>=0):
#    summ += int(newarr[r-1][c])
#if(r-1>=0 and c-1>=0):
#    summ += int(newarr[r-1][c-1])
#if(r+1<=sze-1 and c+1<=sze-1):
#    summ += int(newarr[r+1][c+1])
#if(r-1>=0 and c+1<=sze-1):
#    summ += int(newarr[r-1][c+1])
#if(r+1<=sze-1 and c-1>=0):
#    summ += int(newarr[r+1][c-1])
for i in range(r-1,r+2):
    if(i>=0 and i <= sze-1):
        for j in range(c-1,c+2):
            if(j>=0 and j <= sze-1):
                summ += int(newarr[i][j])
            else:
                continue
    else:
        continue
print(summ)
