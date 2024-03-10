# For each node maintain '5' values i.e three maximum and 2 minimum.
# Because for getting max from multiplication of three values we can get by two ways:

# 1) (+ve, +ve, +ve) : All +ve. In this case we will take three maximum positive value.
# 2) Two negative and one positive. in this case we will take two most negative value and one max positive one.

# Time: O(n)

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:

        n = len(cost)
        adj = collections.defaultdict(list)
        for a , b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()  # this will help in avoiding adding the parent node for any current node.
                        # parent node will get visited first.
        ans = [0] * n

        def dfs(node):
            visited.add(node)  # marking visted 1st time when we will see because we will get ans for this node when we will see 1st time only.
            cost_values = [cost[node]]  # subtree will start from cur node only

            for nei in adj[node]:
                if nei not in visited:
                    cost_values.extend(dfs(nei))  # Add maximum values from all its children
            
            cost_values.sort(reverse = True)
            if len(cost_values) < 3:
                ans[node] = 1
                return cost_values
            # max(0, all_max_+ve, two_most_negative * one most max positive)
            ans[node] = max(0, cost_values[0] * cost_values[1] * cost_values[2] , 
                            cost_values[0] * cost_values[-1] * cost_values[-2])
            
            # return cost_values[: 3] + cost_values[-2 : ] 
            return cost_values if len(cost_values) < 6 else cost_values[: 3] + cost_values[-2 : ]

        dfs(0)

        return ans