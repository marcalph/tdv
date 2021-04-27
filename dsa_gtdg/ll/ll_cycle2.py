# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# O(n)spacetime
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        viewed = set()
        slow=head
        while slow is not None:
            viewed.add(slow)
            slow = slow.next
            if slow in viewed:
                return slow
        return None

#O(n)time| O(1) space
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def intersect(head):
            slow=head
            fast=head
            while fast is not None and fast.next is not None:
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    return slow
            return None
        
        if head is None:
            return None
        
        intersection = intersect(head)
        if intersection is None:
            return None
        else:
            one = head
            two=intersection
            while one!=two:
                one = one.next
                two = two.next
            return one


