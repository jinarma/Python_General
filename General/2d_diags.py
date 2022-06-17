size = int(input())
arr_2d = []
for i in range(size):
    arr_2d.append(list(map(int, input().split())))
diag_sum = 0
for i in range(size):
    diag_sum += arr_2d[i][i]
for i in range(size):
    diag_sum += arr_2d[size-1-i][i]
if size % 2 != 0:
    diag_sum -= arr_2d[size//2][size//2]
other_sum = 0
for ele in arr_2d:
    other_sum += sum(ele)
other_sum = other_sum-diag_sum
print(diag_sum-other_sum)