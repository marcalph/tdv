
#O(h) time O(1)
def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    if root is None:
        return
    node=root
    while node:
        if node.val==val:
            return node
        else:
            if node.val<val:
                node = node.right
            else:
                node = node.left
    return node


# O(h) spacetime
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val) 
        else:
            return self.searchBST(root.right, val)