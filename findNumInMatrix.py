def findNumInMatrix(matrix,target):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return False
    n = len(matrix[0])
    lo, hi = 0, len(matrix) * n
    while lo < hi:
        mid = (lo + hi) / 2
        x = matrix[int(mid/n)][int(mid%n)]
        if x < target:
            lo = mid + 1
        elif x > target:
            hi = mid
        else:
            return((int(mid//n),int(mid%n)))
    return False

matrix = [[1,5,9,10],
        [14,20,21,22],
        [30,34,43,45],
        [50,52,56,58]]
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
print(findNumInMatrix(matrix,1))
print(findNumInMatrix(matrix,58))
print(findNumInMatrix(matrix,34))
print(findNumInMatrix(matrix,35))