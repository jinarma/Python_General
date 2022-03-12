# input -> nums = [int, int, int,...], target = int
# output -> indices = [int, int] which corrospond to nums values and whose sum = target.
# complete in less than O(n^2)
# e.g.
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

def twoSum(nums, target):
    new_list = []
    for i, ele in enumerate(nums):
        if target - ele in nums[i+1:] and new_list == []:
            temp = ele
            new_list.append(i)
            continue
        try:
            if ele == target - temp:
                new_list.append(i)
        except UnboundLocalError:
            pass
    return new_list


num_list = [2, 1, 9, 4, 4, 56, 90, 3]
target = 8
print(twoSum(num_list, target))  # gets a list of indicies
