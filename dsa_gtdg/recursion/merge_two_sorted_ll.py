#O(m+n) spacetime

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def helper(l1, l2):
            """ nh is the new head
            """
            # base case
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            # recurrence
            if l1.val<l2.val:
                l1.next = helper(l1.next, l2)
                return l1
            else:
                l2.next = helper(l1, l2.next)
                return l2
        return helper(l1,l2)