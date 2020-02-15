
arr = [8,9,4,100,10,7,1,66,66,7,98,89,89]
print(arr)
min = int()
temp = int()
temp1 = int()
for i in range(0,arr.__len__()):
	min = arr[i]
	for j in range(i,arr.__len__()):
		if(arr[j] <= min):
			min = arr[j]
			temp = j
	temp1 = arr[temp]
	arr[temp] = arr[i]
	arr[i] = temp1
print(arr)
