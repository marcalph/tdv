
#recursive
#O(n)spacetime
def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        def helper(nodel, noder):
            if nodel is None and noder is None: return True
            if nodel is None or noder is None: return False
            
            return nodel.val==noder.val and helper(nodel.left, noder.right) and helper(nodel.right, noder.left)
        
        return helper(root, root)

#iterative




# iterative bst
# O(n) spacetime
def isSymmetric(self, root: TreeNode) -> bool:
    queue = [root,]
    if root is None:
        return True
    while queue:
        levelnodes = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node is not None:
                levelnodes.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                levelnodes.append(None)
            
        print(levelnodes)
        if levelnodes != levelnodes[::-1]:
            return False
    return True