# need to discuss if sorted


class TwoSum:
    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        hm={}
        for n in self.nums:
            if value-n in hm:
                return True
            
            hm[n]=True
        