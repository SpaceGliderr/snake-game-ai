import random
from solution.bfs import BFS
from solution.astar import AStar

class Player():
  name = "testing player"
  group = "Children of Odin"
  members = [
    ["Thor", "12834823"],
    ["Loki", "98854678"],
    ["Hela", "87654654"]
  ]

  # True for A Star, False for Breadth First Search
  informed = False

  def __init__(self, setup):
    self.setup = setup

  def run(self, problem):
    print("SETUP >>>> ", self.setup)
    print("PROBLEM >>>> ", problem)

    # Uninformed Search Solution - Breadth First Search
    bfs = BFS(problem['snake_locations'], problem['food_locations'], maze_size=self.setup['maze_size'])
    solution = bfs.bfs()

    # Informed Search Solution - A Star Pathfinding
    # astar = AStar(problem['snake_locations'], problem['food_locations'], maze_size=self.setup['maze_size'])
    # solution = astar.astar()

    # Array of actions (unused, not going to remove just yet)
    # directions = "nswe"

    # Generates search tree
    search_tree = [
      {
        "id": 1,
        "state": "0,0",
        "expansionsequence": 1,
        "children": [2,3,4],
        "actions": ["n","w","e"],
        "removed": False,
        "parent": None
      },
      {
        "id": 2,
        "state": "5,0",
        "expansionsequence": 2,
        "children": [5,6,7],
        "actions": ["n","s","w"],
        "removed": False,
        "parent": 1
      },
      {
        "id": 3,
        "state": "0,3",
        "expansionsequence": -1,
        "children": [],
        "actions": [],
        "removed": False,
        "parent": 1
      },
      {
        "id": 4,
        "state": "0,4",
        "expansionsequence": -1,
        "children": [],
        "actions": [],
        "removed": False,
        "parent": 1
      },
      {
        "id": 5,
        "state": "5,0",
        "expansionsequence": -1,
        "children": [],
        "actions": [],
        "removed": True,
        "parent": 2
      },
      {
        "id": 6,
        "state": "5,3",
        "expansionsequence": -1,
        "children": [],
        "actions": [],
        "removed": False,
        "parent": 2
      },
      {
        "id": 7,
        "state": "1,0",
        "expansionsequence": -1,
        "children": [],
        "actions": [],
        "removed": False,
        "parent": 2
      }
    ]
    # this function should return the solution and the search_tree
    return solution, search_tree