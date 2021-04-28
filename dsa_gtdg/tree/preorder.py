


# o(n) spacetime
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stack, viewed = [root,], []
        
        while stack:
            node = stack.pop()
            if node is not None:
                viewed.append(node.val)
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)
            
        return viewed


import collections
def inorder(root):
    res = []
    stack = collections.deque()
    node = root
    while node is not None or stack: #is not empty
        if node is not None:
            stack.append(node)
            res.append(node.val)
            node = node.left
        else:
            node = stack.pop()
            node = node.right
    return res