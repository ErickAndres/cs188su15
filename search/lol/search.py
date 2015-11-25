# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    closed = set() #fringe keeps track of lst of unvisited nodes we are considering visiting
    fringe = util.Stack() #remember that push takes 2 args not 3 since the self is passed
    fringe.push((problem.getStartState(), [])) #the list will keep track of the successors
    while not fringe.isEmpty():
        node, path = fringe.pop() #print node print path
        if problem.isGoalState(node): #state, node
            return path #this is the lst of actions that reaches goal
        if node not in closed:
            closed.add(node)
            for child, action, child_cost in problem.getSuccessors(node): #need all 3 components since that is what getSuccessors works with
                fringe.push((child, path + [action]))                

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    closed = set() 
    fringe = util.Queue() 
    fringe.push((problem.getStartState(), [])) #the list will keep track of the successors
    while not fringe.isEmpty():
        node, path = fringe.pop() #print node print path
        if problem.isGoalState(node): #state, node
            return path #this is the lst of actions that reaches goal
        if node not in closed:#here I am fucking
            closed.add(node)
            for child, action, child_cost in problem.getSuccessors(node):
                fringe.push((child, path + [action]))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    closed = set()  
    fringe = util.PriorityQueue() 
    fringe.push((problem.getStartState(), []), 0) #the list will keep track of the successors
    while not fringe.isEmpty():
        node, path = fringe.pop() #print node print path, only returns item not priority value
        if problem.isGoalState(node): #state, node
            return path #this is the lst of actions that reaches goal
        if node not in closed:
            closed.add(node)
            for child, action, child_cost in problem.getSuccessors(node): # has 3 components
                fringe.push((child, path + [action]), problem.getCostOfActions(path + [action]))

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    closed = set() 
    fringe = util.PriorityQueue() 
    fringe.push((problem.getStartState(), []), 0) #the list will keep track of the successors
    while not fringe.isEmpty():
        node, path = fringe.pop() #print node print path, only returns item not priority value
        if problem.isGoalState(node): #state, node
            return path #this is the lst of actions that reaches goal
        if node not in closed:
            closed.add(node)
            currCost = problem.getCostOfActions(path)
            for child, action, child_cost in problem.getSuccessors(node): # has 3 components
                new_path = path + [action]  #ask why u add this part
                new_cost = currCost + child_cost + heuristic(child, problem) #why do you add heuristic?
                fringe.push((child, new_path), new_cost)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
