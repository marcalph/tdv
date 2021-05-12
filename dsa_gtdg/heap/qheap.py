from sys import stdin
from heapq import heappush, heappop

heap = []
item_lookup = set()

def push(v):
    heappush(heap, v)
    item_lookup.add(v)
    
def discard(v):
    item_lookup.discard(v)
    
def print_min():
    while heap[0] not in item_lookup:
        heappop(heap)
      
    print heap[0]
    
# cmds = {
#     1: push,
#     2: discard,
#     3: print_min
# }

# n = int(stdin.readline())
# for _ in range(n):
#     data = map(int,stdin.readline().split(" "))
#     cmds[data[0]](*data[1:])


#timelimit exceeded
class minHeap():
    def __init__(self):
        self.array = []
    
    def insert(self, val):
        self.array.append(val)
        self.heapify_upwards(len(self.array)-1)
        
    def heapify_upwards(self, index):
        while self.hasparent(index) and self.array[index]<self.array[self.parent(index)]:
            parent_index = self.parent(index)
            self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
            index = parent_index
    
    def hasparent(self, index):
        return self.parent(index)>=0
            
    def delete(self, val):
        for index, v in enumerate(self.array):
            if v == val:
                last =self.array.pop()
                if index<=len(self.array)-1:
                    self.array[index]=last
                    self.heapify_downwards(index)
                    break

    def heapify_downwards(self, index):
        while self.has_left(index):
            min_child_index = self.leftchild(index)
            if self.has_right(index) and self.array[self.rightchild(index)]< self.array[self.leftchild(index)]:
                min_child_index = self.rightchild(index)
                
            if self.array[min_child_index]>self.array[index]:
                break
            else:
                self.array[min_child_index], self.array[index] = self.array[index], self.array[min_child_index]
            index = min_child_index
                
                
    def has_left(self, index):
        return self.leftchild(index)<len(self.array)
    
    def has_right(self, index):
        return self.rightchild(index)<len(self.array)
      
    def leftchild(self, index):
        return 2*index+1
    
    def rightchild(self, index):
        return 2*index+2
    
    def parent(self, index):
        return (index-1)//2

    def getmin(self):
        return self.array[0]

        
MH = minHeap()
for _ in range(int(input())):
    query = input()
    if query[0]=="1":
        MH.insert(int(query.split()[1]))
    elif query[0]=="2":
        MH.delete(int(query.split()[1]))
    else:
        print(MH.getmin())