
#O(n) time | O(1)space
def FirstNonRepeatingCharacter(string):
    charfreqs = {}
    for c in string:
        charfreqs[c] = charfreqs.get(c, 0) + 1
    
    for i in range(len(string)):
        curchar = string[i]
        if charfreqs[curchar]==1:
            return i
    return -1