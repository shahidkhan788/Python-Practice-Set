# Selection sorting using swapping technique

arr = [2,3,6,6,5]

for i in range(len(arr)-1):
    for j in range(i,len(arr)-1):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp

myArr = set(arr)
newList = list(myArr)
newList.sort()
print(arr)
