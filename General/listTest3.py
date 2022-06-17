class Solution:
	def countBits(self, n):
		new_list = []
		for i in range(n+1):
			temp = bin(i)
			temp = temp[2:]
			count = 0
			for j in temp:
				if j == '1':
					count += 1
			new_list.append(count)
		return new_list

obj = Solution()
print(obj.countBits(2))