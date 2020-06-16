class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution (Better than recursive - Less memory & Same speed)
  def reverseIteratively(self, head):
    curr = head
    back = None 
    front = None
    while curr :
        front = curr.next
        curr.next = back
        back = curr
        curr = front
    return back

  # Recursive Solution      
  def reverseRecursively(self, head):
    if head is None or head.next is None:
        return head
    tempNode = self.reverseRecursively(head.next)
    head.next.next = head
    head.next = None
    return tempNode

# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
# testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4