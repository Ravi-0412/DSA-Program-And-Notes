# can be done by dfs but it will take o(m*n)^2 as for evey cell you have to run the dfs


# method 2: using multisource bfs from gate to room
# reverse the problem and find the distance of room starting from all the gates
# how came with this: since using bfs we can mark all the grid at level one in 1st iteration , at level 2 in 2nd and so on and this only we have to do
# by doing with multisource bfs we can get the optimal ans directly for each grid 

# if you do with single source bfs then it won't work in time O(m*n)

# submitted on coding ninja and lintcode

# no ned to make visited set , grid will behave as visited set automatically when we will check the value.. if value is changes then viisted else not
# but it is always better to don't chnage the data given to you in terms of industry point of view
def wallsAndGates(a, n, m): 
    row,col= n,m
    q= deque()
    distance= 0

    for r in range(row):
        for c in range(col):
            if a[r][c]== 0:
                q.append((r,c))

    while q:
        distance+= 1  # all room at level 1 will have distance 1
        for i in range(len(q)):           
            r1,c1= q.popleft()        
            directions= [[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in directions:
                r,c= r1+dr, c1+dc
                if 0<=r<row and 0<=c<col and  a[r][c]== 2147483647:
                    a[r][c]= distance
                    q.append((r,c))   # for next iterat
    return a



