
#O(n) spacetime
#compute product of whole array without division
# compute left products and right product in separate arrays
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