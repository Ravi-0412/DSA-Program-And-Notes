# i was getting how to do but not able to write.
# REcursion me jyada dimag mat lagao bs likh do jo lage kam karega recusrsively nhi to recursion me kabhi bhi confidence nhi aayeaga.

# logic: just check for char of s3 in s1 or s2 if it present in any of tehm them then incr the pointer of that string.
# there will be two cases either char in s3 can be present in s1 or s2.
# index of s3 will be : i+j since we are forming s3 only from s1 + s2

# if we get continous char from same string then it's fine only as it will get counted as whole one time only when switching will happpen,
# so order will be maintained only.

# recursive:
# time: O(2^(n+m))
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2)!= len(s3):
            return False
        return self.helper(0, 0,s1, s2, s3)
    
    def helper(self, i, j, s1, s2, s3):
        if i== len(s1) and j== len(s2):
            return True
        # checking char at curr index in 's3' is same as either curr index in s1 or s2
        # index of s3 will be always equal to 'i+j' since we are forming s3 from s1 and s2 
        if i < len(s1) and s1[i]== s3[i+j]  and self.helper(i+1, j, s1, s2, s3):
            return True
        if j < len(s2) and s2[j]== s3[i+j]  and self.helper(i, j+1, s1, s2, s3):
            return True
        return False

# memoization
# time= space= O(m*n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2)!= len(s3):
            return False
        dp= [[-1 for j in range(len(s2) +1)] for i in range(len(s1) + 1)]
        return self.helper(0, 0,s1, s2, s3, dp)
    
    def helper(self, i, j, s1, s2, s3, dp):
        if i== len(s1) and j== len(s2):
            return True
        if dp[i][j]!= -1:
            return dp[i][j]
        # checking char at curr index in 's3' is same as either curr index in s1 or s2
        # index of s3 will be always equal to 'i+j' since we are forming s3 from s1 and s2 
        if i < len(s1) and s1[i]== s3[i+j]  and self.helper(i+1, j, s1, s2, s3, dp):
            dp[i][j]= True
            return True
        if j < len(s2) and s2[j]== s3[i+j]  and self.helper(i, j+1, s1, s2, s3, dp):
            dp[i][j]= True
            return True
        dp[i][j]= False
        return False