# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
	if not head.next:
		return head
	
	prev= None
	cur=head
	while cur is not None:
		nxt = cur.next
		cur.next=prev
		prev=cur
		cur=nxt
	return prev