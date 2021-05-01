class BFSNode:
    def __init__(self, id=None, expansion_sequence=None, state=None, parent=None, removed=False):
        self.id = id
        self.expansion_sequence = expansion_sequence
        self.state = state
        self.parent = parent
        self.removed = removed
        self.children = []
        self.actions = []

    def addChildren(self, children):
        self.children.extend(children)

    def addAction(self, action):
        self.actions.append(action)


class GreedyNode:
    def __init__(self, id=None, expansion_sequence=None, state=None, parent=None, g=None, h=None, f=None, removed=False):
        self.id = id
        self.expansion_sequence = expansion_sequence
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = f
        self.removed = removed
        self.children = []
        self.actions = []

    def addChildren(self, children):
        self.children.extend(children)

    def addAction(self, action):
        self.actions.append(action)
