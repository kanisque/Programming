#kth largest element
import random

def quickSelect(nums,k):
    if not nums:
        return
    p = random.choice(nums)
    left,mid,right = [x for x in nums if x > p],[x for x in nums if x == p],[x for x in nums if x < p]
    # print(left,mid,right)
    nums,li,ri = left+mid+right, len(left), len(left)+ len(mid)
    return quickSelect(nums[:li], k) if k <= li else quickSelect(nums[ri:], k-ri) if k > ri else nums[li]

print(quickSelect([12,5,787,1,23],2))