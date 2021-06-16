def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        if num<2:
            return True
        while l<r:
            mid = (l+r)//2
            print(mid)
            if mid**2==num:
                return True
            elif mid**2<num:
                l = mid+1
            else:
                r = mid
        return False
        