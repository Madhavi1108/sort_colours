class Solution(object):
    def sortColors(self, nums):
        nums.sort()
        return nums


a = input().split()
numbers = [int(i) for i in a]
solution = Solution()
ans = solution.sortColors(numbers)
print(ans)
