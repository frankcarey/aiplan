import math,random, sys, copy

class Node:
    def __init__(self, tiles, goal):
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

class puzzle:
    def __init__(self, startTiles, goalTiles):
        self.startNode = Node(startTiles, goalTiles)
        self.goalNode = Node(goalTiles, goalTiles)
        
        self.fronts=[self.startNode]
        self.closedNodes=[]
        self.lowestNode = self.startNode

        
    def Test(self):
            #print self.heruistic(self.TestNode)
            
            self.expandTree(self.startNode)
            print self.getNextNode()
            
    def Solve(self):
        while not self.fronts.empty() :
            if self.lowestNode.isGoal() :
                print "VICTORY"
                return
            self.fronts.remove(self.lowestNode)
            self.closedNodes.append(self.lowestNode)
            
            dirs = {"left", "right", "up", "down"}
            
            for direction in dirs:
                move = self.lowestNode.checkMove(direction)
                if ( move > -1) :
                    newNode = self.lowestNode.move(move)
                    if (newNode in self.closedNodes) :
                        continue
                    if (newNode not in self.fronts or self.lowestNode.g > newNode.g) :
                        newNode.parent = self.lowestNode
                        if newNode not in self.fronts:
                            self.fronts.append(newNode)
                    
                    
                    self.fronts.append(newNode)
            print "Fail"
            return        
        
        self.expandTree(self.startNode)
        nxNode=self.getNextNode()
        n = 0 
        #self.log(nxNode)
#        print self.PreviousNode
        #raw_input("Press Enter to continue...")
        while (nxNode.tiles != nxNode.goal):
            n= n+1
            self.expandTree(nxNode)
            nxNode=self.getNextNode()
            if (n > 30 ):
                print "Wrong"
                sys.exit()
            #self.log(nxNode)
            #print self.PreviousNode
            #raw_input("Press Enter to continue...")
        print nxNode
        print n
    
    def expandTree(self,node):        
        dirs = {"left", "right", "up", "down"}
        
        for direction in dirs:
            move = node.checkMove(direction)
            if ( move > -1) :
                newNode = node.move(move)
                if (not (node.hash in self.previousNodes)) :
                    self.fronts.append(newNode)
             
    def getNextNode(self):
        while True:
            for front in self.fronts:
                print "checking front %s" % front
                if(front.f < self.currentNode.f):
                    print "found lower: %s < %s" % (front.f, self.currentNode.f)
                    self.currentNode = front
            
#            if front.hash in self.previousNode and front.hash in self.fronts:
#                print "remove tNode from fronts"
#                self.fronts.remove(tNode)
#                self.PreviousNode.append(tNode)
#                
            else:
                self.closedNodes.append(tNode)
                print "Next node is %s" % nxNode
                return nxNode  
   
puzzle = puzzle([1, 6, 4, 8, 7, 0, 3, 2, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8])
#puzzel.Solve()
puzzle.Solve()