#longest increasing subsequence
#  input   = 5 6 2 3 4 1 9 9 8 9 5
# f(input) = 5 ( 2 3 4 8 9 )

LISMemo = []
def LIS(input):
    LISMemo = [ 1 for x in range(len(input))]
    
    for i in range(1,len(input)):
        for j in range(i):
            LISMemo[i] = max(LISMemo[i], LISMemo[j]+1 if input[i]>input[j] else 1)
    print(max(LISMemo))

def main():
    LIS([5,6,2,3,4,1,9,9,8,9,5])

if __name__ == "__main__":
    main()