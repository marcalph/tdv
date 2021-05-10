#O(n)spacetime

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans=None
        
        def helper(node, p, q):
            if node is None:
                return False
            left = helper(node.left, p,q)
            right = helper(node.right, p, q)
            mid = node.val==p.val or node.val==q.val
                
            if left+right+mid>=2:
                self.ans=node
            return left or mid or right
        
        helper(root, p, q)
        return self.ans