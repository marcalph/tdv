class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.cereal = []
        def helper(node):
            if node is None:
                self.cereal.append(None)
            else:
                self.cereal.append(node.val)
                helper(node.left)
                helper(node.right)
        
        helper(root)
        return self.cereal
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        print(data)
        def helper(data):
            if data is None:
                return None
            
            if data[0] is None:
                data.pop(0)
                return None
            
            root = TreeNode(data[0])
            data.pop(0)
            root.left = helper(data)
            root.right = helper(data)
            return root   
        return helper(data)