

# A >> B >> C >> D >> None
# A << B << C << D 
# prev cur next

# O(n) time | O(1) space
def reverse(head):
    prev  = None
    cur  = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev # need to keep track of next node!!!
        prev = cur
        cur = nxt
        return prev

#recursive O(n) spacetime
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if node.next is None:
            return node
        newhead = self.reverseList(node.next)
        node.next.next=node
        node.next = None
        return newhead