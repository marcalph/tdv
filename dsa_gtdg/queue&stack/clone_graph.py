# O(v+e) time O(v) space
class Solution:
    def __init__(self):
        self.viewed = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        if node not in self.viewed:
            new = Node(node.val,[])
            self.viewed[node] = new
            if node.neighbors:
                new.neighbors = [self.cloneGraph(nei) for nei in node.neighbors]
        
            return new
        else:
            return self.viewed[node]