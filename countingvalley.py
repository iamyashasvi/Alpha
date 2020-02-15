n = input()
s = raw_input()

level = 0
valleys = 0
for direction in s:
    if(direction == "U"):
        level += 1
        if(level == 0):
            valleys += 1
    else:
        level -= 1

print valleys

    countu = 0
    countd = 0
    count = 0
    alarm =0
    start = False
    if(s[0]=='U'):
        for i in range(n):
            if(s[i]=="D"):
                countd -= 1
                #print("D")
            else:
                countu += 1
                #print("U")
            count=countd+countu
            if(count == 0):
                alarm += 0.5
        return int(alarm)
    else:
        for i in range(n):
            if(s[i]=="D"):
                countd -= 1
                #print("D")
            else:
                countu += 1
                #print("U")
            count=countd+countu
            if(count==0 and s[i]=="U"):
                alarm += 1
        return alarm
