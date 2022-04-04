# top down approach
def lcs(x,y,s1,s2):
    dp= [[0 for j in range(y+1)] for i in range(x+1)]
    for i in range(1,x+1):
        for j in range(1,y+1):
            if s1[i-1]== s2[j-1]:
                dp[i][j]= 1+ dp[i-1][j-1]
            else:
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
    return dp[x][y]


# memozoid method
# correct only but giving time limit exceeded for some cases
def lcs(x,y,s1,s2):
        dp= [[-1 for j in range(y+1)] for i in range(x+1)]
        if x==0 or y==0:
            return 0
        if dp[x][y]!= -1:   # means already its value is calculated
            return dp[x][y]
        if s1[x-1]== s2[y-1]:
            dp[x][y]= 1+ lcs(x-1, y-1, s1,s2)
            return dp[x][y]
        else:
            dp[x][y]= max(lcs(x-1,y,s1,s2),lcs(x,y-1,s1,s2))
            return dp[x][y]