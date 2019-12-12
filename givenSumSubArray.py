# Input
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10

def main():
    numTestCases = int(input())
    for x in range(numTestCases):
        temp, findSum = map(int, input().split())
        arr = list(map(int, input().split()))
        header = 0
        tail = 0
        windowSum = arr[0]
        flag = False
        while not flag:
            if windowSum == findSum:
                print(header+1,tail+1)
                break
            elif windowSum < findSum:
                tail += 1
                if tail == len(arr):
                    print(-1)
                    break
                windowSum += arr[tail]
            elif windowSum > findSum:
                windowSum -= arr[header]
                header += 1
                if header == len(arr):
                    print(-1)
                    break
                if tail < header:
                    tail = header
                    windowSum = arr[header]
            

if __name__ == '__main__':
    main()