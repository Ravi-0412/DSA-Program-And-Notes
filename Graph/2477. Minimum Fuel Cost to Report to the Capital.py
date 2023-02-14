# Q reduced to: Find the distance from source '0' to all other nodes having seat restriction.
# if seats= 1 then simply find the shortest distnce of all nodes from source '0'.

# logic: We need to track the number of people that reach each node and divide that by the number of seats per car, 
# this will tell us the number of cars required to take us to the node that is closer to node '0'.

# 1)We're just calculating the number of people that arrive at a city and then the number of cars that would be 
# required for these people to move from this city to the next one.

# 2) Calculating the number of cars gives the amount of fuel consumed because each car would consume a litre of fuel.

# 3) Also return the amount of people that arrive at this node to the next node, so that we can carry out the 
# above calculations on the next node as well.

# Note: we start calculating from leaf and send the no of people to the parent & so on.
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
                    p= dfs(nei, node)
                    people+= p
                    self.fuel+= int(ceil(p / seats))
            
            return people + 1   # '1' to include the curr node also.
        
        self.fuel= 0
        dfs(0, -1)    # node, parent. to avoid getting into cycle while traversing.
        return self.fuel
