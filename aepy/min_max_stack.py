# 0(1) spacetime for all stack ops
# using another stack to store stat info
class MinMaxStack:
	def __init__(self):
		self.value_stack = []
		self.info_stack = []
		

    def peek(self):
        # Write your code here.
        return self.value_stack[-1]

    def pop(self):
        # Write your code here.
		self.info_stack.pop()
        return self.value_stack.pop()

    def push(self, number):
        # Write your code here.
		info = {"min": number,"max":number}
		if len(self.value_stack):
			last = self.info_stack[-1]
			info["min"] = min(last["min"], number)
			info["max"] = max(last["max"], number)
		self.info_stack.append(info)
		self.value_stack.append(number)
		
    def getMin(self):
        # Write your code here.
		return self.info_stack[-1]["min"]
        

    def getMax(self):
        # Write your code here.
        return self.info_stack[-1]["max"]