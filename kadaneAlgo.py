#Kadane's Algorithm

class Solution:
    def kadane(self,nums):
        startIndex, endIndex = 0, 0
        maxSumSoFar, maxSumEndingHere = float("-inf"), 0
        for index,num in enumerate(nums):
            maxSumEndingHere = maxSumEndingHere + num
            if(maxSumEndingHere > maxSumSoFar):
                maxSumSoFar = maxSumEndingHere
                endIndex = index + 1
            if(maxSumEndingHere < 0):
                maxSumEndingHere = 0
                startIndex = index + 1

        if endIndex <= startIndex:
            startIndex = endIndex-1
        # print("Max Sum SubArray:",nums[startIndex:endIndex])
        return(maxSumSoFar)

print(Solution().kadane([-2,1,2,3,-2,3,-5,7,1,2,-2,-1,-3,2,4,1,5,-9,3]))
print(Solution().kadane([-2, -3, 4, -1, -2, 1, 5, -3]))
print(Solution().kadane([-3,-2,-1,-5,-4]))
print(Solution().kadane([7,1,5,3,6,4]))