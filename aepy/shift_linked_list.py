# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    # Write your code here.
	if k == 0:
		return head
	else:
		tail, length = get_tail(head)
		k = k%length
		if k ==0:
			return head
		return shift(head, tail, k, length)

		

def shift(head, tail, k, length):
	new_tail = head	
	for _ in range(length-k-1):
		new_tail = new_tail.next 

	new_head = new_tail.next
	new_tail.next = None
	tail.next = head
	return new_head


def get_tail(head):
	cur = head
	length = 1
	while cur.next:
		cur = cur.next
		length += 1
	return cur, length