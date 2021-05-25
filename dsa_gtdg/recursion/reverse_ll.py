#recursive O(n) spacetime
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if node.next is None:
            return node
        newhead = self.reverseList(node.next)
        node.next.next=node
        node.next = None
        return newhead