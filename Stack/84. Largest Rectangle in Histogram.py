# very simple, time: O(n)

# Logic: if we conside the cur bar as height how much width we can get
# i.e how much we can go in left or right.

# Any bar can go 'left smaller next' to its left and 'right smaller next' to its right.
# so just find the 'left smaller next' and 'right smaller next' for each element.

class Solution:
    def largestRectangleArea(self, heights):
        n,max_area= len(heights),0
        left_smaller=  self.LeftSmallerNext(heights,n)     # will contain the indices of next smaller left for each ele
                                                           # means before that index they can go in the left
        right_smaller= self.RightSmallerNext(heights,n)    # will contain the indices of next smaller right for each ele
                                                           # means before that index they can go in the right
        for i in range(n):
            width= (right_smaller[i]-left_smaller[i]) -1    # range in which they can go 
            local_area= heights[i]*width   
            max_area= max(max_area, local_area)
        return max_area
               
    def LeftSmallerNext(self,heights,n):
        stack,ans= [],[]
        for i in range(n):
            while stack and heights[stack[-1]]>= heights[i]:
                stack.pop()
            if not stack:  # if no next smaller exist means it can go till zero
                ans.append(-1)   # appending '-1' it means that ele can go before the index -1 i.e till zero
            else:  # means you have found the ans
                ans.append(stack[-1])    # in this case ele can go before the index of top of the stack in the left
            stack.append(i)
        return ans
    
    def RightSmallerNext(self,heights,n):
        stack,ans= [], []
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>= heights[i]:
                stack.pop()
            if not stack:   # if no next smaller exist means it can go till 'n'
                ans.append(n)
            else:   # means you have found the ans
                ans.append(stack[-1])   # in this case ele can go before the index of top of the stack in the right
            stack.append(i)
        return ans[::-1]


# Have to understand below 2 solutions later.
# Must understand properly for saving coding time.

# method 2: concise one(good one), single traversal, time: O(n)

# Understand this properly.

# index will always give the right margin i.e before till index stack[poped] can go in right side
# basically stack me push hi hm 'next smaller left' kar rhe and index right margin bta rha
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        maxArea, stack, index= 0, [], 0
        while(index < len(heights)):
            if not stack or heights[index] >= heights[stack[-1]]:   # just push index in the stack and incr the index
                stack.append(index)  #ye actual me next smaller left hi append ho rha, har top of the stack ke liye
                index+= 1
            else:   # if heights[index] < heights[stack[-1]]  means right marging mil gya poped ele ka..
                    # right side me stack[poped] index ke phle tak ja sakta h or
                    # left side me stack[top] tak ja phle tak ja sakta h(poped ele ke liye) agar stack empty nhi hua poped karne ke bad to
                    # agar stack empty ho gya to iska matlab wo abhi tak ka sbse chota ele tha stack me 
                    # is case in wo index tak ja sakta h(i.e from 0 to index so, multiply by index directly)
                topOfStack= stack.pop()
                currArea= heights[topOfStack] *((index- stack[-1]-1) if stack else index)  
                maxArea= max(currArea, maxArea)
        while stack:  # agar abhi bhi stack empty nhi h iska matlab ki stack me sb incresing order me ele h
                      # means all can go before index in right side and before  stack[-1] into the left if stack is not empty after poping 
                      # and in case empty means in left it can go till zero 
            topOfStack= stack.pop()
            currArea= heights[topOfStack] *((index- stack[-1]-1) if stack else index)
            maxArea= max(currArea, maxArea)
        return maxArea


# method 3, time: O(n)
# have to realise it properly once again, not getting why doing like this. will see this later
# very concise one of above method 
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/995249/Python-increasing-stack-explained
# whenever you see any ele greater than equal on the stack to the current index
# then just calculate the area like above method 
# it just finding the next smaller and stopping there
def largestRectangleArea(self, heights):        
    stack, area= [], 0
    for i ,h in enumerate(heights+ [0]): # to evaluate the last ele, just append with smallest ele possible
        while stack and heights[stack[-1]]>= h:  # matlab stack[pop] right side me 'i' tak ja skta h
                                                # and left side me stack[-1] tak after poping the ele
            # h= heights[stack.pop()]             # will give the wrong result as h you are using for iterating also
                                                # this mistake i was making and got after a long time
            H= heights[stack.pop()] 
            W= i if not stack else i-stack[-1]-1
            area= max(area, H*W)
        stack.append(i)
    return area

# Java Code 
"""
//Method 1
import java.util.Stack;

class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length, maxArea = 0;
        int[] leftSmaller = LeftSmallerNext(heights, n);
        int[] rightSmaller = RightSmallerNext(heights, n);

        for (int i = 0; i < n; i++) {
            int width = (rightSmaller[i] - leftSmaller[i]) - 1;
            int localArea = heights[i] * width;
            maxArea = Math.max(maxArea, localArea);
        }
        return maxArea;
    }

    private int[] LeftSmallerNext(int[] heights, int n) {
        Stack<Integer> stack = new Stack<>();
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && heights[stack.peek()] >= heights[i]) {
                stack.pop();
            }
            ans[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        return ans;
    }

    private int[] RightSmallerNext(int[] heights, int n) {
        Stack<Integer> stack = new Stack<>();
        int[] ans = new int[n];

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && heights[stack.peek()] >= heights[i]) {
                stack.pop();
            }
            ans[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }
        return ans;
    }
}
//Method 2
import java.util.Stack;

class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxArea = 0, index = 0;
        Stack<Integer> stack = new Stack<>();

        while (index < heights.length) {
            if (stack.isEmpty() || heights[index] >= heights[stack.peek()]) {
                stack.push(index);
                index++;
            } else {
                int topOfStack = stack.pop();
                int width = stack.isEmpty() ? index : index - stack.peek() - 1;
                maxArea = Math.max(maxArea, heights[topOfStack] * width);
            }
        }

        while (!stack.isEmpty()) {
            int topOfStack = stack.pop();
            int width = stack.isEmpty() ? index : index - stack.peek() - 1;
            maxArea = Math.max(maxArea, heights[topOfStack] * width);
        }

        return maxArea;
    }
}
//Method 3 
import java.util.Stack;

class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;

        for (int i = 0; i <= heights.length; i++) {
            int h = (i == heights.length) ? 0 : heights[i];

            while (!stack.isEmpty() && heights[stack.peek()] >= h) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }

            stack.push(i);
        }

        return maxArea;
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size(), max_area = 0;
        vector<int> left_smaller = LeftSmallerNext(heights, n);
        vector<int> right_smaller = RightSmallerNext(heights, n);

        for (int i = 0; i < n; i++) {
            int width = (right_smaller[i] - left_smaller[i]) - 1;
            int local_area = heights[i] * width;
            max_area = max(max_area, local_area);
        }
        return max_area;
    }

private:
    vector<int> LeftSmallerNext(vector<int>& heights, int n) {
        stack<int> st;
        vector<int> ans(n);

        for (int i = 0; i < n; i++) {
            while (!st.empty() && heights[st.top()] >= heights[i]) {
                st.pop();
            }
            ans[i] = (st.empty()) ? -1 : st.top();
            st.push(i);
        }
        return ans;
    }

    vector<int> RightSmallerNext(vector<int>& heights, int n) {
        stack<int> st;
        vector<int> ans(n);

        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && heights[st.top()] >= heights[i]) {
                st.pop();
            }
            ans[i] = (st.empty()) ? n : st.top();
            st.push(i);
        }
        return ans;
    }
};
//Method 2
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxArea = 0, index = 0;
        stack<int> st;

        while (index < heights.size()) {
            if (st.empty() || heights[index] >= heights[st.top()]) {
                st.push(index);
                index++;
            } else {
                int topOfStack = st.top();
                st.pop();
                int width = (st.empty()) ? index : index - st.top() - 1;
                maxArea = max(maxArea, heights[topOfStack] * width);
            }
        }

        while (!st.empty()) {
            int topOfStack = st.top();
            st.pop();
            int width = (st.empty()) ? index : index - st.top() - 1;
            maxArea = max(maxArea, heights[topOfStack] * width);
        }

        return maxArea;
    }
};
//Method 3 
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        int maxArea = 0;

        for (int i = 0; i <= heights.size(); i++) {
            int h = (i == heights.size()) ? 0 : heights[i];

            while (!st.empty() && heights[st.top()] >= h) {
                int height = heights[st.top()];
                st.pop();
                int width = (st.empty()) ? i : i - st.top() - 1;
                maxArea = max(maxArea, height * width);
            }

            st.push(i);
        }

        return maxArea;
    }
};
"""
# Related Q:
# "1793. Maximum Score of a Good Subarray" 
