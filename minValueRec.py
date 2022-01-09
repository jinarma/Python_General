def minimum(minVal, arr):
    if bool(arr) == False:
        return minVal
    else:
        if minVal > arr[-1]:
            minVal = arr.pop()
            return minimum(minVal, arr)
        else:
            arr.pop()
            return minimum(minVal, arr)
size = int(input())
arr =[]
temp = []
for i in range(size):
    arr.append(int(input()))
for i in range(size):
    temp.append(arr[i])
print('Given Array :', temp)
print('Minimum element of array:', minimum(arr[0], arr))