# Note: whenver we have to find the shoretst path, think of bfs in weightage or equal weightage graph.
# and Dijkastra in weightage graph.

# logic: first time we will see any node, that will be the shortest distance from source.

# VVI: Its a simple BFS, with additional constraint of having alternate colored edges in path.
# By navigating the paths, and remembering which colored edge we came from, the next set of edges are chosen with the opposite color.

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
