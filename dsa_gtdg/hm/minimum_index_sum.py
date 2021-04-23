
# O (l1+l2) time | O(l1*x) space where x mean length of string
# beware of string comparisons! 

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hm1 = {v:i for i,v in enumerate(list1)} #common
        hm2 = {v:i for i,v in enumerate(list2)}
        penalty=10000
        for k,v in hm1.items():
            hm1[k]+=hm2.get(k,penalty)
        lis = min(hm1, key=hm1.get)
        return [k for k in hm1.keys() if hm1[k]==hm1[lis]]
        