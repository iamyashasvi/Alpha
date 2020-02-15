
arr = [2,3,4,1,9,33,11,90,5,12]
pi= 0
def quicksort(arr,s,l):
	if(s<l):
		pi = partition(arr,s,l)
		quicksort(arr,s,pi-1)
		quicksort(arr,pi+1,l)

def partition(arr,s,l):
	i = int(s)
	j = int(l)
	while(i<j):
		while(True):
			i=i+1
			if(arr[i]>pi):
				break
		while(True):
			j=j-1
			if(arr[j]<pi):
				break
		if(i<j):
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
	temp = arr[s]
	arr[s] = arr[j]
	arr[j] = temp
	return j

quicksort(arr,0,9)
print(arr)
