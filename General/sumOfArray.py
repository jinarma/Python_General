def sum_of_arr(sum, arr):
    if bool(arr) == False:
        return sum
    else:
        sum += arr.pop()
        return sum_of_arr(sum, arr)
        
count = int(input())
arr = []
for i in range(count):
    arr.append(int(input()))
print('The sum of elements in array is', sum_of_arr(0, arr))