#O(n)| O(1)
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not array:
        return 0
    if len(array)==1:
        return array[0]
    im2 = array[0]
    im1 = max(array[1],im2)
    if len(array)==2:
        return im1
	maxsum =0
    for i in range(2, len(array)):
        maxsum=max(im2+array[i], im1)
        im2=im1
		im1=maxsum

    return maxsum 