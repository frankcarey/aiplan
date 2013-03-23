import math,random, sys, copy, heapq, itertools

class Node:
    def __init__(self, tiles, parent=None):
        self.tiles = tiles
        self.g = 0
        self.hash = ""
        self.actions = []
        self.parent = parent
        if self.parent:
            self.actions = list(parent.actions)
            self.g = parent.g + 1
        self.actions.append(tiles)
        self.resetHash()
        
    def resetHash(self):
        #generate a hash based on the numbers
        self.hash = ""
        for i in self.tiles:
            self.hash += str(i)

    def getTile(self, i=0):
        return self.tiles[i]

    # i is the new place you want to move the zero. No error checking
    def move(self, i):
        oldZero = self.findTile(0)
        n = self.getTile(i)
        newTiles = list(self.tiles)
        newTiles[oldZero] = n
        newTiles[i] = 0
        newNode = Node(newTiles, self)
        return newNode
        
    def findTile(self, n=0):
        return self.tiles.index(n)
    
    def log(self, msg = "", printout = True, stop = False):
        output = msg + "\n"
        for i in range(3):
            n = i * 3
            output += "[" + str(self.tiles[n+0]) + " " + str(self.tiles[n+1]) + " " + str(self.tiles[n+2]) + "] \n"
        output += "h: %s | g: %s | f: %s \n\n" % (self.h, self.g, self.f)
        if (printout == True):
            print output
        if (stop == True) :
            raw_input("Press Enter to continue...")
        return output
 
    def checkMove(self, direction):
        zeroLoc = self.findTile(0)
        down = zeroLoc+3
        up = zeroLoc-3
        left = zeroLoc-1
        right = zeroLoc+1 

        if (zeroLoc <= 2):
            leftBound = 0
        elif (zeroLoc >= 6):
            leftBound = 6
        else:
            leftBound = 3
                
        if (direction == "down" and down<=8):
            return down
        if (direction == "up" and up>=0):
            return up
        if (direction == "left" and left>=leftBound):
            return left
        if (direction == "right" and right<=leftBound+2):
            return right
        #move not valid, return negative number
        return -1
    #custom string representation
    def __str__(self):
        return "%s" % self.log("", False)       


# h using manhatten distance
def manH(state, goalState):
    manDist=0
    # skip counting the range for the empty slot per the class video.
    for i in range(1,9):
        p1 = state.index(i)
        p2 = goalState.index(i)
        row1 = p1/3
        row2 = p2/3
        col1 = p1%3
        col2 = p2%3
        manDist += abs(row1 - row2) + abs(col1 - col2)
        #print "Tile %s manDist is %s  TOTAL: %s" % (i, manDist, totalDist)
    return manDist

class Problem():
    def __init__(self, initialState, goalState):
        self.initialState = initialState
        self.goalState = goalState

    def goalTest(self, state):
        isGoal = (self.goalState == state) 
        return isGoal

class PriQueue():
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.REMOVED = '<removed-task>'      # placeholder for a removed task
        self.counter = itertools.count()     # unique sequence count
    
    def add(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)
    
    def remove(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED
    
    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                #print "pop! f: %s  g: %s h: %s count: %s" % (priority, task.g, manH(task.tiles, eightPuzzle.goalState), count)
                return task
        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return not self.entry_finder
    
def expand(node):
      
    dirs = ["left", "right", "up", "down"]
    successors = []        
    for direction in dirs:
        move = node.checkMove(direction)
        if ( move > -1) :
            successors.append(node.move(move))
    return successors
 
def aStarTreeSearch(problem, h):
    initialNode = Node(problem.initialState)
    fringe = PriQueue()
    fringe.add(initialNode, h(initialNode.tiles, problem.goalState))
    while True:
    #for i in range(1,30):
        if not fringe: return False
        node = fringe.pop()
        if problem.goalTest(node.tiles):
            print "Solution Found!"
            print node.g
            return node.actions #path
        for successor in expand(node):
            fringe.add(successor, successor.g + h(successor.tiles, problem.goalState))
#END

def aStarGraphSearch(problem, h):
    initialNode = Node(problem.initialState)
    fringe = PriQueue()
    fringe.add(initialNode, h(initialNode.tiles, problem.goalState))
    allNodes = set()
    allNodes.add(initialNode.hash)
    while True:
    #for i in range(1,30):
        if not fringe: return False
        node = fringe.pop()
        if problem.goalTest(node.tiles):
            print "Solution Found!"
            print node.g
            return node.actions #path
        for successor in expand(node):
            if not successor in allNodes:
                fringe.add(successor, successor.g + h(successor.tiles, problem.goalState))
                allNodes.add(successor.hash)
#END

def find27StepsSearch():
    initialNode = Node([0,1,2,3,4,5,6,7,8,9])
    fringe = PriQueue()
    fringe.add(initialNode, initialNode.g)
    allNodes = set()
    allNodes.add(initialNode.hash)
    count = 0
    while True:
    #for i in range(1,30):
        if not fringe: return False
        node = fringe.pop()
        if node.g >= 27:
            print "All paths found."
            return count  #path
        for successor in expand(node):
            if not successor.hash in allNodes:
                fringe.add(successor, successor.g)
                allNodes.add(successor.hash)
                #print "add %s" % successor.g
                if successor.g == 27:
                    count += 1
                    #print count
            #else:
                #print "dupe"



treePuzzle = Problem(initialState=[1, 6, 4, 8, 7, 0, 3, 2, 5], goalState=[0, 1, 2, 3, 4, 5, 6, 7, 8])
graphPuzzle = Problem(initialState=[8, 1, 7, 4, 5, 6, 2, 0, 3], goalState=[0, 1, 2, 3, 4, 5, 6, 7, 8])

print "A* star tree: (Ans: 21)"
print aStarTreeSearch(treePuzzle, manH)

print "A* star graph: (Ans: 25)"
print aStarGraphSearch(graphPuzzle, manH)

print "Count all solutions of 27 steps (Ans: 6274)"
print find27StepsSearch()