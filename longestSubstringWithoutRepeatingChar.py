# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s):

        if len(s) < 2:
            return(len(s))
        charMap = [None] * 100
        left ,right, globalMax = 0,0,0
        for i,char in enumerate(s):
            if charMap[ord(char) - ord('a')] != None :
                    left = max(left,charMap[ord(char) - ord('a')] + 1)
            right += 1
            charMap[ord(char)-ord('a')] = i
            globalMax = right - left if right - left > globalMax else globalMax
        return globalMax
        
print(Solution().lengthOfLongestSubstring(''))
print(Solution().lengthOfLongestSubstring(' '))
print(Solution().lengthOfLongestSubstring('abba'))
print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10