
#O(v+e) O(v)
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]
		array.append(self.name)
		while queue:
			node = queue.pop(0)
			for child in node.children:
				queue.append(child)
				array.append(child.name)
		return array
