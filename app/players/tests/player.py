import random
# from solution.bfs import BFS
# from solution.astar import AStar
from solution.bfs_improved import BFS
from solution.greedy import Greedy

class Player():
  name = "testing player"
  group = "Children of Odin"
  members = [
    ["Thor", "12834823"],
    ["Loki", "98854678"],
    ["Hela", "87654654"]
  ]

  # True for Greedy, False for Breadth First Search
  informed = False

  def __init__(self, setup):
    self.setup = setup

  def run(self, problem):
    print("SETUP >>>> ", self.setup)
    print("PROBLEM >>>> ", problem)

    try:
      # Uninformed Search Solution - Breadth First Search
      # bfs = BFS(problem['snake_locations'], problem['food_locations'], self.setup['maze_size'])
      # solution, search_tree = bfs.bfs()

      # Informed Search Solution - A Star Pathfinding
      greedy = Greedy(problem['snake_locations'], problem['food_locations'], self.setup['maze_size'])
      solution, search_tree = greedy.greedy()
    except IndexError:
      # Catch Index out of Bounds problem
      # Means that the solution can't be found, and all possible coordinates are explored already
      # Take the tail as the new goal state to ensure that the snake continues moving / will potentially find a path to the food
      problem['food_locations'].append(problem['snake_locations'][-1])
      del problem['snake_locations'][-1]

      # Uninformed Search Solution - Breadth First Search
      # bfs = BFS(problem['snake_locations'], problem['food_locations'], self.setup['maze_size'])
      # solution, search_tree = bfs.bfs()

      # Informed Search Solution - A Star Pathfinding
      greedy = Greedy(problem['snake_locations'], problem['food_locations'], self.setup['maze_size'])
      solution, search_tree = greedy.greedy()

    return solution, search_tree