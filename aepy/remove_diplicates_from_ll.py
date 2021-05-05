class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(n) time, O(1)space
def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	if linkedList is None:
		return linkedList
    node = linkedList
	while node: #is not None
		while node.next and node.value==node.next.value :
			node.next=node.next.next
		node = node.next
	return linkedList