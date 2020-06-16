
def findPivot(nums):
        low = 0
        high = len(nums) -1
        
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid +1
            else:
                high = mid
        return low

def flipArray(nums,i,j):
    while i < j:
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
        j-=1
    return nums

# nums = [5,1,2,3,4]
nums = [3,4,5,1,2]
# nums = [3,4,5,6,7]
#Step 1 : Find pivot // or index of minimum number, same thing
pivot = findPivot(nums)
#Step 2 : Execute Order 'Flip-flop'
nums = flipArray(nums,0,pivot-1)
nums = flipArray(nums,pivot,len(nums)-1)
nums = flipArray(nums,0,len(nums)-1)

print(nums)