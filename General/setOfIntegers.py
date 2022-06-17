# bhasad
size_of_arr = int(input())
list1 = list(map(int, input().split()))
sum_for_check = int(input())
final_list = []
high_difference_list = []
for index in range(len(list1)):
    for second_index in range(index + 1, len(list1)):
        if (list1[index] + list1[second_index]) == sum_for_check:
            final_list.append(f"{list1[index]},{list1[second_index]}")
            high_difference_list.append(abs(list1[index] - list1[second_index]))
print(final_list[high_difference_list.index(max(high_difference_list))])
