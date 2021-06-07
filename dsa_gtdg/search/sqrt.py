# comptue floor of sqrt(x)
# without using pow or **
def mySqrt(self, x: int) -> int:
    l, r = 0, x//2
    if x<2:
        return x
    
    while l<=r:
        mid = (l+r)//2
        if mid*mid==x:
            return mid
        elif mid*mid>x:
            r = mid-1
        else:
            l = mid+1
    return r