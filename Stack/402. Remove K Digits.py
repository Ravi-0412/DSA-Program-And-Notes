# Exactly same Q as "1673. Find the Most Competitive Subsequence".

# Required length after removing 'k' number will be 'n-k'.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        k = n - k   # required length after removing 'k' digit.
        stack = []
        for i in range(len(num)):
            while stack and int(stack[-1]) > int(num[i]) and (len(stack) + (n - i)) > k:
                stack.pop()
            if len(stack) < k:
                stack.append(num[i])
        # Now handle the '0' at start.
        ans= "".join(stack).lstrip('0')
        return ans if ans else '0'
    
        # or simply return 
        # return "".join(stack).lstrip("0") or "0"

# time= space= O(n)
# logic: just keep poping the num from stack when you see curr ele is smaller than the stack_top, else append into stack.
# note: we have to make number smaller so we will remove the most significant digit only. 
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack= []
        for n in num:
            while stack and k and stack[-1] > n:   # stack will always contain the ele in ascending order.
                stack.pop()
                k-= 1
            stack.append(n)
        if k : # means we are not able to remove 'k' ele since after a point of time ele were in ascending order.
            stack= stack[:-k]   # removing the last 'k' ele.
        # return "".join(stack).lstrip('0') if stack else '0' # will give error in case e.g: "10" and k= 1. after removing we will be having "0" 
                                                             # and this will give empty ans after removing '0'.
        # we may left with leading zeroes at the start and for that we used lstrip('0)
        ans= "".join(stack).lstrip('0')
        return ans if ans else '0'   # after removing leading zero if ans is not empty then return  ans else '0'.


# Java Code 
"""
//Method 1
import java.util.Stack;

class Solution {
    public String removeKdigits(String num, int k) {
        int n = num.length();
        k = n - k; // Required length after removing 'k' digits
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < num.length(); i++) {
            while (!stack.isEmpty() && k > stack.size() + (n - i) && stack.peek() > num.charAt(i)) {
                stack.pop();
            }
            if (stack.size() < k) {
                stack.push(num.charAt(i));
            }
        }

        // Convert stack to result string
        StringBuilder ans = new StringBuilder();
        while (!stack.isEmpty()) {
            ans.insert(0, stack.pop());
        }

        // Remove leading zeros
        while (ans.length() > 0 && ans.charAt(0) == '0') {
            ans.deleteCharAt(0);
        }

        return ans.length() == 0 ? "0" : ans.toString();
    }
}

"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {
        int n = num.size();
        k = n - k; // Required length after removing 'k' digits
        vector<char> stack;

        for (int i = 0; i < num.size(); i++) {
            while (!stack.empty() && k > stack.size() + (n - i) && stack.back() > num[i]) {
                stack.pop_back();
            }
            if (stack.size() < k) {
                stack.push_back(num[i]);
            }
        }

        // Convert stack to result string
        string ans(stack.begin(), stack.end());
        ans.erase(0, min(ans.find_first_not_of('0'), ans.size())); // Remove leading zeros

        return ans.empty() ? "0" : ans; // If empty after removing leading zeros, return "0"
    }
};

"""