# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

#using a hashmap
# O(n+m) time| O(m) space
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        viewed = set()
        while headB != None:
            viewed.add(headB)
            headB = headB.next
        
        while headA != None:
            if headA in viewed:
                return headA
            headA = headA.next


#two pointer
# O(n+m) time | O(1)space
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        one = headA
        two = headB
        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one
