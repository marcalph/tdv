

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
        node=head   
        if node is None or node.next is None:
            return node
        prev = self.reverseList(node.next)
        node.next.next=node
        node.next = None
        return prev