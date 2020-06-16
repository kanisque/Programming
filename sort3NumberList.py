# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]

def sortNums(nums):
    countOne, countTwo, countThree = 0,0,0
    for i in nums:
        if i == 1:
            countOne += 1
        elif i == 3:
            countThree += 1
    countTwo = len(nums) - (countOne + countThree)
    for i in range(len(nums)):
        if countOne > 0:
            nums[i] = 1
            countOne -= 1
        elif countTwo > 0:
            nums[i] = 2
            countTwo -= 1
        else:
            nums[i] = 3
            countThree -= 1
    return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]