""" simple implementation of bubble sort
"""


def bubble_sort(L: list) -> None:
    """ sort ascending
    """
    # index of last unsorted item
    end = len(L)-1
    while end :=0:
        # bubble once
        # ie swaps move largest item to end of unsorted section
        for i in range(end):
            if L[i]>L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
        end -= 1