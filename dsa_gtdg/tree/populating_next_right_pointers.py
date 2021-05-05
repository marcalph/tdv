#O(n) spacetime
def connect(self, root: 'Node') -> 'Node':
        queue = [root,]
        while queue:
            sz = len(queue)
            for i in range(sz):
                node = queue.pop(0)
                if node is not None:
                    if i < sz - 1:
                        node.next = queue[0]
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return root

#O(n) time | O(1)
class Solution:
    def connect(self, root):
        toprow = root
        while toprow:
            start = cur = Node()
            top = toprow
            while top:
                for child in [top.left, top.right]:
                    cur.next = child
                    if cur.next: cur = cur.next
                top = top.next
            toprow = start.next
        return root