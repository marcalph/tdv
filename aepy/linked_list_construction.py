# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

	def setHead(self, node):
 		if self.head is None:
 			self.head = node
 			self.tail = node
 			return
 		self.insertBefore(self.head, node)
						  
 	# O(1) time | O(1) space
	def setTail(self, node):
 		if self.tail is None:
 			self.setHead(node)
 			return
 		self.insertAfter(self.tail, node)
		
	def insertBefore(self, node, nodeToInsert):
 		if nodeToInsert == self.head and nodeToInsert==self.tail:
 			return
 		self.remove(nodeToInsert)
 		nodeToInsert.prev = node.prev
 		nodeToInsert.next = node
 		if node.prev is None:
 			self.head = nodeToInsert
 		else:
 			node.prev.next = nodeToInsert
 		node.prev = nodeToInsert
			
			
 # O(1) time | O(1) space
	def insertAfter(self, node, nodeToInsert):
 		if nodeToInsert == self.head and nodeToInsert== self.tail:
 			return
 		self.remove(nodeToInsert)
 		nodeToInsert.prev = node
 		nodeToInsert.next = node.next
 		if node.next is None:
 			self.tail = nodeToInsert
 		else:
 			node.next.prev = nodeToInsert
 		node.next = nodeToInsert	


    #O(p)
    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
		if position == 1:
			self.setHead(nodeToInsert)
			return
		current = self.head
		current_pos = 1
		while current is not None and current_pos!=position:
			current = current.next
			current_pos+=1
		if current is not None:
			self.insertBefore(current, nodeToInsert)
        else:
			self.setTail(nodeToInsert)

    #O(n)
    def removeNodesWithValue(self, value):
        # Write your code here.
        current = self.head
		while current:
			nodetoremove = current
			current = current.next	
			if nodetoremove.value==value:
				self.remove(nodetoremove)
				
    def remove(self, node):
        # Write your code here.
        if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		self.removeNodeBindings(node)
	
	def removeNodeBindings(self, node):
		if node.prev is not None:
			node.prev.next=node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev=None
		node.next=None
		
	#O(n)
    def containsNodeWithValue(self, value):
        # Write your code here.
        current = self.head
		while current is not None and current.value != value:
			current = current.next
		return current is not None
				
				