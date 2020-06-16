class Node():
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self,value):
        self.root = Node(value)

    def printTree(self,type):
        if type == "pre":
            return str.strip(self.prePrint(self.root,""))
        elif type == "in":
            return str.strip(self.inPrint(self.root,""))
        elif type == "post":
            return str.strip(self.postPrint(self.root,""))

    def prePrint(self,root,preString):
        if root and root.data:
            preString += (str(root.data) + " ")
            preString = self.prePrint(root.left,preString)
            preString = self.prePrint(root.right,preString)
        return preString

    def inPrint(self,root,inString):
        if root and root.data:
            inString = self.inPrint(root.left,inString)
            inString += (str(root.data) + " ")
            inString = self.inPrint(root.right,inString)
        return inString
    
    def postPrint(self,root,postString):
        if root and root.data:
            postString = self.postPrint(root.left,postString)
            postString = self.postPrint(root.right,postString)
            postString += (str(root.data) + " ")
        return postString

tree = BinaryTree(5)
tree.root.left = Node(4)
tree.root.left.left = Node(2)
tree.root.left.right = Node(3)
tree.root.right = Node(6)
tree.root.right.left = Node(7)
tree.root.right.right = Node(8)

print(tree.printTree("pre"))
print(tree.printTree("in"))
print(tree.printTree("post"))