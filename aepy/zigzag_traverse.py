
#O(n) 
#weird matrix traversal
def zigzagTraverse(array):
    # Write your code here.
	
	res = []
	i, j = 0, 0
	height, width = len(array)-1, len(array[0])-1
	go_down = True
	
	while is_valid(i,j, height, width):
		print(array[i][j])
		res.append(array[i][j])
		if go_down:
			if i==height or j==0:
				go_down=False
				if i==height:
					j+=1
				else:
					i+=1
			else:
				i+=1
				j-=1
		else: # go up
			if i==0 or j==width:
				go_down=True
				if j==width:
					i+=1
				else:
					j+=1
			else:
				j+=1
				i-=1
	return res

def is_valid(i, j, height, width):
	if 0<=i<=height and 0<=j<=width:
		return True
	return False