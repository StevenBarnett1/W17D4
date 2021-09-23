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
            child._parent = self

    def remove_child(self,child):
        if child in self._children:
            self._children.remove(child)
            child._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self,newParent):
        if newParent is not None:
            self._parent = newParent
            newParent.add_child(self)
