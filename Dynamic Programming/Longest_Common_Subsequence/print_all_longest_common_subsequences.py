#1st method: will print any one possible longest subsequences
# just go from bottom right to top left and just take the pre path you had taken to reach the curr cell and if the char is equal then include into the ans
def FindLcs(m,n,s1,s2):
    dp= [[0 for j in range(n+1)] for i in range(m+1)]  # initialised with base cases
    length= lcs(m,n,s1,s2,dp)
    print("length of longest commom subsequence: ",length)
    return PrintLcs(m,n,s1,s2,dp)
    
def PrintLcs(x,y,s1,s2,dp):
    ans= ""
    i ,j = x, y
    while(i>0 and j>0):
        if s1[i-1]== s2[j-1]:
            ans= s1[i-1] + ans
            # in case of equal you must have taken the diagoanl ele so decr 'i' and 'j' by 1
            i-= 1
            j-= 1
        # if char not equal then we must have taken the max value of left or right up
        # if left > right up take the left one   
        elif dp[i][j-1]>= dp[i-1][j]:  
            j-= 1
        # if right up > left, take the left one 
        else:
            i-= 1
    return ans   
    
    
def lcs(x,y,s1,s2,dp):
    for i in range(1,x+1):
        for j in range(1,y+1):
            if s1[i-1]== s2[j-1]:
                dp[i][j]= 1+ dp[i-1][j-1]
            else:
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
    return dp[x][y]
    
s1= "abcbdab"
s2= "bdcaba"
x,y= len(s1), len(s2)
# print(FindLcs(x,y,s1,s2))


# method 2:To print all possible distinct subsequences
# have to understand this properly 
class Solution:
    def __init__(self,x,y):
        self.x, self.y= x, y    
        self.dp= [[0 for j in range(y+1)] for i in range(x+1)]

    def lcs(self,x,y,s1,s2):
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    self.dp[i][j]= 1+ self.dp[i-1][j-1]
                else:
                    self.dp[i][j]= max(self.dp[i-1][j], self.dp[i][j-1])
        return self.dp[x][y]
    
    def FindLcs(self,x,y,s1,s2):
        # start checking from top to down 
        s= set()
        if x==0 or y==0:   # means you have reached the last row or col of matrix
                          # and there won't be any ele to check as atleast one
                          # of the string index ele will be empty for this index
            s.add("")
            return s
        if s1[x-1]== s2[y-1]:
            temp= self.FindLcs(x-1, y-1,s1,s2)
            for ele in temp:
                s.add(ele + s1[x-1])
        else:
            # follow the path which has maximum value
            if self.dp[x-1][y]>= self.dp[x][y-1]:
                s= self.FindLcs(x-1, y,s1,s2)
            if self.dp[x][y-1]>= self.dp[x-1][y]:
                temp= self.FindLcs(x, y-1,s1,s2)
                # merge two sets in s to get added in equal to condition
                # because all the smaller subsequences will have to get added in equal to condition
                for ele in temp:
                    s.add(ele)   # all smaller subsequences will get added as
                                 # diff ele in set 
                                 # when equal to condition will satisfy,this all ele of sets
                                 # will get added to the char at equal to condition one by one
        return s

s1= "qpqrr"
s2= "pqprqrp"
# s1= "abcbdab"
# s2= "bdcaba"
# s1= "abc"
# s2= "acb"
# s1= "dcbcf"
# s2= "abcdaf"
x,y= len(s1), len(s2)
ob= Solution(x,y)
print("length of the longest subsequences is: ",ob.lcs(x,y,s1,s2))
print("all possible distinct subsequences are: ")
s= ob.FindLcs(x,y,s1,s2)
for i in s:
    print(i)

