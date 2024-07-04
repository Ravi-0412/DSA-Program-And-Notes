# checking valid paranthesis if it contains only two types of string i.e: '(' and ')'.

# In this type of question, try to do by taking count of '(' rather than pushing and poping.

class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount= 0  # will count the no of open paranthesis
        for i  in range(len(s)):
            if s[i]== '(':
                openCount+= 1
            else:
                openCount-= 1
            if openCount < 0:   # '(' is less than ')'.
                return False
        return openCount== 0

# can do the same logic by Recursion also.
def isValid(self, i, s, open):
        if open < 0:
            return False
        if i== len(s):
            return open== 0
        if s[i]== '(':
            open+= 1
        else:
            open-= 1
            
        return self.isValid(i+1, s, open)


# actual Q
# method 1: by Recursion(TLE)
# time: O(3^n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount= 0  # count the no of open paranthesis
        return self.check(s, 0, openCount)  # '0': start index from where we have to check.
    
    def check(self, s, ind, openCount):
        if openCount < 0:
            return False
        if ind== len(s):
            return openCount== 0
        if s[ind]== '(':
            return self.check(s, ind+1, openCount +1)
        elif s[ind]== ')':
            if openCount <=0:
                return False
            return self.check(s, ind+1, openCount -1)
        elif s[ind]== '*':  # we have three choices either treat this as 1) '('  2) ')' or 3) empty string. 
                          # and if anu of them return True then return True.
            return self.check(s, ind+1, openCount +1) or self.check(s, ind+1, openCount -1) or self.check(s, ind+1, openCount)

# OR 
# in both of the solution(above and this one, remove the condition for '*'. it will become the recursive sol for  '(' and ')' only.)
class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount= 0  # count the no of open paranthesis
        return self.check(s, 0, openCount)  # '0': start index from where we have to check.
    
    def check(self, s, ind, openCount):
        if openCount< 0:
            return False
        if ind== len(s):
            return openCount== 0
        if s[ind]== '(':
            openCount+= 1
        elif s[ind]== ')':
            if openCount <=0: return False
            openCount-= 1
        elif s[ind]== '*':  # we have three choices either treat this as 1) '('  2) ')' or 3) empty string. 
                            # and if anu of them return True then return True.
            return self.check(s, ind+1, openCount +1) or self.check(s, ind+1, openCount -1) or self.check(s, ind+1, openCount)
        return self.check(s, ind+1, openCount)    # if only either '(' or ')' comes at current index.

# optimising the above solution
# time= space= O(n^2) 
class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount= 0  # count the no of open paranthesis
        dp= [[-1 for i in range(len(s) +1)]for i in range(len(s) +1)]
        return self.check(s, 0, openCount, dp)  # '0': start index from where we have to check.
    
    # @lru_cache(None)   # or simply write this one line to memoise. but not a good way. 
    def check(self, s, ind, openCount, dp):
        if openCount< 0:
            return False
        if ind== len(s):
            return openCount== 0
        if dp[ind][openCount] != -1:
            return dp[ind][openCount]
        if s[ind]== '(':
            dp[ind][openCount]= self.check(s, ind+1, openCount +1, dp)
        elif s[ind]== ')':
            if openCount <=0:
                return False
            dp[ind][openCount]= self.check(s, ind+1, openCount -1, dp)
        elif s[ind]== '*':  # we have three choices either treat this as 1) '('  2) ')' or 3) empty string. 
                          # and if anu of them return True then return True.
            dp[ind][openCount]= self.check(s, ind+1, openCount +1, dp) or self.check(s, ind+1, openCount -1, dp) or self.check(s, ind+1, openCount, dp)
        return dp[ind][openCount]
    

# METHOD 2: optimising the above one to O(n)
# time= O(n), space= O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin, openMax= 0, 0   # max and min no of ')' that can be accomodated.
        for i in range(len(s)):
            if s[i]== '(':
                openMinv += 1
                openMaxv += 1
            elif s[i]== ')':
                openMin -= 1
                openMax -= 1
            elif s[i]== '*':
                openMin -= 1    # 'if '*' behaves as ')'. means one '(' is accomodated by '*'.
                openMax += 1    # 'if '*' behaves as '('. means one more matching of '(' is increased.

            if openMax < 0:
                return False
            openMin= max(openMin, 0)    # openMin can't be negative.(if negative make= 0)
        return openMin== 0    # we are not waiting for anymore ')'.


# Note: read solutions in sheet and also few comments under that.



