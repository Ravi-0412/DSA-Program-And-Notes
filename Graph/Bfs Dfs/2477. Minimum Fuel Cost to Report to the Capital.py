# Q reduced to: Find the distance from source '0' to all other nodes having seat restriction.
# if seats= 1 then simply find the shortest distance of all nodes from source '0'.

# logic: We need to track the number of people that reach each node and divide that by the number of seats per car, 
# this will tell us the number of cars required to take us to the node that is closer to node '0'.

# 1)We're just calculating the number of people that arrive at a city and then the number of cars that would be 
# required for these people to move from this city to the next one.

# 2) For this we need to find the no of people that arrives at this node.
# For this we need to return 'no of people' from each node.(Just like we used to do in Tree)

# 3) Calculating the number of cars gives the amount of fuel consumed because each car would consume a litre of fuel.


# Note: we start calculating from leaf and send the no of people to the parent & so on.

# Time: O(n)

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj= defaultdict(list)
        for s,d in roads:
            adj[s].append(d)
            adj[d].append(s)

        self.ans = 0
        visited = set()

        def dfs(node):
            visited.add(node)
            people = 1
            for nei in adj[node]:
                if nei not in visited:
                    people += dfs(nei)   # Add people from all its adjacent node
            if node != 0:
                # To avoid calculation after reaching capital
                self.ans += ceil(people / seats)
            return people

        dfs(0)
        return self.ans
    

# Other way.
# time: O(n).

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj= defaultdict(list)
        for s,d in roads:
            adj[s].append(d)
            adj[d].append(s)

        def dfs(node, parent):
            people= 0
            for nei in adj[node]:
                if nei != parent:
                    p= dfs(nei, node)  # here 'p' people at this 'nei' node.
                    self.fuel+= int(ceil(p / seats))  # we will require this much car= fuel, to reach to the node.
                    people+= p  # 
            
            return people + 1   # will send this much people to the parent, '1' to include the curr node also.

        self.fuel= 0
        dfs(0, -1)    # node, parent. to avoid getting into cycle while traversing.
        return self.fuel

    












