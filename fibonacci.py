# Dynamic Programming for fibonacci
# n    0 1 2 3 4 5 6
# f(n) 0 1 1 2 3 5 8

#Bottoms up is iterative with subproblems solved before they are needed
#Can be solve without memoization as value of only last 2 is needed, hence can be kept in 2 variables i.e a,b and sum = a+b ; a = b; b = sum;
bFibMemo = [0,1]
def bottomsUpFibonacci(n):
    for i in range(2,n+1):
        bFibMemo.append(bFibMemo[i-1] + bFibMemo[i-2])
    return bFibMemo[n]

#Tops down is recursive with subproblems solved after they are called
#memoization is a must to prevent solving same subproblem multiple times
tFibMemo = {0:0,1:1}
def topsDownFibonacci(n):
    if n in tFibMemo.keys():
        return tFibMemo.get(n)
    tFibMemo[n] = topsDownFibonacci(n-1) +topsDownFibonacci(n-2)
    return tFibMemo.get(n)

def main():
    print('Let\'s Code Fibonacci')
    print(bottomsUpFibonacci(10))
    print(topsDownFibonacci(10))

if __name__ == '__main__':
    main()