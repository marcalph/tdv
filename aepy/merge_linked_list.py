#Merge sorted linked list inplace
# O(n+m), O(1)
# both

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    prev = None
	p1 = headOne
	p2 = headTwo
	while p1 is not None and p2 is not None:
		if p1.value<=p2.value:
			prev = p1
			p1 = p1.next
		else:
			if prev is not None:
				prev.next=p2
			prev=p2
			p2 = p2.next
			prev.next=p1
	if p1 is None:
		prev.next=p2
	return headOne if headOne.value<=headTwo.value else headTwo



def mergeLinkedLists(headOne, headTwo):
    # Write your code here
	prev = None
	p1 = headOne
	p2 = headTwo
	while p1 is not None and p2 is not None:
		if prev is None:
			if p1.value <= p2.value:
				prev=p1
				p1 = p1.next
			else:
				p1, p2 = p2, p1
				continue
		else:
			if p1.value<=p2.value:
				prev.next=p1
				p1=p1.next
				prev = prev.next
			else:
				p2, p1= p1, p2
				continue
	if p1 is None:
		prev.next=p2
	return headOne if headOne.value<= headTwo.value else headTwo
			
	
    