# Note: whenver we have to find the shoretst path, think of bfs in unweightage or equal weightage graph.
# and Dijkastra in weightage graph.


# VVI: Its a simple BFS, with additional constraint of having alternate colored edges in path.
# By navigating the paths, and remembering which colored edge we came from, the next set of edges are chosen with the opposite color.

# logic: we have to keep track of color also i.e choose alternating color node.
# so for visited: we will add (node, color), to check whether we have visited the nei node with same color of cur_node or not.
# For this: we will append (node, length, color) in Q.
# we will add the nei of diff color node only if nei is not visited with that color.

# Here we will get the ans for node when we see the node for 1st time itself that node can get visited by any path i.e red or blue(parent).
# so we will mark the ans after poping only.

# time: O(n)
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # first convert into ajacency list
        red= collections.defaultdict(list)
        blue= collections.defaultdict(list)
        for src, des in redEdges:
            red[src].append(des)
        for src, des in blueEdges:
            blue[src].append(des)
        
        ans= [-1 for i in range(n)]
        q= collections.deque()  
        q.append((0, 0, None))  # [node, length, preEdge-Color]
        visited= set()
        visited.add((0, None))   # (node, preEdge_color). will tell if visited then by which color because we can visit the same node through diff ways.
        while q:
            node, length, edgeColor= q.popleft()
            if ans[node]== -1: # means we have found the ans for that node.
                ans[node]= length

            # now visit the nei 
            # since we can visit the same edge multiple time if we have a different incoming edge.
            # we have to traverse both the cases i.e because we don't know which one of these will lead to a different shortest path.

            if edgeColor!= "red":    # since initially color is 'None'  so doing like this instead of checking equal to(edgeColor==)
                for nei in red[node]:
                    if (nei, "red") not in visited:
                        visited.add((nei, "red"))
                        q.append((nei, length +1, "red"))
            if edgeColor!= "blue":
                for nei in blue[node]:
                    if (nei, "blue") not in visited:
                        visited.add((nei, "blue"))
                        q.append((nei, length +1, "blue"))
        return ans


# if we want to mark ans when we see the node for 1st time itself then.
# visited should be same only as we can visit the same node by diff parent color and any of the path can help in finding the ans for other nodes.
# because we have to follow the alternating color property.
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # first convert into ajacency list
        red= collections.defaultdict(list)
        blue= collections.defaultdict(list)
        for src, des in redEdges:
            red[src].append(des)
        for src, des in blueEdges:
            blue[src].append(des)
        
        ans= [-1 for i in range(n)]
        q= collections.deque()  
        q.append((0, 0, None))  # [node, length, preEdge-Color]
        visited= set()
        visited.add((0, None))   # (node, preEdge_color). will tell if visited then by which color because we can visit the same node through diff ways.
        ans[0]= 0  # for source node
        while q:
            node, length, edgeColor= q.popleft()
            if edgeColor!= "red":    # since initially color is 'None'  so doing like this instead of checking equal to(edgeColor==)
                for nei in red[node]:
                    if (nei, "red") not in visited:
                        visited.add((nei, "red"))
                        q.append((nei, length +1, "red"))
                        if ans[nei]== -1:  # if ans has been not found yet
                            ans[nei]= length + 1
            if edgeColor!= "blue":
                for nei in blue[node]:
                    if (nei, "blue") not in visited:
                        visited.add((nei, "blue"))
                        q.append((nei, length +1, "blue"))
                        if ans[nei]== -1: 
                            ans[nei]= length + 1
        return ans
