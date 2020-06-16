# Given an integer k and a binary search tree, find the floor (less than or equal to) of k,
# and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root, k, floor=None, ceil=None):
    # Base Case 
    if root == None: 
        return -1
      
    # We found equal key 
    if root.value == k : 
        ceil = root.value
        floor = root.value  
      
    # If root's value is smaller, ceil must be in right subtree 
    elif root.value < k: 
        ceil = findCeilingFloor(root.right, k)
    else:
        floor = findCeilingFloor(root.left,k)
      
    # Else, either left subtre or root has the ceil value 
    val = findCeilingFloor(root.left, k) 
    ceil = val if val >= k else root.value  

    

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
# (4, 6)