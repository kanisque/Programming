#kLargestElements
import heapq
nums,k = [12,5,787,1,23],2

min_heap = nums[:k]
heapq.heapify(min_heap)
for i in range(k, len(nums)):
    if nums[i] > min_heap[0]:
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, nums[i])
min_heap = sorted(min_heap)
min_heap.reverse()
str1 = " " 
    # str1.join(s)) 
print(" ".join([str(x) for x in min_heap]))