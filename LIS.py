#longest increasing subsequence
#  input   = 5 6 2 3 4 1 9 9 8 9 5
# f(input) = 5 ( 2 3 4 8 9 )

LISMemo = []
def LIS(input):
    LISMemo = [ 1 for x in range(len(input))]
    
    for i in range(1,len(input)):
        for j in range(i):
            LISMemo[i] = max(LISMemo[i], LISMemo[j]+1 if input[i]>input[j] else 1)
    print(LISMemo)
    print(max(LISMemo))

def main():
    LIS([5,6,2,3,4,1,9,9,8,9,5])
    # 5
    LIS([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15])
    # 6

if __name__ == "__main__":
    main()