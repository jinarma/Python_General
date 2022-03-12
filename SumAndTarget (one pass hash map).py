# input -> nums = [int, int, int,...], target = int
# output -> indices = [int, int] which corrospond to nums values and whose sum = target.
# complete in less than O(n^2)
# e.g.
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

def twoSum(nums, target):
    dictionary = {}
    for i, ele in enumerate(nums):
        temp = target - ele
        if temp in dictionary:
            return [dictionary[temp], i]
        dictionary[ele] = i


num_list = [2, 1, 9, 4, 4, 56, 90, 3]
target = 8
print(twoSum(num_list, target))  # gets a list of indicies