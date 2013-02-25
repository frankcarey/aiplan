import math,random
class puzzel:
    def __init__(self):
        #self.node=[]
        self.fronts=[]
        self.GoalNode=['1','2','3','4','5','6','7','8','0']
        self.StartNode=['1','2','3','4','5','6','7','8','0']
        self.PreviousNode=[]
    def Solve(self):
        self.sucessor(self.StartNode)
        nxNode=self.getNextNode()
        print nxNode
        while nxNode!=self.GoalNode:
            self.sucessor(nxNode)
            nxNode=self.getNextNode()
            print nxNode
    def boundries(self, zero):
        if (zero <= 3):
            return [1,3]
        if (zero >= 7):
            return [7,9]
        else:
            return [4,6]
         
    def shufler(self):
                    
        while True:
            node=self.StartNode
            subNode=[]
            direct=random.randint(1,4)
            getZeroLocation=node.index('0')+1
            subNode.extend(node)
            boundry=self.boundries(getZeroLocation)
                    
            if getZeroLocation+3<=9 and direct==1:
                temp=subNode[node.index('0')]
                subNode[node.index('0')]=subNode[node.index('0')+3]
                subNode[node.index('0')+3]=temp
                self.StartNode=subNode
                return
                
            elif getZeroLocation-3>=1 and direct==2:
                temp=subNode[node.index('0')]
                subNode[node.index('0')]=subNode[node.index('0')-3]
                subNode[node.index('0')-3]=temp
                self.StartNode=subNode
                return
                    
            elif getZeroLocation-1>=boundry[0] and direct==3:
                temp=subNode[node.index('0')]
                subNode[node.index('0')]=subNode[node.index('0')-1]
                subNode[node.index('0')-1]=temp
                self.StartNode=subNode
                return
            elif getZeroLocation+1<=boundry[1] and direct==4:
                temp=subNode[node.index('0')]
                subNode[node.index('0')]=subNode[node.index('0')+1]
                subNode[node.index('0')+1]=temp
                self.StartNode=subNode
                return
    
    
    def heruistic(self,node):
        herMisplaced=0
        
        for i in range(9):
            if node[i]!=self.GoalNode[i]:
                herMisplaced +=1
        
        totalHerst=herMisplaced
       
        node.append(totalHerst)
        return node
           
    def sucessor(self,node=[]):
        subNode=[]
        getZeroLocation=node.index('0')+1
        subNode.extend(node)
        boundry=self.boundries(getZeroLocation)
        self.fronts=[]
                
        if getZeroLocation+3<=9:
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')+3]
            subNode[node.index('0')+3]=temp
            self.fronts.append(self.heruistic(subNode))
            subNode=[]
            subNode.extend(node)
        if getZeroLocation-3>=1:
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')-3]
            subNode[node.index('0')-3]=temp
            self.fronts.append(self.heruistic(subNode))
            subNode=[]
            subNode.extend(node)
        if getZeroLocation-1>=boundry[0]:
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')-1]
            subNode[node.index('0')-1]=temp
            self.fronts.append(self.heruistic(subNode))
            subNode=[]
            subNode.extend(node)
        if getZeroLocation+1<=boundry[1]:
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')+1]
            subNode[node.index('0')+1]=temp
            self.fronts.append(self.heruistic(subNode))
            subNode=[]
            subNode.extend(node)     
             
    def getNextNode(self):
        nxNode=[]
        tNode=[]
        while True:
            hrCost=100000
            for i in self.fronts:
                    if(i[-1]<hrCost):
                        hrCost=i[-1]
                        nxNode=i[0:-1]
                        tNode=i
            
            if tNode in self.PreviousNode and tNode in self.fronts:
                self.fronts.remove(tNode)
                self.PreviousNode.append(tNode)
                
            else:
                self.PreviousNode.append(tNode)
                return nxNode     
puzzel = puzzel()
puzzel.Solve()