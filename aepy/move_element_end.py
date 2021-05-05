def moveElementToEnd(array, toMove):
    # Write your code here.
	left = 0
	for i in range(len(array)):
		if array[i]!=toMove:
			array[left], array[i] = array[i], array[left]
			left+=1
    return array