class Solution:
  def isValid(self, s):
    stack = []
    pairOf = {"(" : ")","[" : "]","{" : "}"}
    for i in s:
        if i in "({[":
            stack.append(i)
        else:
            if len(stack) is 0 or i != pairOf[stack.pop()]:
                return False
    if len(stack) is 0:
        return True
    return False

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))