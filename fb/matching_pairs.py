from collections import defaultdict

def matchPairs(s1: str, s2: str) -> int:
    
    base = 0 # matched count
    matched = defaultdict(int) # matched char set
    mismatched = [] # mismatched indicies
    for i, (c1, c2) in enumerate(zip(s1,s2)):
        if c1 == c2: 
            base += 1
            matched[c1] += 1
        else: 
            mismatched.append(i)
    
    # if all matched and all chars are unique, any swap will result in -2
    if not mismatched and len(matched) == base:
        return base - 2

    # perfect swap for (c1, c2) if (c2, c1) is also a mismatch
    paired = set()
    for i in mismatched:
        if (s1[i], s2[i]) in paired:
            return base + 2
        paired.add((s2[i], s1[i]))

    # swapping at least one char into place
    seen = defaultdict(lambda: set())
    for i in mismatched: 
        seen[s2[i]].add(i)

    for i in mismatched:
        if s1[i] in seen and i not in seen[s1[i]]:
            return base +1
    
    # check if neutral swaps exists
    if len(mismatched) >= 2 or \
        any(s1[i] in matched for i in mismatched) or \
        any(count >= 2 for count in matched.values()):
        return base
    
    return base - 1