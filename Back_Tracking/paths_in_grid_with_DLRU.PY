# Q) You are allowed to move left, right, up, down. False means 'obstacle is there' and True means 'no obstacle'
# will count and print the path as well
# page: 19
# same approach if obstacles are also there

def Paths(ans, maze, row, col):
    count= 0
    if row== len(maze)-1 and col== len(maze[0])-1:  # corner most will be only the base condition in this case
            print(ans)
            return 1
    # writing all the invalid case together
    if row < 0 or row>= len(maze) or col < 0 or col>= len(maze[0]) or maze[row][col]== False: 
        return 0
    # if not false, make it 'false' 
    # since i am considering this cell for my paths
    maze[row][col]= False  # made it false so again we don't repeat this cell in same path i.e it's child shouldn't take this cell at any point of time.
    count+= Paths(ans+ 'D', maze, row+1, col)   # Down
    count+= Paths(ans+ 'R', maze, row, col+1)   # Right
    count+= Paths(ans+ 'U', maze, row-1, col)   # up
    count+= Paths(ans+ 'L', maze, row, col-1)   # left

    # since now the function is returning back so restore the changes made by the this
    # function call while going down

    maze[row][col]= True
    return count

maze= [[True,True,True],[True,True,True],[True,True,True]]
# print(Paths("",maze,0,0))

maze= [[True,True,True],[True,False,True],[True,True,True]]  # false means at that point there is obstacles
# print(Paths("",maze,0,0))  


# Q)   print all the separate path in a matrix for same Q i.e:
# mark the no 1,2,3,4.... as you traverse the path to reach the destination
def Paths_Matrix(ans, maze, row, col,matrix,step):  # step will increase in each rec call
    if row== len(maze)-1 and col== len(maze[0])-1:  # after reaching the base condition just print the matrix
        matrix[row][col]= step  # last step will be also a step
        for num in matrix:
            print(num)
        print(ans)
        print()
        return     
    if not maze[row][col]:  # if false then simply return
        return 
    # if not false, make it 'false' 
    # since i am considering this cell for my paths
    maze[row][col]= False
    temp = matrix[row][col]
    matrix[row][col]= step  # means you are now using the cell,so write the value of step in that cell

    if row< len(maze)-1:  # then only you can go down
        Paths_Matrix(ans+ 'D', maze, row+1, col,matrix,step+1)
    if col< len(maze[0])-1:  # then only you can go right
        Paths_Matrix(ans+ 'R', maze, row, col+1,matrix,step+1)
    if row >0:  # Then only you can go up
        Paths_Matrix(ans+ 'U', maze, row-1, col,matrix,step+1)
    if col>0:  # Then only you can go left
        Paths_Matrix(ans+ 'L', maze, row, col-1,matrix,step+1)

    # since now the function is returning back so restore the changes made by the this
    # function call while going down

    maze[row][col]= True
    matrix[row][col]= temp  # when you traverse back restore the value of step like pre Q
                        # So that for another function get the original matrix(back tracking)
    

maze= [[True,True,True],[True,True,True],[True,True,True]]
path_matrix= [[0 for j in range(len(maze[0]))] for i in range(len(maze))]  # make a matrix same size as input
print(path_matrix)
Paths_Matrix("",maze,0,0,path_matrix,1)   #step will be initially 1


# Related q: 
# 1) Rat in a Maze Problem - I
# 2) 79. Word Search