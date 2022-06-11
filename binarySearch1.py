def cronk(target, nums):
	l, r, mid = 0, len(nums)-1, len(nums)//2
	if target == nums[0]:
		print(l)
		return l
	elif target == nums[-1]:
		print(r)
		return r
	elif nums[mid] == target:
		print(mid)
		return mid
	while nums[mid] != target:
		mid = (l+r)//2
		if abs(l-r) <= 1 and target != nums[mid]:
			print(-1)
			return -1
		if target > nums[mid]:
			l = mid
		elif target < nums[mid]:
			r = mid
		elif target == nums[mid]:
			print(mid)
			return mid
		elif l == r:
			if target != nums[mid]:
				print(-1)
				return -1


# cronk(2, [-1, 0, 3, 5, 9, 12])
# cronk(5, [2, 5])
cronk(0, [-1, 0, 5])
