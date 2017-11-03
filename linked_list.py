#python test bench

class node():
	def __init__(self,var):
		self.data=var
		self.nextNode=None

def printList(head):
	while head is not None:
		print(head.data)
		head=head.nextNode

def addNode(head,var):
	if head is None:
		head=node(var)
		return head

	temp = head
	while temp.nextNode is not None:
		temp=temp.nextNode
	new = node(var)
	temp.nextNode=new
	return head

head=addNode(None,10)
head=addNode(head,20)
head=addNode(head,30)

printList(head)

