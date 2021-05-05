
#O(n)spacetime
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        visited = []
        queue = [root,]
        if root is None:
            return []
        while queue:
            levelnodes = []
            for _ in range(len(queue)):
                node = queue.pop(0) 
                if node is not None:
                    levelnodes.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            visited.append(levelnodes)
        return visited