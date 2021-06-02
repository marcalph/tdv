#find stricly monotonic array
#O(n) time | O(1)space
def isMonotonic(array):
    nonDecreasing = 0
    nonIncreasing = 0
    for i in range(1, len(array)):
        if array[i]<array[i-1]:
            nonDecreasing+=1
        if array[i]>array[i-1]:
            nonIncreasing+=1
    return nonDecreasing==len(array)-1 or nonIncreasing==len(array)-1


def isMonotonic(array):
    if len(array)<=2:
        return True
    
    direction=array[1]-array[0]
    for i in range(2, len(array)):
        if direction ==0:
            direction = array[i] - array[i-1]
            continue
        if breaksDirection(direction, array[i-1], array[i]):
            return False
    
    return True

def breaksDirection(direction,  prev, curr):
    diff = curr-prev
    if direction>0:
        return diff<0
    return diff>0