
# Understanding the question : SA valid parenthesis is (), ((())) , ()(), ()(()) and so on as such.
# We need to find if the given string is a valid parenthesis, but here's the catch - the "*" - that can act both as ( and ) accoring to the requirement. 

# We will solve this using 2 approaches - Greedy and Recursion. 
# The recursion solution is mostly like a brute force, but the greedy is a 0(n) solution. However, we will see the optimal solution first this time,as it is more intuitive than the recursion solution .


# method 1: 
# By Recursion(TLE)
# time: O(3^n)
# when remove the condition for '*'. it will become the recursive sol for  '(' and ')' only.)
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

# Method 2 :
# optimising the above solution
# time= space= O(n^2) 
class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount= 0  # count the no of open paranthesis
        dp= [[-1 for i in range(len(s) +1)]for i in range(len(s) +1)]
        return self.check(s, 0, openCount, dp)  # '0': start index from where we have to check.
    
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
    

# Method  3: 

"""
Greedy : Most Optimal
While iterating through the string you have 3 possibilites - "(" OR "*" OR ")". We will doscuss what to do in each case.

For "(" : 
When we encounter a open parenthesis, "(" , we are either looking for a ")" to close it or even a "*" would help as it could act as anything.
So, it is quite understandable that whenever we get a "(" , we have something to do in the 'Future'.
So, without any hesitation , whenever we get a open parenthesis, we will push it into the stack for future use .

For "*" :
It can act both as open or closed parenthesis. 
So, we will push it into a sepaarate stack. (Along with the indices - the reason will be understoood at the last)

For ")" : 
If we out open parenthesis stack is empty (i.e, we already have a parenthesis opened which we pushed into the stack), then we pop one element out of it, to close this bracket.
If our open parenthesis stack is empty (i.e, no open parenthesis are left), then we look at the star stack. (i.e, if our star stack is not empty, then our star can act as open parenthesis for this one). 
So , we pop out our star stack for that matter. 
If both of these doesn't happen, i.e, if both open parenthesis stack and star stack is empty, then it means there is no chance for a closed parenthesis to get an open one.
So, we can immediately return False in that case. 


After completing the iteration, there is an edge case left - 
What if the open parenthesis are not yet closed, and they can be closed using the "*" stars left.

So , now we will iterate through the open parenthesis stack ...
For each open parenthesis, we will see if there is a star present after it ( this is the reason we pushed along with indices into the stack ).

If all the stacks are empty, we will return true. 
Else, we can return false.
"""

"""
TIME COMPLEXITY ANALYSIS :

-> 0(n) for iterating through the array.
-> 0(n) (worst case) for itertating through the left over stack.staticmethod
->> Overall TC : 0(n)


SPACE COMPLEXITY : 
-> O(n) for the stack spaces.
"""


# PYTHON : 


class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        star = []
        for idx, char in enumerate(s):
            if char == '(':
                stk.append( idx )
            elif char == ')':
                if stk:
                    stk.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append( idx )
        while stk and star:
            if stk[-1] > star[-1]:
                return False
            stk.pop()
            star.pop()
        return len(stk) == 0
    


# JAVA : 


'''
class Solution {
    public boolean checkValidString(String s) {
        Stack<Integer> stk = new Stack<>();
        Stack<Integer> star = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(') {
                stk.push(i);
            } else if (ch == ')') {
                if (!stk.isEmpty()) {
                    stk.pop();
                } else if (!star.isEmpty()) {
                    star.pop();
                } else {
                    return false;
                }
            } else {
                star.push(i);
            }
        }
        while (!stk.isEmpty() && !star.isEmpty()) {
            if (stk.peek() > star.peek()) {
                return false;
            }
            stk.pop();
            star.pop();
        }
        return stk.isEmpty();
    }
}
'''



# C++ : 



'''
class Solution {
public:
    bool checkValidString(string s) {
        stack<int> stk, star;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                stk.push(i);
            } else if (s[i] == ')') {
                if (!stk.empty()) {
                    stk.pop();
                } else if (!star.empty()) {
                    star.pop();
                } else {
                    return false;
                }
            } else {
                star.push(i);
            }
        }
        while (!stk.empty() && !star.empty()) {
            if (stk.top() > star.top()) {
                return false;
            }
            stk.pop();
            star.pop();
        }
        return stk.empty();
    }
};
'''