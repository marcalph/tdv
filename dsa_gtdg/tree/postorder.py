
def traverse(tree):
    viewed = []
    def helper(node, viewed):
        if node is None:
            return 
        
        if node.left:
            helper(node.left, viewed)
        if node.right:
            helper(node.right, viewed)
        viewed.append(node.val)
    
    helper(root, viewed)
    return viewed



def traverse(tree):
    stack = [tree]
    res = []
    while stack:
        node = stack.pop()
        
