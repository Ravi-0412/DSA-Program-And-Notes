# try to color the node one by one with every possible color

# time: O(m^n): 
# Reason: Every node has 'm' possibility i.e we can color it with any of the 'm' color.

# space: O(n). Recursive depth

def graphColoring(graph, k, V):
    # first create  a adjacency list
    adj= {i:[] for i in range(V)}   # adj= collections.defaultdict(list)
    for i in range(V):
        for j in range(V):
            if graph[i][j]==1:
                adj[i].append(j)
    
    color= [0]*V   # using number 1,2,3....M for 'm' colors.                       
    return isColoringPossible(adj,color,k,V,0)

def isSafe(adj,color,node,node_col):
    for nei in adj[node]:
        if color[nei]== node_col:  # if adjacent node has same color then you can't color with chosen color
            return False
    return True


def isColoringPossible(adj,color,k,n,node):
    # try to color the given node with all possible color
    if node==n:   # means we have colored all the nodes
        return True
        
    for i in range(1,k+1):  
        # check if we can color 'node' with color 'i' safely.
        if isSafe(adj,color,node,i):
            color[node]= i
            # call the function to color the next node safely
            if isColoringPossible(adj,color,k,n,node+1):  
                # if we are able to color the current and next node(all nodes) safely then simply return.
                return True
            # if not possible to color all the nodes with chosen color then backtrack i.e try with different color
            color[node]= 0
    
    # if not possible to color any of the nodes with any of the color then it means not possible to color
    return False