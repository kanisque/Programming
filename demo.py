# sentences = ["asd fad cde asds","adf abc bcd asd","asdf s","abv","as dfas","Abc abc","abc bcd asdf a"]
# words = ["abc","bcd","cde"]

# dict ={ word:0 for word in words }
# for sentence in sentences:
#     for word in words:
#         if word in list(map(str.lower,sentence.split())):
#             dict[word] += 1

# sortedDict = {key:value for key,value in sorted(dict.items(), key = lambda x:(-x[1],x[0]))}
# print(list(sortedDict.items())[0:3])
# print(" ".join(list(sortedDict.keys())[0:3]))
# n = int(00000000000000000000000000001011)
for i in zip([1,2],[1,2,3]):
    print(i)