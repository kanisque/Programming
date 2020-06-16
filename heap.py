class heap:

	def __init__(self,capacity=3):
		self.capacity = capacity
		self.heap = [None] * capacity
		self.length = 0
	
	def getLeft(self,index):
		return None if index > capacity else self.heap[index*2+1]

	def getRight(self,index):
		return None if index > capacity else self.heap[index*2+2]

	def getParent(self,index):
		return None if index < 0 else self.heap[int((index-1)/2)]
	
	def insert(self,inputNumber):
		if self.length == self.capacity:
			self.heap.extend([None] * self.capacity)
			self.capacity += self.capacity
		self.heap[self.length] = inputNumber
		self.length += 1

		# self.heapify()
	
	def heapify(self):
		print("Heapifying")


	def printHeap(self):
		print(self.heap)


def main():
	a = heap()
	[a.insert(x) for x in range(0,7)]
	
# 				0
# 		1				2
#  3		4		5		6
	# print(a.getLeft(0))
	# print(a.getRight(0))
	# print(a.getParent(1))
	# print(a.getParent(2))
	# print(a.getLeft(1))
	# print(a.getRight(1))
	# print(a.getParent(3))
	# print(a.getParent(4))
	# print(a.getParent(5))
	# print(a.getParent(6))
	a.printHeap()

if __name__ == '__main__':
	main()