if(c1<0 and c2>0 and m>0):
    c2 = c1*(-1) + c2
    m = c1*(-1) + m
    c1 = 0
if(c1>0 and c2<0 and m>0):
    c1 = c2*(-1) + c1
    m = c2*(-1) + m
    c2 = 0
if(c1>0 and c2>0 and m < 0):
    c1 = m*(-1) + c1
    c2 = m*(-1) + c2
    m = 0
if(c1 < 0 and c2 < 0 and m>0):
    if(c1 < c2):
        c2 = c1*(-1)+c2
        m = m+c2+c1*(-1)
        c1 = 0
    else:
        c1 = c2*(-1)+c1
        m = m+c1+c2*(-1)
        c2 = 0
if(c1 < 0 and m < 0 and c2 > 0):
    if(c1<m):
        m = c1*(-1)+m
        c2 = c2+m+c1*(-1)
        c1 = 0
    else:
        c1 = m*(-1)+c1
        c2 = c2+c1+m*(-1)
        m = 0
if(m<0 and c2 < 0 and c1 > 0):
    if(m<c2):
        c2 = m*(-1)+c2
        c1 = c1+c2+m*(-1)
        m = 0
    else:
        m = c2*(-1)+m
        c1 = c1+m+c2*(-1)
        c2 = 0
if(m<0 and c1<0 and c2<0):
    if(c1<m and c2<m):
        if(c1<c2):
            c2 = c1*(-1)+c2
            m = c1*(-1)+m
            c1 = 0
        else:
            c1 = c2*(-1)+c1
            m = c2*(-1)+m
            c2 =0
    #elif(c1<c2 and m<c2):
     #   if(c1<m):
