import math,random, sys, copy, heapq, itertools

class NodeQueue(object):
    def __init__(self):
        self.heap = []
        
    def __getitem__(self, index):
        result = self.heap[index]
        return result

    def add(self, node):
        heapq.heappush(self.heap, node)

    def pop(self):
        node = heapq.heappop(self.heap)
        return node


class Node:
    def __init__(self, tiles, goal, parent):
        self.tiles = tiles
        self.g = 0
        self.h = 0
        self.f = 0
        self.goal = goal
        self.updateF()
        self.hash = ""
        #generate a hash based on the numbers
        for i in self.tiles:
            self.hash += str(self.tiles[i])
        self.parent = parent
        
    def updateF(self):  
        self.f = self.updateG() + self.updateH()
        return self.f

    def updateG(self, n=0):
        self.g = self.g + n
        return self.g
    
    # Computes the heuristic value for a node. 
    def updateH(self):
        manDist=0
        totalDist=0
        # skip counting the range for the empty slot per the class video.
        for i in range(1,9):
            manDist  = self.manhattanDist(self.tiles.index(i), self.goal.index(i))
            totalDist += manDist
            #print "Tile %s manDist is %s  TOTAL: %s" % (i, manDist, totalDist)
        #print node
        self.h = totalDist
        return self.h

    def getTile(self, i=0):
        return self.tiles[i]

    # i is the new place you want to move the zero. No error checking
    def move(self, i):
        print "moving"
        new = copy.deepcopy(self)
        oldZero = new.findTile(0)
        n = new.getTile(i)
        new.tiles[oldZero] = n
        new.tiles[i] = 0
        new.updateG(1)
        new.updateF();
        return new
        
    def findTile(self, n=0):
        return self.tiles.index(n)

    def isGoal(self):
        return (self.tiles == self.goal)
    
    #Calculates the Manhattan distance of 2 points in a 3x3 board.
    def manhattanDist(self, p1, p2):
        row1 = p1/3
        row2 = p2/3
        col1 = p1%3
        col2 = p2%3
        dist = abs(row1 - row2) + abs(col1 - col2)
        #print 'r1: %s, r2: %s, c1: %s, c2: %s, d: %s' % (row1, row2, col1, col2, dist)
        return dist
    
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
        zeroLoc = self.getTile(0)
        down = zeroLoc+3
        up = zeroLoc-3
        left = zeroLoc-1
        right = zeroLoc+1 

        if (zeroLoc <= 2):
            leftBound = 0
        if (zeroLoc >= 6):
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

class Problem():
    def __init__(self, initialState, goalState):
        self.initialState = initialState
        self.goalState = goalState

    def goalTest(self, state):
        isGoal = (self.goalState == state) 

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
                return task
        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return not self.entry_finder
    
def expand(problem, node):
      
    dirs = ["left", "right", "up", "down"]
    successors = []        
    for direction in dirs:
        move = node.checkMove(direction)
        if ( move > -1) :
            successors.add(node.move(move))
    return successors
 
def aStarTreeSearch(problem):
    initialNode = Node(problem.initialState)
    fringe = PriQueue().add(initialNode), initialNode.h)
    while True:
        if fringe.empty() return False
        node = fringe.pop())
        if problem.goalTest(node.tiles):
            return node.actions #path
        for successor in expand(problem, node):
            fringe.add(sucessor, f(successor))
#END

8puzzle = Problem(initialState=[1, 6, 4, 8, 7, 0, 3, 2, 5], goalState=[0, 1, 2, 3, 4, 5, 6, 7, 8])
print aStarTreeSearch(8puzzle)
