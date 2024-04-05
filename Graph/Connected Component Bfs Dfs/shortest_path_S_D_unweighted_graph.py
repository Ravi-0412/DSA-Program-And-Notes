
# method 1 : using BFS
# logic: just count the level at which destination is present from the source
# this method can be used to find the shortest path even in weighted graph if the weight of each edge will be same.

# Note: First time when you will see the 'destination' that will be ans only.

class Graph:
    def __init__(self,n):
        self.V= n
        self.visited= [False]*n
        self.parent= [-1]*n
        self.distance= ['inf']*n  # value at any index will give the distance of that node from the source
    
    def BFS(self, adj, src, des):
        self.distance[src]= 0
        Q, total_distance= [], 0   # use 'deque' instead of 'q'. 
        self.visited[src]= True
        Q.append(src)
        while Q:
            curr= Q.pop(0)
            for u in adj[curr]:
                if self.visited[u]== False:
                    self.visited[u]= True
                    Q.append(u)
                    self.parent[u]= curr
                    self.distance[u]= self.distance[curr] +1
                    if u== des:
                        total_distance= self.distance[u]
                        
        print(self.parent)
        # for printing the path
        reverse_path, v= [], des
        reverse_path.append(des)
        while self.parent[v]!= -1:
            pred_v= self.parent[v]
            reverse_path.append(pred_v)
            v= pred_v
        # now reverse the reverse_path to get the path from source to destination
        print("path is: ")
        for i in range(len(reverse_path)-1,-1, -1):
            print(reverse_path[i], end= " ")


adj= {0:[1,3], 1:[0,2], 2:[1], 3:[0,4,7], 4:[3,5,6,7], 5:[4,6], 6:[4,5,7], 7:[3,4,6]}
# print(adj)
g= Graph(8)
# g.BFS(adj, 0, 7)
g.BFS(adj, 2, 6)


# Method 2: 

# # Logic: in deque add (node, distance) and when node == destination that will be the ans.
# First time you will see the destination that will be the ans only.

# Method 3: Apply multisource bfs


# Extension of this q:
# 1) Shortest path in Undirected Graph having unit distance
# link: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
