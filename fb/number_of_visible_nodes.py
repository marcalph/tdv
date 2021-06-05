""" There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.
"""

ni = namedtuple("nodeinfo", "node, depth")

def visible_nodes(root):
  # obvious answer is just to compute the depth
  # but bfs seems more adequate to a follow up like returning the nodes
  # O(n), O(1)
  result = 0
  max_depth = float("-inf")
  nodeinfo = ni(root, 0)
  q = deque([nodeinfo])
  while q: # is not empty
    nodeinfo = q.popleft()
    node = nodeinfo.node
    depth = nodeinfo.depth
    if node.left and depth+1>max_depth:
      q.append(ni(node.left, depth+1))
    if node.right and depth+1>max_depth:
      q.append(ni(node.right, depth+1))
    if depth > max_depth:
      max_depth=depth
      result +=1
  return result