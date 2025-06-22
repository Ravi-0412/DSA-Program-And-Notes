# Method 1: 

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

# Java Code 
"""
import java.util.*;

class Solution {
    public String removeKdigits(String num, int k) {
        int n = num.length();
        k = n - k;   // required length after removing 'k' digit.
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && stack.peek() > num.charAt(i) && (stack.size() + (n - i)) > k) {
                stack.pop();
            }
            if (stack.size() < k) {
                stack.push(num.charAt(i));
            }
        }

        // Now handle the '0' at start.
        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }
        String ans = sb.toString().replaceFirst("^0+", "");
        return ans.isEmpty() ? "0" : ans;

        // or simply return
        // return sb.toString().replaceFirst("^0+", "").isEmpty() ? "0" : sb.toString().replaceFirst("^0+", "");
    }
}
"""

# C++ Code 
"""
#include <string>
#include <stack>

class Solution {
public:
    std::string removeKdigits(std::string num, int k) {
        int n = num.length();
        k = n - k;   // required length after removing 'k' digit.
        std::stack<char> stack;

        for (int i = 0; i < n; ++i) {
            while (!stack.empty() && stack.top() > num[i] && (stack.size() + (n - i)) > k) {
                stack.pop();
            }
            if (stack.size() < k) {
                stack.push(num[i]);
            }
        }

        // Now handle the '0' at start.
        std::string ans;
        while (!stack.empty()) {
            ans = stack.top() + ans;
            stack.pop();
        }

        ans.erase(0, ans.find_first_not_of('0'));
        return ans.empty() ? "0" : ans;

        // or simply return
        // return ans.empty() ? "0" : ans;
    }
};
"""

# Method 2: 
# logic: just keep poping the num from stack when you see curr ele is smaller than the stack_top, else append into stack.
# note: we have to make number smaller so we will remove the most significant digit only. 
# time= space= O(n)

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
import java.util.*;

public class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> stack = new Stack<>();
        
        for (char n : num.toCharArray()) {
            // stack will always contain the ele in ascending order.
            while (!stack.isEmpty() && k > 0 && stack.peek() > n) {
                stack.pop();
                k--;
            }
            stack.push(n);
        }

        if (k > 0) {
            // means we are not able to remove 'k' ele since after a point of time ele were in ascending order.
            while (k-- > 0) stack.pop();  // removing the last 'k' ele.
        }

        // we may be left with leading zeroes at the start and for that we remove leading '0's
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        sb.reverse();
        
        // remove leading zeros
        int index = 0;
        while (index < sb.length() && sb.charAt(index) == '0') {
            index++;
        }
        String ans = sb.substring(index);
        
        // after removing leading zero if ans is not empty then return ans else '0'
        return ans.isEmpty() ? "0" : ans;
    }
}

"""

# C++ Code 
"""
#include <iostream>
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {
        stack<char> stack;

        for (char n : num) {
            // stack will always contain the ele in ascending order.
            while (!stack.empty() && k > 0 && stack.top() > n) {
                stack.pop();
                k--;
            }
            stack.push(n);
        }

        if (k > 0) {
            // means we are not able to remove 'k' ele since after a point of time ele were in ascending order.
            while (k-- > 0 && !stack.empty()) {
                stack.pop();  // removing the last 'k' ele.
            }
        }

        // we may be left with leading zeroes at the start and for that we remove leading '0's
        string sb;
        while (!stack.empty()) {
            sb += stack.top();
            stack.pop();
        }
        reverse(sb.begin(), sb.end());

        // remove leading zeros
        int index = 0;
        while (index < sb.size() && sb[index] == '0') {
            index++;
        }
        string ans = sb.substr(index);

        // after removing leading zero if ans is not empty then return ans else '0'
        return ans.empty() ? "0" : ans;
    }
};

"""
