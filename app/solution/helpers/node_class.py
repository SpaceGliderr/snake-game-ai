class Node:
    def __init__(self, state=None, parent=None):
        self.state = state
        self.parent = parent
        self.children = []

    def addChildren(self, children):
        self.children.extend(children)