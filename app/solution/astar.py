class AStarNode:
    def __init__(self, state=None, parent=None, g=None, h=None, f=None):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = f
        self.children = []

    def addChildren(self, children):
        self.children.extend(children)

class AStar:
    def __init__(self, initial_state, goal_state, state_space=None, maze_size=None):
        self.initial_state = initial_state[0]
        self.snake_body = initial_state
        self.goal_state = self.prioritiseGoalStates(goal_state) # Can have multiple goal states
        self.state_space = self.initStateSpace(state_space, maze_size)


    def initStateSpace(self, state_space, maze_size):
        result = []
        if maze_size is not None:
            for i in range(0, maze_size[0]):
                for j in range(0, maze_size[1]):
                    result.append([i, j])
            return result
        return state_space


    def prioritiseGoalStates(self, goal_states):
        # Scuffed piece of code to prio states, please find an alternative
        distances = []
        for goal_state in goal_states:
            distances.append(self.calculateManhattanDistance(self.initial_state, goal_state))

        # Thank you Stack Overflow <3
        # https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
        prioritised = [dist for _, dist in sorted(zip(distances, goal_states))]
        print("PRIORITISED >>>>>>>> ", prioritised)

        return prioritised


    def calculateManhattanDistance(self, coord1, coord2):
        # We will use Manhattan Distance to calculate the h(n) value
        x1, y1 = coord1
        x2, y2 = coord2
        return abs(x1 - x2) + abs(y1 - y2)


    def getPotentialNeighbours(self, coord):
        up = [coord[0], coord[1] + 1]
        down = [coord[0], coord[1] - 1]
        left = [coord[0] - 1, coord[1]]
        right = [coord[0] + 1, coord[1]]

        return up, down, left, right


    def expandAndReturnChildren(self, node):
        # Will return neighbouring nodes
        children = []

        for coord in self.getPotentialNeighbours(node.state):
            # Removed this line: and coord not in self.snake_body first
            # Trying to find the first solution first before attempting the 2nd and 3rd questions
            if coord in self.state_space and coord not in self.snake_body:
                children.append(AStarNode(coord, node.state))

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


    def astar(self):
        frontier = []
        explored = []
        found_goal = False
        goalie = AStarNode()

        # Initial state g cost will be 0 since it's the start node
        # Takes the first goal node because it is the closest based on estimated cost
        initial_h = self.calculateManhattanDistance(self.initial_state, self.goal_state[0])
        frontier.append(AStarNode(self.initial_state, None, 0, initial_h, 0 + initial_h))

        # Where BFS begins
        while not found_goal:
            # Goal test before expansion
            if frontier[0].state == self.goal_state[0]:
                goalie = frontier[0]
                break

            # Check for empty list
            # if not self.goal_state:
            #     print("GOAL STATES >>>>> ", self.goal_state)
            #     break

            # Get the children paths of the first frontier element
            children = self.expandAndReturnChildren(frontier[0])
            frontier[0].addChildren(children)
            # Put the first element of the frontier to the explored array
            explored.append(frontier[0])

            temp_parent = frontier[0]
            # Delete first frontier as it is already explored
            del frontier[0]

            for child in children:
                # If the state in child is not in explored and
                # is not in any of the states in the Nodes of the frontier array
                # Meaning that it has not been explored at all
                if not (child.state in [e.state for e in explored]) and not (child.state in [f.state for f in frontier]):
                    # # Goal test
                    # if child.state in self.goal_state:
                    #     found_goal = True
                    #     # Goalie is the goal node
                    #     goalie = child

                    # Perform path calculations
                    child.g = temp_parent.g + 1
                    child.h = self.calculateManhattanDistance(child.state, self.goal_state[0])
                    child.f = child.g + child.h

                    # Append the child path to frontier for exploration
                    frontier.append(child)

            # Sort the frontier by the value of f
            frontier = sorted(frontier, key=lambda x: x.f)

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

        return self.recreateSolutionPath(solution)