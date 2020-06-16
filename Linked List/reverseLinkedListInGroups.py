# Reverse a Linked List in groups of given size

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Linkedlist:
	def createLL(self,nums):
		head = None
		headTemp = None
		for i in range(len(nums)):
			if head == None:
				head = Node(nums[i])
				headTemp = head
			else:
				headTemp.next = Node(nums[i])
				headTemp = headTemp.next
		return head

	def printLL(self,head):
		while head:
			print(head.data, end=" ")
			head = head.next
		print("*END*")

	def reverseLinkedListInGroups(self,head,k):
		front = back = start = end = None
		curr = head
		sublist = 0
		while(curr):
			back = None
			start = curr
			count = 0
			while(curr and count < k):
				count += 1
				front = curr.next
				curr.next = back
				back = curr
				curr = front
			sublist += 1
			if sublist == 1:
				head = back
			else:
				end.next = back
			end = start
		return head


nums =[1,2,3,4,5,6,7,8]
k = 3
head = Linkedlist().createLL(nums)
Linkedlist().printLL(head)
head = Linkedlist().reverseLinkedListInGroups(head,k)
Linkedlist().printLL(head)