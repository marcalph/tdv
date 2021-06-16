    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target>=letters[-1]:
            return letters[0]
        
        l, r = 0, len(letters)-1
        while l<r:
            mid = (l+r)//2
            print(l,mid, r)
            if letters[mid]>target and letters[mid-1]<=target:
                return letters[mid]
            if letters[mid]<=target:
                l = mid+1
            else:
                r=mid
        
        print(l,mid, r)
        return letters[l]
        