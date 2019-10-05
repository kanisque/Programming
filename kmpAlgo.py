#kmp algo is for exact string pattern matching
# eg
# 
# pattern  =>    ababaca
# prefixArray => 0012301

def prefixFunc(pattern):
    prefixArray = [0] * len(pattern)
    prefixCounter = 0
    prefixPointer = 1
    for index,char in enumerate(pattern):
        if pattern[index] == pattern[prefixPointer]:
            prefixArray[index] = prefixCounter + 1
            prefixCounter += 1
            prefixPointer += 1
        else:
            prefixCounter = 0
            prefixPointer = 0
        if prefixPointer == len(pattern):
            break
    return prefixArray

# print(prefixFunc('ababaca'))
# print(prefixFunc('abababa'))
# print(prefixFunc('aaaaaaa'))

def kmpMatching(text,pattern):
    index = 0
    pointer = 0
    prefixArray = prefixFunc(pattern)
    # print(prefixArray)
    while index < len(text):
        if pointer == len(pattern):
            break
        if text[index] == pattern[pointer]:
            pointer += 1
            index += 1
        elif pointer > 0:
            pointer = prefixArray[pointer-1]
        else:
            pointer = 0
            index += 1
    if pointer == len(pattern):
        return index - len(pattern)
    else:
        return -1
        
print(kmpMatching('cdabab','abab'))
print(kmpMatching('cdabab','ababc'))
print(kmpMatching('bacbabababacaca','ababaca'))