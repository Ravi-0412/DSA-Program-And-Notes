# for count ways
# Q no: 62 leetcode

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m== 1 or n== 1:
            return 1
        return self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)

# Now print all the paths also
# in case of string you don't have to push or pop like array because string is immutable i.e 
# it can't be changed auto when you will change in nay other function call.
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

# print("path :")
# print("path no of ways: ",ways2(0,0,2,2,""))


# concise way of writing the above code.
# write all the invalid cases as base case then after that simply call the next function.
def ways2(r,c,m,n,path):
    if r >m or c > n:  # invalid case
        return 0
    if r==m and c==n:
        print(path)
        return 1  # telling the no of ways
    return ways2(r,c+1,m,n,path+"R") + ways2(r+1,c,m,n,path+"D")   # Right and Down

# print("path :")
# print("path no of ways: ",ways2(0,0,2,2,""))

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

# print("path :")
# print("path no of ways: ",ways2(0,0,2,2,[]))

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

# print("path :")
# print("path no of ways: ",ways4(0,0,2,2,""))
# print("path no of ways: ",ways4(0,0,1,1,""))

# concise way of writing above code.
def ways4(r,c,m,n,path):
    if r > m or c > n:
        return 0
    if r==m and c==n:
        print(path)
        return 1
    return ways4(r+1,c+1,m,n,path+"D")  + ways4(r,c+1,m,n,path+"H") + ways4(r+1,c,m,n,path+"V") # Diagonal, Horizontal, Verical

print("path :")
print("path no of ways: ",ways4(0,0,2,2,""))
# print("path no of ways: ",ways4(0,0,1,1,""))