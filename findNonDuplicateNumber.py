#Given a list of numbers, where every number shows up twice except for one number, find that one number.

def singleNumber(nums):
    for x in nums[1:]:
        nums[0] ^= x
    return nums[0]

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
