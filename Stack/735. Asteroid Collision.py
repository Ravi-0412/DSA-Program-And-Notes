# Method 1: 

# very nice Q.
# logic: overall, there are totally 4 scenarios will happen: 1.(+,+) 2.(-,-) 3.(+,-) 4.(-,+)  => see this combination as resultant also 
# But collision will hapen in 3rd case only.(not even in 4th case)
# i.e if we traverse from left to right in array then for collision 1st asteroid (left one) must be moveing towards right,
# and 2nd one must be moving towards left. (+, -)
# why? => just draw on paper .

# what does this mean?
# Ans: It means that when we will see the asteroid going left (-ve) then, 
# it will collide  with all the asteroid on left of it going right(+ve).
# Means we need to search for the pre asteroids before left going right .

# From here we get the intitution for 'stack' i.e after seeing any negative value we wil search for +ve values left of it.

# How to do ?
# 1) whenever you see positive value(going right) store them into stack simply.
# 2) when you see -ve value (going left) then, collision will happen.

# But till when they will collide?
# 1) when stack is not empty and there is +ve value(opposite one) on stack and 'stack[-1] < abs(num)'.
# see the explanation in coding

# time: o(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack= []
        for num in asteroids:
            if num > 0:
                stack.append(num)
            else:
                # keep on poping as the curr one will cancel the stack top.
                while stack and stack[-1] > 0 and stack[-1] < abs(num):
                    stack.pop()
                #stack can be empty only or have become empty after poping(curr -ve have cancel all ball due to high magnitude) or
                # stack top is of same sign i.e -ve only, so append in stack
                if not stack or stack[-1] < 0:  
                    stack.append(num)
                # if magnitude of both equal then both will get cancelled, so pop from stack.
                elif stack[-1]== abs(num):
                    stack.pop()
        return stack

# Java Code 
"""
import java.util.*;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();

        for (int num : asteroids) {
            if (num > 0) {
                stack.push(num);
            } else {
                // Keep popping as the current asteroid will cancel the stack top
                while (!stack.isEmpty() && stack.peek() > 0 && stack.peek() < Math.abs(num)) {
                    stack.pop();
                }
                // Stack can be empty or have become empty after popping (current -ve asteroid cancels all)
                // or stack top is of the same sign (negative only), so append to stack
                if (stack.isEmpty() || stack.peek() < 0) {
                    stack.push(num);
                }
                // If magnitude of both asteroids is equal, both get canceled, so pop from stack
                else if (stack.peek() == Math.abs(num)) {
                    stack.pop();
                }
            }
        }

        int[] result = new int[stack.size()];
        for (int i = stack.size() - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }

        return result;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> st;

        for (int num : asteroids) {
            if (num > 0) {
                st.push(num);
            } else {
                // Keep popping as the current asteroid will cancel the stack top
                while (!st.empty() && st.top() > 0 && st.top() < abs(num)) {
                    st.pop();
                }
                // Stack can be empty or have become empty after popping (current -ve asteroid cancels all)
                // or stack top is of the same sign (negative only), so append to stack
                if (st.empty() || st.top() < 0) {
                    st.push(num);
                }
                // If magnitude of both asteroids is equal, both get canceled, so pop from stack
                else if (st.top() == abs(num)) {
                    st.pop();
                }
            }
        }

        vector<int> result;
        while (!st.empty()) {
            result.insert(result.begin(), st.top());
            st.pop();
        }

        return result;
    }
};
"""


