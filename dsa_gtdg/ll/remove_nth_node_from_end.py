# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# O(l) time, O(1) space
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
    
        for _ in range(n):
            fast = fast.next
        if fast is None: # the fast pointer has exhausted 
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head