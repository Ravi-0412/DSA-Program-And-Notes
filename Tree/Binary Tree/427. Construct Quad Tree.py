# logic: first checking if grid starting from (r,c) to(n, n) is a leaf or not.
# if leaf then simply return with(grid_value , True).
# given in Q: If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and
#  set val to the value of the grid and set the four children to Null and stop.

# else recursively check for four sub-grid  and return Node with any value(0/1) with all its four children.
# give in Q: If the current grid has different values, set isLeaf to False and
# set val to any value and divide the current grid into four sub-grids. 
# Finding the sub_grids by top_Left_Position.

# time: O(log*n *n^2).
# we may have to check till dimension of sub-boxes becomes= 1 from 'n' and we are divinding each time by '2'. so logn times.
# And every time we may have to check nearly 'n^2' cells.

# vvi: It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [val, isLeaf].
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n, r, c):  # (r,c) is telling from where we will start checking and 'n' is telling how many sub-boxes we will check.
            isLeaf= True
            for i in range(n):
                for j in range(n):
                    if grid[r][c]!= grid[r+ i][c+ j]:  # if any of the cell has different value.
                        isLeaf= False
                        break
            # check if the current grid is a leaf
            if isLeaf:
                return Node(grid[r][c], True)    # return the cell value for which it is forming leaf and 'True' denoting it is leaf and (all four children will be None auto)
            n= n//2   # if not leaf, checking the other four sub-boxes. this much dimension we have to check now from (r, c).
            topLeft= dfs(n, r, c)   
            topRight= dfs(n, r, c + n)
            bottomLeft= dfs(n, r + n, c)
            bottomRight= dfs(n, r + n, c + n)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)   # we are sure that this is not the leaf so return with [any_value, False, with_all_four_children]

        return dfs(len(grid), 0, 0)
