# logic: Just exacyly same as 'M-coloring'.
# just treat garden as nodes and flowers as color.

# " choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers."
# This line tells that this is a 'M-coloring' problem only.

# Here we have to print one of the possible ans.

# Note: This will work for every Q of this type.

# Note: there is no node that has more than 3 neighbors, always one possible color to choose.
# so There must be one color availabe to color a node anytime.

# Note: Due to this reason, this  brute force solution get accepted.

# time: O(4**n)

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj= collections.defaultdict(list)
        for u, v in paths:
            adj[u].append(v)
            adj[v].append(u)
        
        def isSafe(node, node_color):
            for nei in adj[node]:
                if color[nei]== node_color:
                    return False
            return True

        def isPlantingPossible(node):
            if node== n + 1:
                # means we have found one ans. so simply add color value of all nodes into the ans.
                for i in range(1, n+ 1):
                    ans.append(color[i])
                return True
            for i in range(1, 4 + 1):   # (k+1)
                if isSafe(node, i):
                    color[node]= i
                    if isPlantingPossible(node + 1):
                        return True
                    # try to plant with different flowers.
                    # color[node]= -1   # No need of this line as there will be one color available for each node so it will return True.
        
        ans= []
        color= [-1]*(n+1)
        isPlantingPossible(1)    # start planting from garden '1'.
        return ans 


# method 2: will only work if no of color is > no of adjacent node for any node.
# Here no_of_color = 4 and max_no_adjacent_node_for_any_node = 3

# logic: There must be one color availabe to color a node.

# Note: Due to this reason,above brute force solution get accepted.
# Reason: Because there is no node that has more than 3 neighbors, always one possible color to choose.

# It says that there are 4 flowers to choose from, but each garden can only have 3 edges. 
# This means that there must be a flower to choose from for each garden and 
# you don't have to worry about choosing the order of the garden to plant flowers in.

# Note: color every node with least value color available(not used by its neighbour).

# time: O(4*n)

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj= collections.defaultdict(list)
        for u, v in paths:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        res= [0]*n  # for each flower, we have to return the color.
        # color each node with available color
        for i in range(n):
            used_colors= set()  # will store the used colors by the nei of node 'i'.
            # check whatever color has been used by its neighbour.
            # Add those into 'used_colors'
            for nei in adj[i]:
                used_colors.add(res[nei])
            # check which color has not been used till now by its nei.
            for color in range(1, 5):
                if color not in used_colors:
                    # if not used then color the cur node with cur 'color'.
                    res[i]= color
        return res
