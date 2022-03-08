# creating a matrix 
# 1st method

def matrix(m,n):
    result= []   # final matrix
    for i in range(m):
        row= []  # will store the content of each row in each iteration
        for j in range(n): # will traverse through each row
            num= int(input("enter the no: "))
            row.append(num)
        # after each row append the content of each row into resultant list to make it a matrix
        result.append(row)
        # print(result)
         
m= int(input("enter the no of row: "))
n= int(input("enter the no of col: "))
A= matrix(m,n)



# another method and some more thing

# arr= [0]*6   # 1D array
# print(arr)

# way to create 2D matrix
arr= [[0]*3]*6   # will make a 2D array where no of rows= 6
                    # and col= 3
                
# OR
# arr= [[0 for i in range(3)] for i in range(4)]  # row=3, col= 4
print(arr)

# method to acccess the each row in 2D array
for i in arr:
    print(i)


# accessing the row and col 

A = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]] 
for i in A:
    for j in i:
        print(j,end = " ")
    print()


# e.g: finding transpose of a matrix
matrix= [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# transpose= []
# for i in range(4):
#     lst= []
#     for row in matrix:
#         lst.append(row[i])
#     transpose.append(lst)
# print(transpose)

# concise way of finding the transpose of a matrix
transposed= [[row[i] for row in matrix] for i in range(4)]
print(transposed)


# accessing the ele of the matrix
# method 1:

matrix= [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
# here row=3,col=4
for row in matrix:   # will point to one of the row of matrix one by one
    # print(row)
    for i in row:   # will point to elements of particular row one by one
        print(i)

# method2- e.g: 
# reversing the each row of the given matrix   
# will work only when no of rows and col is known

# traverse each row of the matrix
# for i in range(3):   # as no of row in matrix= 3
#     start= 0
#     end= 4-1   # col-1
#     while start< end:   # we only have to go till mid-1 to reverse each array(row)
#         matrix[i][start],matrix[i][end]= matrix[i][end], matrix[i][start]
#         # now incr 'start' and decr 'end' to swap the next pair
#         start+= 1
#         end-= 1
# print(matrix)


# reversing a given matrix when no of rows and col is not known
# shortcut and best
reverse=[[row[-i] for i in range(1,len(row)+1)] for row in matrix]
print(reverse)

# reversing a given matrix when no of rows and col is not known
# for row in matrix:
#     col= len(row)   # no of col is equal to the no of ele in each row
#     start,end= 0, col-1
#     while start< end:
#         row[start], row[end]= row[start], row[end]
#         start+= 1
#         end-= 1
# print(matrix)



# method to reverse only the row not the individual ele in the row
matrix.reverse()
print(matrix)