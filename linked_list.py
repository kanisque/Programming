#python test bench

class node():
	def __init__(self,var):
		self.data=var
		self.nextNode=None
	
	def addNode(self,newVal=-1):
		self.lastNode().nextNode = node(newVal)

	def deleteNode(self,deleteVal):
		head = self
		if self.data == deleteVal:
			self = self.nextNode
		while head.nextNode is not None:
			if head.nextNode.data == deleteVal:
				head.nextNode = head.nextNode.nextNode
				break
			head = head.nextNode
		return self

	def length(self):
		count = 0
		while self is not None:
			count+=1
			self = self.nextNode
		return(count)

	def findNode(self,findVal):
		count = 1
		while self is not None:
			if(self.data == findVal):
				return(count)	
			self = self.nextNode
			count+=1
		return(None)
	
	def lastNode(self):
		head = self
		while head.nextNode is not None:
			head = head.nextNode
		return head
	
	def addNodeAfter(self,position,newVal):
		head = self
		newNode = node(newVal)
		if(position == 0):
			newNode.nextNode = self
			return newNode
		while position>1:
			head = head.nextNode
			position-=1
		
		newNode.nextNode = head.nextNode
		head.nextNode = newNode
		return self
	def printList(self,name="HEAD"):
		head = self
		print(name,": ",end="")
		while head is not None:
			print(head.data,end=" ---> ")
			head=head.nextNode
		print("END")

def main():
	print("--- Running ---")
	firstLList = node(10)
	for i in range(20,110,10):
		firstLList.addNode(i)

	print("Finding element 40:",firstLList.findNode(40))
	print("Finding element 150:",firstLList.findNode(150))
	print("Length",firstLList.length())
	firstLList.printList(name="Original")
	firstLList = firstLList.addNodeAfter( firstLList.findNode(20) ,"Unexpected")
	firstLList.printList(name="addNodeAfter 20")
	firstLList = firstLList.deleteNode(20)
	firstLList.printList(name="deleteNode 20")


	print("Length",firstLList.length())
	'''
	# CAUTION: creates a looping linked list 
	temp = firstLList.lastNode()
	print("temp.data = ",temp.data)
	temp.nextNode = firstLList.nextNode 
	'''

	# secondLList = node(20)
	# for i in range(40,220,20):
	# 	secondLList.addNode(i)

	# secondLList.printList(name="List 2")
if __name__ == "__main__":
	main()
 