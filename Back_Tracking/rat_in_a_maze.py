# Q)given a 2d matrix in which '1' represnts rat can take that path 
# '0' means rat can't take that path
# problem: you have to return a matrix in which '1' will
# denote that rat has taken that path and '0' means rat has not taken the path
# you are allowed to go only down and right

def paths(matrix,row,col,ans):
    count= 0
    if row== len(matrix)-1 and col==len(matrix[0]) -1:
        ans[row][col]= 1   # to make '1' visible at the last also
        Display(ans)
        print()
        ans[row][col]=0    # again restore back
        return 1
    if matrix[row][col]== 0:  # means you cant take this path
        return 0
    if row<len(matrix) -1:  # then only you can go down
        ans[row][col]= 1
        count+= paths(matrix,row+1,col,ans)
        ans[row][col]= 0
    if col<len(matrix[0]) -1:  # then only you can go right
        ans[row][col]= 1
        count+= paths(matrix,row,col+1,ans)
        ans[row][col]= 0

    return count

def Display(arr):
    print("path taken by the rat is:")
    for row in arr:
        print(row)


input= [[1,0,1,0,1],[1,1,1,1,1],[0,1,0,1,0],[1,0,0,1,1],[1,1,1,0,1]]
n= len(input)
m= len(input[0])
ans= [[0 for i in range(m)] for j in range(n)]    # to store the ans  
                            # Always create 2d matrix like this if you have to update later
                            # something in the matrix
print("input array is: ")
for row in input:
    print(row)
print()
print("no of possible paths is: ",paths(input,0,0,ans))
