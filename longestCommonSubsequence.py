# X = 'ABCBDAB'
# Y = 'BDCABA'
# f(X,Y) = {BCBA,BDAB,BCAB}

import timeit

tLCSSeqMemo = {}
def topsDownLCSSeq(X,Y):
    if len(X) is 0 or len(Y) is 0:
        return 0
    if X+'#'+Y in tLCSSeqMemo.keys():
        return tLCSSeqMemo[X+'#'+Y]
    tLCSSeqMemo[X+'#'+Y] = 1 + topsDownLCSSeq(X[1:],Y[1:]) if X[0] == Y[0] else max(topsDownLCSSeq(X[1:],Y),topsDownLCSSeq(X,Y[1:]))
    return tLCSSeqMemo[X+'#'+Y]

def bottomsUpLCSSeq(X,Y):
    m,n = len(X),len(Y)
    bLCSSeqMemo = [[0 for x in range(m)] for y in range(n+2)]
    # print(bLCSSeqMemo)
    for i in range(1,m+1):
        for j in range(1,n+1):
            bLCSSeqMemo[i][j] = 1 + bLCSSeqMemo[i-1][j-1] if X[i-1] == Y[j-1] else bLCSSeqMemo[i-1][j-1]
            if (bLCSSeqMemo[i][j-1] > bLCSSeqMemo[i][j]):
                bLCSSeqMemo[i][j] = bLCSSeqMemo[i][j-1]  
            if (bLCSSeqMemo[i-1][j] > bLCSSeqMemo[i][j]):
                bLCSSeqMemo[i][j] = bLCSSeqMemo[i-1][j]
    return bLCSSeqMemo[m][n]

def main():
    print('Let\'s Code Longest Common Subsequence!')
    X = 'ABCBDAB'
    Y = 'BDCABA'
    print("Result: ",topsDownLCSSeq('ABCBDAB','BDCABA')," Time taken for 10000 iterations:˜",timeit.timeit('topsDownLCSSeq("ABCBDAB","BDCABA")', globals=globals(), number = 10000))
    print("Result: ",bottomsUpLCSSeq('ABCBDAB','BDCABA')," Time taken for 10000 iterations:˜",timeit.timeit('bottomsUpLCSSeq("ABCBDAB","BDCABA")', globals=globals(), number = 10000))
    # print(topsDownLCSSeq(X,Y))
    # print(bottomsUpLCSSeq(X,Y))

if __name__=='__main__':
    main()
