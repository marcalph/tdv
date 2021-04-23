class MyHashMap:
    def __init__(self):
        self.d = [-1 for i in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.d[self.getHash(key)] = value
    
    def get(self, key: int) -> int:
        return self.d[self.getHash(key)]

    def remove(self, key: int) -> None:
        self.d[self.getHash(key)] = -1

    def getHash(self, key: int) -> None:
        return hash(key)%1000000


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)