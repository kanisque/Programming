def two_sum(nums, k):
    occur = {}
    for num in nums:
        if num in occur:
            return True
        occur[k-num] = 1
    return False
print(two_sum([4,7,1,-3,2], 5))
# True
print(two_sum([4,7,1,-3,2], 6))
# True
print(two_sum([4,7,1,-3,2], 7))
# False
