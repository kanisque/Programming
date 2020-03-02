#longest palindromic substring

class Solution:
    # Bottoms Up  - Iterative
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        if slen < 2:
            return s
        mem = [[True if i == j else False for i in range(slen)] for j in range(slen)]
        globalmax = -1
        start, end = 0,0
        for checkLen in range(slen):
            i = 0
            j = i + checkLen
            while j < slen:
                if s[i] == s[j] and (checkLen < 2 or i+1 < slen and j > 0 and mem[i+1][j-1]):
                        mem[i][j] = True
                if mem[i][j] and j - i > globalmax:
                    globalmax = j - i
                    start,end = i,j+1
                i += 1
                j = i + checkLen
                
        return(s[start:end])

print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("ac"))
print(Solution().longestPalindrome("aa"))
print(Solution().longestPalindrome("banana"))
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))