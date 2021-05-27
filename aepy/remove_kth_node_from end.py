class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n), O(1)
# two pointers to remove kth node from end in ll
def removeKthNodeFromEnd(head, k):
    # Write your code here.
    fast = head
	slow = head
	# assume k is consistent with linked list size
	for _ in range(k):
		fast = fast.next
	if fast is None:
		head.value = head.next.value
		head.next = head.next.next
		return head
	while fast.next:
		fast = fast.next
		slow = slow.next
	
	# slow is now at (k-1)th from end
	slow.next = slow.next.next
	return head