# input -> nums = [int, int, int,...], target = int
# output -> indices = [int, int] which corrospond to nums values and whose sum = target.
# complete in less than O(n^2)
# e.g.
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

def twoSum(nums, target):
	one = -1
	two = -1
	for i, ele in enumerate(nums):
		if target - ele in nums[i+1:] and one == -1:
			one = i
			two = target - ele
			continue
		try:
			if ele == two and one != -1:
				two = i
				break
		except UnboundLocalError:
			pass
	if one == -1 or two == -1:
		return None
	else:
		return [one, two]

		
num_list = [150, 24, 79, 50, 88, 345, 3]
target = 200
print(twoSum(num_list, target))  # gets a list of indicies
