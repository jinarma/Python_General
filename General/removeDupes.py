def removeDuplicates(nums):
	for i, ele in enumerate(nums):
		if ele in nums[i:]:
			nums.remove(ele)
	return len(nums), nums


# print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates([1, 1, 2]))