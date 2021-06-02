#O(n^2) spacetime
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
	if len(arrayOne)!= len(arrayTwo):
		return False
	
	if len(arrayOne)==0 and len(arrayTwo)==0:
		return True

	if arrayOne[0]!= arrayTwo[0]:
		return False

	leftsub1 = get_strictly_smaller(arrayOne)
	leftsub2 = get_strictly_smaller(arrayTwo)
	rightsub1 = get_bigger(arrayOne)
	rightsub2 = get_bigger(arrayTwo)
	
	return sameBsts(leftsub1, leftsub2) and sameBsts(rightsub1, rightsub2)


def get_strictly_smaller(array):
	res = []
	compare_value = array[0]
	for i in range(1,len(array)):
		if array[i]<compare_value:
			res.append(array[i])
	return res

def get_bigger(array):
	res = []
	compare_value = array[0]
	for i in range(1, len(array)):
		if array[i]>=compare_value:
			res.append(array[i])
	return res

