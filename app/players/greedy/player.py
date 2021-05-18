from .greedy import Greedy

class Player():
  name = "Greedy Best First Search"
  group = "Jimmy Neurons"
  members = [
    ["Nicholas Lee Choon Sin", "18073957"],
    ["Cheong Keng Son", "18074229"],
    ["Adrian Ching Liansheng", "18063685"],
    ["Ng Wei Jinn", "18064154"]
  ]

  informed = True

  def __init__(self, setup):
    self.setup = setup
    self.steps_taken = 0
    self.nodes_expanded = 0
    self.rounds = 0

  def run(self, problem):
    print("SETUP >>>> ", self.setup)
    print("PROBLEM >>>> ", problem)
    print("STEPS >>>> ", self.steps_taken)
    print("NODES_EXPANDED >>>> ", self.nodes_expanded)
    print("ROUNDS >>>> ", self.rounds)

    try:
      # Informed Search Solution - A Star Pathfinding
      greedy = Greedy(problem['snake_locations'], problem['food_locations'], self.setup['maze_size'])
      solution, search_tree, expansions = greedy.greedy()

    except IndexError:
      # Catch Index out of Bounds problem
      # Means that the solution can't be found, and all possible coordinates are explored already
      # Take the tail as the new goal state to ensure that the snake continues moving / will potentially find a path to the food
      problem['food_locations'].append(problem['snake_locations'][-1])
      k_value = int(len(problem['snake_locations']) / 4)
      # del problem['snake_locations'][-1]
      res = problem['snake_locations'][: len(problem['snake_locations']) - k_value]
      print("RESULT >>>> ", res)

      # Informed Search Solution - A Star Pathfinding
      greedy = Greedy(res, problem['food_locations'], self.setup['maze_size'])
      solution, search_tree, expansions = greedy.greedy()

    self.steps_taken += len(solution)
    self.nodes_expanded += expansions
    self.rounds += 1

    return solution, search_tree


if __name__ == "__main__":
  p1 = Player({ "maze_size": [10,10], "static_snake_length": True })
  sol, st = p1.run({'snake_locations': [[0, 5]], 'current_direction': 'e', 'food_locations': [[6, 7]]})
  print("Solution is:", sol)
  print("Search tree is:")
  print(st)