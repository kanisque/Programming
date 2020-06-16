class Solution:
    def searchInsert(self, nums, target):
        # Recursive Approach
        # def binarySearch(nums,target,start,end):
        #     if target > nums[-1]:
        #         return len(nums)
        #     if target < nums[0]:
        #         return 0
        #     mid = (start+end) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         if nums[mid-1] < target:
        #             return mid
        #         return binarySearch(nums,target,0,mid-1)
        #     else:
        #         if nums[mid+1] > target:
        #             return mid+1
        #         return binarySearch(nums,target,mid+1,end)

        # return binarySearch(nums,target,0,len(nums)-1)
        
        # Iterative Approach
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
                

print( Solution().searchInsert([1],0) )
#0
print( Solution().searchInsert([1],1) )
#0

print( Solution().searchInsert([1,3,5,6],0) )
#0
print( Solution().searchInsert([1,3],2) )
#1
print( Solution().searchInsert([1,3,5,6],2) )
#1
print( Solution().searchInsert([1,3,5,6],5) )
#2
print( Solution().searchInsert([1,3,5,6],7) )
#4