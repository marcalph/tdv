def checkBST(root):
    res=[]
    if root is None:
        return True
    def helper(node,res):
        if node:
            if node.left:
                helper(node.left, res)
            res.append(node.data)
            if node.right:
                helper(node.right, res)
    helper(root, res)
    for i in range(len(res)-1):
        if res[i]>=res[i+1]:
            return False
    return True


# doesn't pass everything
def checkBST(root):
    res = []
    def helper(node,res):
        if node:
            if node.left:
                helper(node.left, res)
            res.append(node.data)
            print(res)
            if len(res)==2:
                if res[0]>=res[1]:
                    return False
                res.pop(0)
            
            if node.right:
                helper(node.right, res)
            return True
    return helper(root, res)