from solution.helpers.node_class import Node

class BFS:
    def __init__(self, initial_state, goal_state, state_space=None, maze_size=None):
        self.initial_state = initial_state[0]
        self.snake_body = initial_state
        self.goal_state = goal_state # Can have multiple goal states
        self.state_space = self.initStateSpace(state_space, maze_size)
        self.number_of_nodes = 0
        self.number_of_expansions = 0
        self.actions = 'nswe'


    def initStateSpace(self, state_space, maze_size):
        result = []
        if maze_size is not None:
            for i in range(0, maze_size[0]):
                for j in range(0, maze_size[1]):
                    result.append([i, j])
            return result
        return state_space


    def getPotentialNeighbours(self, coord):
        up = [coord[0], coord[1] - 1]
        down = [coord[0], coord[1] + 1]
        left = [coord[0] - 1, coord[1]]
        right = [coord[0] + 1, coord[1]]

        return up, down, left, right


    def expandAndReturnChildren(self, node):
        # Add expansion sequence
        self.number_of_expansions += 1
        node.expansion_sequence = self.number_of_expansions

        # Will return neighbouring nodes
        children = []

        for idx, coord in enumerate(self.getPotentialNeighbours(node.state)):
            if coord in self.state_space and coord not in self.snake_body:
                self.number_of_nodes += 1
                children.append(Node(self.number_of_nodes, -1, coord, node.state, False))
                node.addAction(self.actions[idx])
            # else:
            #     # -1 because it is not expanded on, therefore don't need expansion sequence
            #     children.append(Node(self.number_of_nodes, -1, coord, node.state, True))

        # Filter to return children that are False (not removed path)
        return children


    def recreateSolutionPath(self, solution):
        solution_actions = []
        for idx, coord in enumerate(solution):
            if idx != len(solution) - 1:
                resultant_coord = [solution[idx + 1][0] - coord[0], solution[idx + 1][1] - coord[1]]
                if resultant_coord == [0, 1]:
                    solution_actions.append('s')
                elif resultant_coord == [0, -1]:
                    solution_actions.append('n')
                elif resultant_coord == [-1, 0]:
                    solution_actions.append('w')
                elif resultant_coord == [1, 0]:
                    solution_actions.append('e')

        return solution_actions


    def getParentId(self, parent_state, explored):
        for e in explored:
            if e.state == parent_state:
                return e.id
        return None


    def returnSearchTree(self, explored):
        search_tree = []

        # Recreate search tree
        for e in explored:
            # print("EXPLORED >>>> ", ','.join(str(v) for v in e.state))
            tree_node = {
                "id": e.id,
                "state": ','.join(str(v) for v in e.state),
                "expansionsequence": e.expansion_sequence,
                "children": [child.id for child in e.children],
                "actions": e.actions,
                "removed": e.removed,
                "parent": self.getParentId(e.parent, explored) # search for parent ID
            }

            search_tree.append(tree_node)

        return search_tree


    def bfs(self):
        frontier = []
        explored = []
        removed = []
        found_goal = False
        goalie = Node()

        self.number_of_nodes += 1

        # `frontier` variable needs to append Node class
        # This is because the frontier will be storing an array of yet to visit Node states
        frontier.append(Node(self.number_of_nodes, self.number_of_expansions, self.initial_state, None, False))

        # Where BFS begins
        while not found_goal:
            # Get the children paths of the first frontier element
            children = self.expandAndReturnChildren(frontier[0])
            frontier[0].addChildren(children)
            # Put the first element of the frontier to the explored array
            explored.append(frontier[0])
            # Delete first frontier as it is already explored
            del frontier[0]

            for child in children:
                # If the state in child is not in explored and
                # is not in any of the states in the Nodes of the frontier array
                # Meaning that it has not been explored at all
                if not (child.state in [e.state for e in explored]) and not (child.state in [f.state for f in frontier]):
                    # Goal test
                    if child.state in self.goal_state:
                        found_goal = True
                        # Goalie is the goal node
                        goalie = child
                    # Append the child path to frontier for exploration
                    frontier.append(child)
                else:
                    child.removed = True
                    removed.append(child)

            print("Explored: ", [e.state for e in explored])
            print("Frontier: ", [f.state for f in frontier])
            print("Children: ", [c.state for c in children])

        solution = [goalie.state]
        # Loop through to find the entire solution path
        while goalie.parent is not None:
            # Insert the parent before the child in the array
            solution.insert(0, goalie.parent)
            for e in explored:
                # To get the parent's parent
                if e.state == goalie.parent:
                    # Next goal node will be the e node to get the parent of the goal node's parent
                    goalie = e
                    break

        print("SOLUTION >>>>> ", solution)
        print("ACTIONS >>>>> ", self.recreateSolutionPath(solution))
        print("SEARCH TREE >>>>> ", self.returnSearchTree(explored + frontier + removed))

        return self.recreateSolutionPath(solution), self.returnSearchTree(explored + frontier + removed)