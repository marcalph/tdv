#O(n)time , O(h) space
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count=0
        if root is None: return 0
        self.helper(root)
        return self.count
        
    def helper(self, node):
        if node.left is None and node.right is None:
            self.count+=1
            return True
        
        is_uni=True
        
        if node.left:
            is_uni = self.helper(node.left ) and is_uni and node.left.val==node.val
        if node.right:
            is_uni = self.helper(node.right) and is_uni and node.right.val==node.val
        self.count +=is_uni
        return is_uni
        