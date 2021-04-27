
# Given the head of a singly linked list, return true if it is a palindrome

# O(n)spacetime
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        prev, cur = None, head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]

# recursively O(n)spacteime
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.left_pnter = head
        
        def recursive_check(curnode):
            if curnode is not None:
                if not recursive_check(curnode.next):
                    return False
                if self.left_pnter.val != curnode.val:
                    return False
                self.left_pnter = self.left_pnter.next
            return True
        
        return recursive_check(head)



# O(n) time | O(1) space
 class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # get half
        def half(head):
            """ locate middle of linked list (ll)
            """
            slow = fast = head
            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
    
        # reverse half
        def reverse(node):
            """ reverse ll
            """
            prev, cur = None, node
            while cur is not None:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        # check "palindromeness"/ "palindromity"
        result=True
        middle = half(head)
        rightend_head = reverse(middle.next)
        
        firstpos = head
        secondpos = rightend_head
        # enjoy/cry
        while result and secondpos is not None:
            if firstpos.val != secondpos.val:
                    result=False
            firstpos = firstpos.next
            secondpos = secondpos.next
            
        return result



