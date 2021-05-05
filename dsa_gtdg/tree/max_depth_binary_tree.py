
# top down
def maxDepth(self, root: TreeNode) -> int:
        self.ans=0
        def helper(node, depth):
            if node.left is None and node.right is None:
                self.ans = max(self.ans, depth+1)
                return self.ans
            if node.left:
                helper(node.left, depth+1)
            if node.right:
                helper(node.right, depth+1)
        if root is None:
            return 0
        helper(root,0)
        return self.ans

#bottom up
def maxDepth(self, root: TreeNode) -> int:
        def helper(node):
            left=right=0
            if node.left:
                left = helper(node.left)
            if node.right:
                right = helper(node.right)
            return max(left, right)+1
        if root is None:
            return 0
        ans = helper(root)
        return ans