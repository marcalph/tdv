#O(n) spacetime
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        queue = [root,]
        
        def helper(queue, depth):
            while queue:
                depth+=1
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    if node is None:
                        return 0
                    if node.left:
                        queue.append(node.left)
                    if node .right:
                        queue.append(node.right)
            return depth
        return helper(queue,0)

#O(n) O(h)
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