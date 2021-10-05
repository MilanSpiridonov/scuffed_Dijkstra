import math, time
class Node:
    currCost = float('inf')
    prevNode = None
    lastNodeIndex = None
    def __init__(self,x,y,id,blocked):
        self.x = x
        self.y = y
        self.id = id
        self.blocked = blocked

    def isDiag(self,node):
        if self.x != node.x and self.y != node.y:
            return True
        else:
            return False
    def getCost(self,node):
        if self.isDiag(node):
            return 14
        else:
            return 10
    def availableNodes(self): #returns a list of adjascent nodes
        avN = []
        for n in nodes:
            notDia = False
            if (n.x == self.x - 1 or n.x == self.x + 1) and n.y == self.y:
                avN.append(n)
                notDia = True
            if (n.y == self.y - 1 or n.y == self.y + 1) and n.x == self.x:
                avN.append(n)
                notDia = True
            if notDia == False:
                if n.x == self.x - 1 and n.y == self.y - 1:
                    avN.append(n)
                if n.x == self.x - 1 and n.y == self.y + 1:
                    avN.append(n)
                if n.x == self.x + 1 and n.y == self.y - 1:
                    avN.append(n)
                if n.x == self.x + 1 and n.y == self.y + 1:
                    avN.append(n)
        return avN
    def costToNode(self,node):
        if self.currCost < 99999999999:
            return self.getCost(node) + self.currCost
        else:
            return self.getCost(node) # +0

#Populates nodes List
nodes = []
ctr = 0
for i in range(-5,0):
    for j in range(5):
        ctr += 1
        nodes.append(Node(j+1,abs(i),ctr,False))
infi = 99999999999999


def calc(start, end, nodeL): #this func weighs all the nodes, doesn't support recalculation yet
    #initialize unexplored list, fill it up and set the starting currCost of nodes to infi
    unexplored = []
    explored = []
    for n in nodeL:
        n.currCost = infi
        if n != start:
            unexplored.append(n)
    start.currCost = 0

    #set costs for adjascent nodes for start node:
    for n in start.availableNodes():
        n.currCost = n.getCost(start)
        explored.append(n)
        unexplored.remove(n)

    calced = []
    #go to all current available nodes and update their overall cost:
    cheapestNode = end
    for j in range(100):
        #print("Rotation {} - cheapest node: {}".format(j,cheapestNode.id))
        found = False
        for n in explored:
            if n.currCost <= cheapestNode.currCost and n.blocked == False:
                found = True
                cheapestNode = n
                explored.remove(n)
                calced.append(n)
        if found == False:
                cheapestNode = end
                continue
        for n in cheapestNode.availableNodes():
            if n in unexplored:
                n.currCost = cheapestNode.currCost + n.getCost(cheapestNode)
                explored.append(n)
                unexplored.remove(n)
    nodes = explored.copy()

def Dijkstra(start, end): # starts from the goal node and picks the cheapest viable node, which ultimately returns the ~shortest~ path
                            # the container gets reversed at the end, so the path is actually from start-end
    currNode = end
    path = []
    path.append(currNode)
    for n in currNode.availableNodes():
        #print("{} - {}".format(currNode.currCost,n.currCost))
        if n.currCost < currNode.currCost and n != currNode:
            if n.blocked == False:
                currNode = n
            #print(currNode.id)
    path.append(currNode)
    for k in range(100):
        stop = False
        for n in currNode.availableNodes():
            if n.currCost < currNode.currCost:
                if n.blocked == False:
                    currNode = n
                    path.append(currNode)
                #print(currNode.id)
                    break
            if currNode.id == start.id:
                stop = True
        if stop:
            break
    pStr = ''
    print("Path between node {} and node {} is:".format(start.id, end.id))
    path.reverse()
    pStr += str(path[0].id)
    for n in range(len(path)):
        if n != 0:
            pStr += ' - {}'.format(path[n].id)
    print(pStr)


nodes[5].blocked = True
nodes[6].blocked = True
nodes[11].blocked = True
nodes[12].blocked = True
calc(nodes[0], nodes[len(nodes)-1],nodes) #Calculate the weights for all of the nodes from the earliest node to the end node
Dijkstra(nodes[0], nodes[10]) #Prints out the calculated path ;)

### IT ACTUALLY FUCKING WORKS???!!!?!!???!!????!!??!??????!
###The algo works with walls(fina-fucking-lly) 

###No backtracking
    
    
##Old logs:

### <Update>
### Calc() officially sets the cost of movement from start for each and every node,
### which means I "could" use that to write the algo A* style...
### For now though, im glad I can finally find distance/cost between two nodes.
### Im not entirely sure how im gonna use this, or if Im gonna use it even, but I
### believe it was usefull nonetheless. :3
### </Update
