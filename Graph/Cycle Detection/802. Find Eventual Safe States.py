# main : checking the safe node is making the problem good.
# e.g:Suppose if we are checking a node and if any of its vertices are not in terminal but that can be the safe node.
# This thing is making problem.

# Note: Terminal nodes has no outgoing vertices so these can't be part of a cycle.
# And safe nodes will have all its edges to terminal nodes only so this also can't be part of any cycle.

# Except these nodes i.e terminal and safe all nodes will be part of cycle .

# logic of above: since terminal will be the nodes having no adjacent node and 
# safe nodes are those nodes which have only terminal or safe node as adjacent node.
# i.e if any node reaches to any terminal or safe node then it will not go back. so will not form a cycle.

# vvi: So basically we have to find the 'nodes which doesn't belong to any of cycle formed'.

# One thing to keep in mind:
# Also we do not have to include those nodes which is directly not included in cycle but is a part of cycle i.e 
# it is directly connected to any node which is directly included in the cycle.

# how to solve: just try to find the cycle and if you don't encounter a cycle 
# then all nodes from starting to where call ended(will end only at any terminal node)
# will be safe only since they are not part of any cycle.

# exactly same code as cycle detction in directed graph using dfs.
# only one extra line added to include the node in the ans that's it.

# Note: All terminal node is a safe node since all paths from terminal node go to same terminal node.

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n= len(graph)
        visited= set()
        path_visited= set()   # making this as local variable for each dfs call will give error
        ans= []

        def dfs(node):   #checking cycle
            visited.add(node)
            path_visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei)== True:   # means we have found a cycle. so simply return we don't have to include any node as safe.
                        return True
                elif nei in path_visited:   # means cycle so simply return, because all nodes part of this cycle will not be in our ans.
                    return True
            # if neither of nei is part of a cycle means that is a safe node.
            ans.append(node)    # only extra line than cycle detection.
            path_visited.remove(node)
            return False

        for i in range(n):
            if i not in visited:
                dfs(i)     # we have to call for each component. we don't have to return 
        ans.sort()
        return ans

# later do by Bfs also.
# Kahn's Algo only.