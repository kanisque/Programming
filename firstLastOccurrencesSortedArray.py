# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x.
class Solution:
    def getRange(self, nums, target):
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > A[mid]: left = mid + 1
                else: right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]: left = mid + 1
                else: right = mid - 1
            return right

        left = binarySearchLeft(nums, target)
        right = left + binarySearchRight(nums[left:], target)
        return [left, right] if left <= right else [-1, -1]

# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
print(Solution().getRange(arr, 1))
# [0, 0]
print(Solution().getRange(arr, 2))
# [1, 4]
print(Solution().getRange(arr, 3))
# [5, 5]
print(Solution().getRange(arr, 5))
# [-1, -1]
print(Solution().getRange(arr, 8))
# [8, 9]