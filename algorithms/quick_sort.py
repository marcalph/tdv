""" simple implementation of quick sort
"""

def partition(L, start, end):
    pivot = L[start]
    i=start+1
    j=end
    while True:
        # if value at i lower than pivot
        # it's in the right place (left side of pivot)
        # move right to next element
        while i<=j and L[i]<=pivot:
            i+=1
        while i<=j and L[j]>=pivot:
            j-=1
        if i<=j:
            L[i], L[j] = L[j], L[i]
        else:
            break
    # replace pivot
    L[j], L[start] = L[start], L[j]
    return j
    

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


arr = [4,5,3,6]
print(arr)
quick_sort(arr,0,3)
print(arr)
