class Solution:
    def findMaximumSquareIsland(self,nums):
        maxSize = 0
        for row in range(1,len(nums)):
            for col in range(1,len(nums[0])):
                if nums[row-1][col] > 0 and nums[row-1][col-1] > 0 and nums[row][col-1] > 0 and nums[row][col] > 0:
                    nums[row][col] = min(nums[row-1][col-1],nums[row][col-1],nums[row-1][col]) + 1
                maxSize = max(maxSize,nums[row][col])
        return maxSize



nums = [[1,0,1,0],
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]]
print( Solution().findMaximumSquareIsland(nums) )