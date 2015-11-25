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
    #added
    Output
    Start: A
    Is the start a goal? False
    Start's successors: [('B', '0:A->B', 1.0), ('C', '1:A->C', 2.0), ('D', '2:A->D', 4.0)]
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    stack = util.Stack() # creates empty lst at top, this is the fringe represented (state curState, list lstMoves, int cost)
    #print stack.pop()
    start = problem.getStartState()
    stack.push((start, [])) # note item represented as coordinates direction value, is it just the start coordinates followed by the rest of the lst of items
    #print stack.pop()
    closed = set() #node seems to carry both the "state" information, and the list of directions it takes to get to that particular node
    while not stack.isEmpty():
        node, path = stack.pop() # node is the first element & path is the actions or nodes visited to obtain our answer
        if problem.isGoalState(node): #is this right
           return path #path of nodes
        if node not in closed:
            closed.add(node) #state
            for child, action, child_cost in problem.getSuccessors(node): #what is the fringe
                stack.push((child, path + [action]))
                #print stack.pop()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    start = problem.getStartState()
    queue.push((start, [])) #why empty lst
    closed = set()
    while not queue.isEmpty():
        node, path = queue.pop()
        if problem.isGoalState(node):
            return path
        if node not in closed: #node is state[node], so path is the actual value
            closed.add(node)
            for child, action, child_cost in problem.getSuccessors(node):
                queue.push((child, path + [action]))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #low cost for StayEastSearchAgent, high cost for StayWestSearchAgent
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #self is implied parameter already passed in
    closed = set()
    fringe = util.PriorityQueue() # ((state currState, list currMoves), int priority)
    #print fringe, to comment out comments its command + /
    start = problem.getStartState()
    fringe.push((start, []), 0) #here item associated is the info from start which is a 
    while not fringe.isEmpty():
        node, path = fringe.pop()
        if problem.isGoalState(node):
            return path
        if node not in closed:
            closed.add(node)
            for child, action, child_cost in problem.getSuccessors(node):
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
    #only stop when we dequeu a goal state
    closed = set()
    fringe = util.PriorityQueue()
    start = problem.getStartState()
    fringe.push((start, []), 0) #here item associated is the info from start which is a 
    while not fringe.isEmpty():
        node, currMoves = fringe.pop()
        currCost = problem.getCostOfActions(currMoves) #this is for the cost part
        if problem.isGoalState(node):
            return currMoves
        if node not in closed:
            closed.add(node)
            for state, action, child_cost in problem.getSuccessors(node):
                updatedMoves = currMoves + [action]
                updatedCost = currCost + child_cost + heuristic(state, problem)
                item = (state, updatedMoves) #child is current node we are looking at
                fringe.push(item, updatedCost)
    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
