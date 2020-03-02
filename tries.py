charCount = 26

#Tries data structure
class Node():
    def __init__(self,char,value = None):
        self.char = char
        self.value = value
        self.pointerArr = [None]* charCount

    # To add one char with some value at certain node
    def insertChar(self,charVal,data):
        if self.pointerArr[ord(charVal)%65] == None:
            self.pointerArr[ord(charVal)%65] = Node(charVal,data)
        else:
            self.pointerArr[ord(charVal)%65].value += data

class Trie():
    def __init__(self):
        self.root = Node("*")
    
    def insertWord(self,word):
        currNode = self.root
        value = 0
        for i,char in enumerate(word):
            if i == len(word)-1:
                value = 1
            upperChar = str.upper(char)
            currNode.insertChar(upperChar,value)
            currNode = currNode.pointerArr[ord(upperChar)%65]
    
    def printTrie(self, currNode = None):
        if currNode is None:
            currNode = self.root
        for node in currNode.pointerArr:
            if node is not None:
                print(node.char,node.value)
                self.printTrie(node)
    
    def findWord(self,word):
        currNode = self.root
        for char in word:
            if currNode is None:
                return False
            upperChar = str.upper(char)
            currNode = currNode.pointerArr[ord(upperChar)%65]
        return currNode.value if currNode.value else False

trie = Trie()
trie.insertWord("app")
trie.insertWord("app")
trie.insertWord("apple")
trie.insertWord("applefizz")

trie.printTrie()

print(trie.findWord("ap"))
print(trie.findWord("app"))
print(trie.findWord("applefi"))
print(trie.findWord("applefizz"))
print(trie.findWord("boy"))
