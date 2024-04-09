# Q: min time needed to reach all the nodes from all possible paths.

# just totally based on Dijkastra Algorithm
# just apply the dijkastra's algo and find the maximum from the array distance that will be the ans, 
# this is the basic way to think from dijkastra algo

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges= defaultdict(list)  # converting into adjacency list with adjacent edges and their weights
        for u,v,w in times:
            edges[u].append((v,w))
        distance= [9999999]*(n+1)
        distance[k]= distance[0]= 0   # will conatin the distance of source to all other vertices
        minHeap= [(0,k)]  # first ele should be weight as it will create the heap using 1st ele always
        visited= set()  # better use an array since searching in set will take O(n) for each time..visited tells whether that node has been relaxed or not
        while minHeap:
            w1,n1= heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            distance[n1]= w1
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,(w1+w2, n2))  
        return max(distance) if len(visited)== n else -1


# another way of writing above code and my mistakes
# we have to take max of all nodes. they are visited with minimum time when they will get poped out from heap.
# So at that time just update our ans.

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj= collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append((v, w))
        min_time= 0
        minHeap= [(0,k)]
        visited= set()  # it will contain the node whose adjacent node is also visited
        while minHeap:
            w1, n1= heapq.heappop(minHeap)
            if n1 in visited: # if visited simply skip
                continue
            # if not visited, add to visited set and visit all its nodes and update the weight
            visited.add(n1)
            # min_time= max(min_time, w1)   # will take max of all the node times. 
            min_time = w1   # this will also work because w1 will be maximum only. Element getting poped later will have more time.
            for n2,w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,(w1+ w2, n2))   # add in heap by adding the weight of its parent also
                    # min_time= max(min_time, w1+w2)   # writing here will wrong ans as there can be other path also
                    #  with minimum cost and minimum you will get only after poping not here
        return min_time if len(visited)== n else -1  # if len(visited)== n means every node is reachable by the source
    