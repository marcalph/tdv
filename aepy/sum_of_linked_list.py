#O(max(m,n)) spacetime
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
	
	dummy = LinkedList(-1)
	prev = dummy
	carry = 0
	value = 0
	while  linkedListOne or linkedListTwo or carry:
		value += carry
		if linkedListOne:
			value += linkedListOne.value
			linkedListOne = linkedListOne.next
		
		if linkedListTwo:
			value += linkedListTwo.value
			linkedListTwo = linkedListTwo.next
			
		carry = value//10
		value = value%10
		
		prev.next = LinkedList(value)
		prev = prev.next
		value = 0
		
    return dummy.next