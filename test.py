
def canBalance(nums):
    left, right = [], []
    for i in range(1, len(nums)+1):
        left.append(sum(nums[:i]))
        right.append(sum(nums[-i:]))
    print(left)
    print(right[::-1])
    for i in range(len(left)):
        if left[i]==right[::-1][-i]:
            return True
    return False


print(canBalance([2,1,1,2,1]))