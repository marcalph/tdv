
def validate(array, sequence):
    j = 0
    for n in array:
        if n == sequence[j]:
            j+=1
        if j==len(sequence):
            return True
    return False
        