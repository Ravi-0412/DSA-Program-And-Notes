# logic: when we are standing at any node then to have same path value to leaf from the current node
# cost value to leaf from both the subtree must be same.
# if not same then we will incr the value of node in subtree having lower value by their diff i.e abs(l- r)'.

# Reason: current  node will common to both (left and right subtree), so ans will depend on the left and right subtree value only.

# will go bottom up.

# After that at each function call(at each node), we will return the cost to leaf from the current node.

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.count= 0
        
        def dfs(index):
            # if leaf node
            if 2*index >= n and 2*index + 1 >= n:
                return cost[index -1]
            l= dfs(2*index)
            r= dfs(2*index + 1)
            # to make the both subtree to have same weight till leaf 
            self.count+= abs(l - r)
            return cost[index -1] + max(l, r)  # return the cost to leaf from this node
        
        dfs(1)  # calling from index '1'.
        return self.count
