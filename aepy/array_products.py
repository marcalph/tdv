
#O(n) spacetime
def arrayOfProducts(array):
    # Write your code here.
	n = len(array)
	products= n*[1]
	
	
	lrp=1
	for i in range(n):
		products[i]=lrp
		lrp*=array[i]
	rrp=1	
	for i in reversed(range(n)):
		print(i)
		products[i]*=rrp
		rrp*=array[i]
	
	return products