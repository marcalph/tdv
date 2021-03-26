""" insertion sort O(n²)
"""

def insertion_sort(array):
    for i in range(len(array)):
        j=i
        # ensure elements on left of i are sorted
        while array[j-1]>array[j] and j>0:
            array[j-1], array[j] = array[j], array[j-1]
            j-=1
            

array = [2, 3, 5, 7, 9, 11, 13, 6]
print(array)
insertion_sort(array)
print(array)