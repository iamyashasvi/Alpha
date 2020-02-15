def SubArraySum(arr, n):
    temp,result = 0,0

    # Pick starting point
    for i in range(0, n):

        # Pick ending point
        temp=0;
        for j in range(i, n):

            # sum subarray between
            # current starting and
            # ending points
            temp+=arr[j]
            result += temp
            print(temp," ",result)
        print("final",temp," ",result)
    return result
arr = [1, 2, 3]
n = len(arr)
print ("Sum of SubArray :" ,SubArraySum(arr, n))
