# you are allowed to move right and down only
def ways(r,c,n,m):
    if r==m or c==n:
        return 1
    return ways(r,c+1,m,n) + ways(r+1,c,m,n)   # right or down

# print(ways(0,0,2,2))   # to reach from (0,0) to (n,m)

# method 2:  you can do in reverse way like n,m to 0,0
# in this case you can take only left or up
def ways1(m,n):
    if n==0 or m==0:
        return 1
    return ways1(m,n-1) + ways1(m-1,n)  # left or up

# print(ways1(2,2))
# print(ways1(1,2))


# Now print all the paths also
# in case of string you don't have to push or pop like array because string is immutable i.e it can't be changed auto when you will change in nay other function call
# so storing the ans in string
def ways2(r,c,m,n,path):
    if r==m and c==n:
        print(path)
        return 1
    right,down= 0,0
    if c<=m:
        right= ways2(r,c+1,m,n,path+"R")    # R: Right
    if r<=n:
        down= ways2(r+1,c,m,n,path+"D")     # D: down
    return right + down

print("path :")
print("path no of ways: ",ways2(0,0,2,2,""))


# my mistakes
def ways2(r,c,m,n,path):
    if r==m or c==n:  # my mistake: you have to reach end point for printing the path
        print("".join(path))
        return 1
    path.append('R')
    # r= ways2(r,c+1,m,n,path)   # my mistake, i was storing ans in same var name as passes in parameter by mistake
    right= ways2(r,c+1,m,n,path)
    path.pop()
    path.append('D')
    down= ways2(r+1,c,m,n,path)  
    return right + down

print("path :")
print("path no of ways: ",ways2(0,0,2,2,[]))


# not able to do by storing the path in list
# tried a lot. have to ask someone
def ways2(r,c,m,n,path):
    if r==m and c==n:
        print("".join(path.copy()))
        return 1
    right,down= 0,0
    if c<=m:
        path.append('R')
        right= ways2(r,c+1,m,n,path)
    # path.pop()  # this i got by dry run that it won't work 
    if r<=n:
        path.append('D')
        down= ways2(r+1,c,m,n,path)  
    return right + down

print("path :")
print("path no of ways: ",ways2(0,0,1,1,[]))


# Q: you are allowed to go diagonally also
def ways4(r,c,m,n,path):
    if r==m and c==n:
        print(path)
        return 1
    diagonal,right,down= 0,0,0
    if r<=m and c<=n: #   D:diagonal, incr row and col both by 1
        diagonal= ways4(r+1,c+1,m,n,path+"D")   
    if c<=n:
        right= ways4(r,c+1,m,n,path+"H")       # H: horizonatl
    if r<=m:
        down= ways4(r+1,c,m,n,path+"V")       # V: vertical
    return diagonal+ right + down
