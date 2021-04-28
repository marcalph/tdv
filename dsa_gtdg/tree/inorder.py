class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def rec_trav(node, res):
            if node is not None:
                if node.left is not None:
                    rec_trav(node.left, res)
                res.append(node.val)
                if node.right is not None:
                    rec_trav(node.right, res)
            return res
        return rec_trav(root, res)

import collections
def inorder(root):
    res = []
    stack = collections.deque()
    node = root
    while node is not None or stack: #is not empty
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            res.append(node.val)
            node = node.right
    return res