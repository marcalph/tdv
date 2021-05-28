# O(n^2), O(n)
# recursive sort of stack using only push and pop
def sortStack(stack):
    # Write your code here.
	
	def sort_helper(stack):
		# base case
		if len(stack)==0:
			return stack
		
		popped = stack.pop()
		sort_helper(stack)
		insert_helper(stack, popped)
		return stack
	
	
	def insert_helper(stack, to_insert):
		if len(stack)==0 or stack[-1]<=to_insert:
			stack.append(to_insert)
			return 
		
		popped = stack.pop()
		insert_helper(stack, to_insert)
		stack.append(popped)
	

	return sort_helper(stack)