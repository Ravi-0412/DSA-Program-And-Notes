# Q: we have to form 'n' pairs in such a way that they are balanced i.e we have to fill '2*n' boxes with '(' and ')'
# in such a way that they form a valid paranthesis.

# just think from basic like how we evaluate the 'valid parenthesis Q'.
# parenthesis is valid only if 'openp==0 at last', it means at last no of '(' and ')' should be equal in number.

# since here we are generating the valid parenthesis, so will get the valid one when 'no of openP== closeP'.
# so we will keep track of both 'openP an closeP' count.

# Note: no return statement at last while adding open and close paranthesis because after adding open or close paranthesis 
# we have to add the close and open paranthesis also so we can't return simply after adding.

# Note vvi: we can reduce this Q to :"generate all possible paranthesis such that count of '(' is >= count of ')' for all prefix".
# in similar way we can replace '(' and ')' with number also.

# jiska count jyada rakna h usko phle add karna h here like '('. and Agar jisko phle add kar rhe wo agar number me bda h dusre
# ke comparison me to automatically decreasing order me ans milega. (in case parathesis ke jagah num lete h tb)
# e.g: "Print N-bit binary numbers having more 1s than 0s"

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, stack= [], []
        
        def Backtrack(openP, closeP):
            if openP== closeP== n:  # means stack will be containing one of the valid parenthesis.
                ans.append("".join(stack))
                return
            # can only add '(' if the openP < n
            if openP < n:
                stack.append('(')
                Backtrack(openP +1, closeP)
                stack.pop()
            # only add close paranthesis if no of open Paranthesis is greater than the no of close paranthesis.
            # otherwise it won't be valid one.
            if closeP < openP:
                stack.append(')')
                Backtrack(openP, closeP +1)
                stack.pop()
        
        Backtrack(0,0)    # this will tell the no of open and closed paranthesis we have added till now.
        return ans

# storing the paranthesis formed in string
# Better one
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans= []
        
        def Backtrack(openP, closeP, paran):
            if openP== closeP== n:  # means stack will be containing one of the valid parenthesis.
                ans.append(paran)
                return
            # can only add '(' if the openP < n
            if openP < n:
                Backtrack(openP +1, closeP, paran + "(" )
            # only add close paranthesis if no of open Paranthesis is greater than the no of close paranthesis.
            # otherwise it won't be valid one.
            if closeP < openP:
                Backtrack(openP, closeP +1, paran + ")" )
        
        Backtrack(0,0, "")    # this will tell the no of open and closed paranthesis we have added till now.
        return ans


# writing like this will give error.
# writing in two diff line chages globally like list only.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans= []
        
        def Backtrack(openP, closeP, paran):
            if openP== closeP== n:  # means stack will be containing one of the valid parenthesis.
                ans.append(paran)
                return
            # can only add '(' if the openP < n
            if openP < n:
                paran= paran + "("
                Backtrack(openP +1, closeP, paran )
            # only add close paranthesis if no of open Paranthesis is greater than the no of close paranthesis.
            # otherwise it won't be valid one.
            if closeP < openP:
                paran= paran + ")"
                Backtrack(openP, closeP +1, paran )
        
        Backtrack(0,0, "")    # this will tell the no of open and closed paranthesis we have added till now.
        return ans


# Related Q:
# 1) Print N-bit binary numbers having more 1s than 0s


# Java Code
"""
// Method 1
import java.util.*;

class Solution {
    List<String> ans = new ArrayList<>();
    Deque<Character> stack = new ArrayDeque<>();

    private void Backtrack(int openP, int closeP, int n) {
        if (openP == closeP && openP == n) {  
            // means stack will be containing one of the valid parenthesis.
            StringBuilder sb = new StringBuilder();
            for (char ch : stack) sb.append(ch);
            ans.add(sb.toString());
            return;
        }
        // can only add '(' if the openP < n
        if (openP < n) {
            stack.push('(');
            Backtrack(openP + 1, closeP, n);
            stack.pop();
        }
        // only add close parenthesis if the number of open parentheses is greater than the number of close parentheses.
        // otherwise, it won't be valid.
        if (closeP < openP) {
            stack.push(')');
            Backtrack(openP, closeP + 1, n);
            stack.pop();
        }
    }

    public List<String> generateParenthesis(int n) {
        ans.clear();
        Backtrack(0, 0, n);  // this will track the number of open and closed parentheses added till now.
        return ans;
    }
}
//Method 2
import java.util.*;

class Solution {
    List<String> ans = new ArrayList<>();

    private void Backtrack(int openP, int closeP, String paran, int n) {
        if (openP == closeP && openP == n) {  
            // means paran will be containing one of the valid parenthesis.
            ans.add(paran);
            return;
        }
        // can only add '(' if the openP < n
        if (openP < n) {
            Backtrack(openP + 1, closeP, paran + "(", n);
        }
        // only add close parenthesis if the number of open parentheses is greater than the number of close parentheses.
        // otherwise, it won't be valid.
        if (closeP < openP) {
            Backtrack(openP, closeP + 1, paran + ")", n);
        }
    }

    public List<String> generateParenthesis(int n) {
        ans.clear();
        Backtrack(0, 0, "", n);  // this will track the number of open and closed parentheses added till now.
        return ans;
    }
}

"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> ans;
    vector<char> stack;

    void Backtrack(int openP, int closeP, int n) {
        if (openP == closeP && openP == n) {  
            // means stack will be containing one of the valid parenthesis.
            ans.push_back(string(stack.begin(), stack.end()));
            return;
        }
        // can only add '(' if the openP < n
        if (openP < n) {
            stack.push_back('(');
            Backtrack(openP + 1, closeP, n);
            stack.pop();
        }
        // only add close parenthesis if the number of open parentheses is greater than the number of close parentheses.
        // otherwise, it won't be valid.
        if (closeP < openP) {
            stack.push_back(')');
            Backtrack(openP, closeP + 1, n);
            stack.pop();
        }
    }

    vector<string> generateParenthesis(int n) {
        ans.clear();
        Backtrack(0, 0, n);  // this will track the number of open and closed parentheses added till now.
        return ans;
    }
};
//Method 2 
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> ans;

    void Backtrack(int openP, int closeP, string paran, int n) {
        if (openP == closeP && openP == n) {  
            // means paran will be containing one of the valid parenthesis.
            ans.push_back(paran);
            return;
        }
        // can only add '(' if the openP < n
        if (openP < n) {
            Backtrack(openP + 1, closeP, paran + "(", n);
        }
        // only add close parenthesis if the number of open parentheses is greater than the number of close parentheses.
        // otherwise, it won't be valid.
        if (closeP < openP) {
            Backtrack(openP, closeP + 1, paran + ")", n);
        }
    }

    vector<string> generateParenthesis(int n) {
        ans.clear();
        Backtrack(0, 0, "", n);  // this will track the number of open and closed parentheses added till now.
        return ans;
    }
};
"""
