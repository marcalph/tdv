# O(n) spacetime
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(head):
            if head is None or head.next is None:
                return head

            first = head
            second = head.next

            first.next = helper(second.next)
            second.next = first
            return second
        return helper(head)
         