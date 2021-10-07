class Node:
    currCost = float('inf')
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
    def getCostHotFix(self,node):
        if self.isDiag(node):
            return 10
        else:
            return 14
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
nodes = [] #This list contains all the nodes, thats basically the grid 

#Populates nodes List
def populateGrid(w,h):
    nodes = []
    ctr = 0
    for i in range(-h,0):
        for j in range(w):
            ctr += 1
            nodes.append(Node(j+1,abs(i),ctr,False))

infi = 99999999999999
def calc(start, end, nodeL):
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
    #nodes = explored.copy()

    
def Dijkstra(start, end): # starts from the goal node and picks the cheapest viable node, which ultimately returns the ~shortest~ path
                            # the container gets reversed at the end, so the path is actually from start-end    currNode = end
    calc(nodes[startNode-1], nodes[len(nodes)-1],nodes)
    if start.blocked == True or end.blocked == True:
        return "Either start or end node are blocked, making the pathfinding process unviable!"
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
    found = False
    for k in range(100):
        stop = False
        for n in currNode.availableNodes():
            if n.currCost == infi:
                n.currCost = currNode.currCost - currNode.getCostHotFix(n)
            if n.currCost < currNode.currCost:
                if n.blocked == False:
                    #print("{}".format(n.id))
                    currNode = n
                    path.append(currNode)
                    break
            if currNode.id == start.id:
                stop = True
        if stop:
            found = True
            break
    if found:
        print("Path has been found!")
    else:
        print("The program has failed at finding a path, either the complexity limit was exceeded, or a walkable path was not found!")
        return ""
    pStr = ''
    print("Path between node {} and node {} is:".format(start.id, end.id))
    path.reverse()
    pStr += str(path[0].id)
    for n in range(len(path)):
        if n != 0:
            pStr += ' - {}'.format(path[n].id)
    return pStr


#Populate the grid, the first param is Width, the second is Height
populateGrid(5,5)

#Set start-and endNodes 
# !!! Dont forget that node[0] -> node.id = 1 !!! IT'S A LIST !!! #
startNode = 1
endNode = 25

#Define which nodes will be blocked off
#nodes[6].blocked = True <-- This indicates which nodes are blocked off, default value is False
nodes[6].blocked = True

print(Dijkstra(nodes[startNode-1], nodes[endNode-1]))
