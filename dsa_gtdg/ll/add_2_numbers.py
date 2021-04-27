#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carrying = 0
        head = res = ListNode(0)
        
        while l1 or l2 or carrying:
            tmpl1 = l1.val if l1 else 0
            tmpl2 = l2.val if l2 else 0
            tmp = tmpl1+tmpl2+carrying  # do the actual sum
            carrying = tmp//10
            
            res.next=ListNode(tmp%10)
            res = res.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            
        return head.next