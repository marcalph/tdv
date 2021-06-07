# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

from dataclasses import dataclass

@dataclass
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size:int = 1000000
        self.d: list = [False for i in range(self.size)]

    def getHash(self, key: int) -> None:
        return hash(key)%self.size

    def add(self, key: int) -> None:
        self.d[self.getHash(key)] = True
        
    def contains(self, key: int) -> int:
        return self.d[self.getHash(key)]

    def remove(self, key: int) -> None:
        self.d[self.getHash(key)] = False



if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    obj.remove(2)
    print(obj.contains(5))
    print(obj)