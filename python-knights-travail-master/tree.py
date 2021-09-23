class Node:
    def __init__(self,value):
        self._value = value
        self._children = []
        self._parent = None

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self,child):
        if child not in self._children:
            self._children.append(child)
            child.parent = self

    def remove_child(self,child):
        if child in self._children:
            self._children.remove(child)
            child.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self,newParent):
        if newParent is self._parent: return
        if self._parent is not None:
            self._parent.remove_child(self)
        self._parent = newParent
        if newParent is not None:
            newParent.add_child(self)



    def depth_search(self, value):
        if value == self.value:
            return self
        for currentNode in self.children:
           returnedNode = currentNode.depth_search(value)
           if returnedNode is not None:
               return returnedNode



    def breadth_search(self, value):
        nodes = [self]
        while len(nodes) != 0:
            currentNode = nodes.pop(0)
            if currentNode.value == value:
                return currentNode
            for child in currentNode.children:
               nodes.append(child)
        return None

# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)
