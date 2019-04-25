from sys import maxsize

# inputArr = [-2,1,2,3,-2,3,-5,7,1,2,-2,-1,-3,2,4,1,5,-9,3]
#inputArr = [-2, -3, 4, -1, -2, 1, 5, -3]
inputArr = [-3,-2,-1,-5,-4]

def main():
    kadane()

def kadane():
    startIndex = 0
    endIndex = 0
    maxSumSoFar = - maxsize - 1
    maxSumEndingHere = 0
    
    for index,number in enumerate(inputArr):
        maxSumEndingHere = maxSumEndingHere + number
        if(maxSumEndingHere > maxSumSoFar):
            maxSumSoFar = maxSumEndingHere
            endIndex = index + 1

        if(maxSumEndingHere < 0):
            maxSumEndingHere = 0
            startIndex = index+1
            
    print("Max Sum:",maxSumSoFar,"for Sub Array:",inputArr[startIndex:endIndex])

if __name__ == "__main__":
    main()