# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyhead = ListNode(0)
        dummyhead.next = head
        
        prev, cur = dummyhead, head
        
        while cur is not None:
            if cur.val==val:
                prev.next=cur.next
            else:
                prev=cur
            cur = cur.next
        return dummyhead.next