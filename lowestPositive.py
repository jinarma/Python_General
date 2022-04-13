def firstMissingPositive(nums):
        # tempList = nums
        nums.sort()
        for i, ele in enumerate(nums):
            if ele >= 0 and i < len(nums)-1:
                if nums[i+1] - ele != 1:
                    return ele+1
                else:
                    continue
                    
print(firstMissingPositive([1, 2, 0]))