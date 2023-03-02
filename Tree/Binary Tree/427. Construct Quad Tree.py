# logic: first checking if grid starting from (r,c) to(n, n) is a leaf or nor.
# if leaf then simply return with(grid_value , True)
# else recursively check for four sub-grid.
# Finding the sub_grids by top_Left_Position.

# time: O(log*n^2).
# we may have to check till dimension of sub-boxes becomes= 1 from 'n' and we are divinding each time by '2'. so logn times.
# And every time we may have to check nearly 'n^2' cells.

# vvi: It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [val, isLeaf].
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n, r, c):
            isLeaf= True
            for i in range(n):
                for j in range(n):
                    if grid[r][c]!= grid[r+ i][c+ j]:  # if any of the cell has different value.
                        isLeaf= False
                        break
            # check if the current grid is a leaf
            if isLeaf:
                return Node(grid[r][c], True)    # return the cell value for which it is forming leaf and 'True' denoting it is leaf and (all four children will be None auto)
            n= n//2   # if not leaf, checking the other four sub-boxes.
            topLeft= dfs(n, r, c)   
            topRight= dfs(n, r, c + n)
            bottomLeft= dfs(n, r + n, c)
            bottomRight= dfs(n, r + n, c + n)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)   # we are sure that this is not the leaf so return with [any_value, False, with_all_four_children]

        return dfs(len(grid), 0, 0)