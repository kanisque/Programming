
arrA = [1,3,4,6,7,8,10]
arrB = [0,2,5,9,11,12,13]
# arrA = [0,2]
# arrB = [1]

# Seperate function to validate input and corner cases
def validInputs(arrA, arrB):
    if len(arrA) == 0 and len(arrB) == 0:
        return False
    return True


# Create a new sorted array, return the middle element if odd / avg of middle elements if even
def medianByMerge(arrA, arrB):
    #Always validate inputs
    if not validInputs(arrA, arrB):
        return ('Provide valid inputs')

    arrC = sorted(arrA + arrB)
    lenC = len(arrC)
    return arrC[lenC // 2] if not lenC % 2 == 0 else ((arrC[lenC // 2] + arrC[(lenC // 2) + 1]) / 2)


# Count the elements using two pointers, return middle element if odd / avg of middle elements if even
def medianByCount(arrA, arrB):
    #Always validate inputs
    if not validInputs(arrA, arrB):
        return ('Provide valid inputs')

    pointyA = 0
    pointyB = 0
    totlen = len(arrA) + len(arrB)
    if totlen % 2 == 0:
        first = totlen // 2
        second = first + 1
    else:
        first = totlen // 2
        second = first

    firstElement = None
    secondElement = None
    count = 0
    while True:
        if arrA[pointyA] <= arrB[pointyB]:
            pointyA += 1
            count += 1
        else:
            pointyB += 1
            count += 1
        if count == first:
            firstElement = min(arrA[pointyA],arrB[pointyB])
        if count == second:
            secondElement = min(arrA[pointyA],arrB[pointyB])
            return ((firstElement + secondElement) / 2)
    return None


print(medianByMerge(arrA, arrB))
print(medianByCount(arrA, arrB))
