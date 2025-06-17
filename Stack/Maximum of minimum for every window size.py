# Method 1: 

# Brute force:
# check for each possible length.
# Time: O(n^3)


class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        res = []

        # check for each possible length.
        for k in range(1, n + 1):  # window size from 1 to n
            max_min = float('-inf')

            for i in range(n - k + 1):  # slide window
                # find min in current window
                curr_min = float('inf')
                for j in range(i, i + k):
                    curr_min = min(curr_min, arr[j])

                max_min = max(max_min, curr_min)

            res.append(max_min)

        return res


# Java
"""
import java.util.*;

class Solution {
    public List<Integer> maxOfMins(int[] arr) {
        int n = arr.length;
        List<Integer> res = new ArrayList<>();

        // check for each possible length.
        for (int k = 1; k <= n; k++) {  // window size from 1 to n
            int maxMin = Integer.MIN_VALUE;

            for (int i = 0; i <= n - k; i++) {  // slide window
                int currMin = Integer.MAX_VALUE;

                for (int j = i; j < i + k; j++) {
                    currMin = Math.min(currMin, arr[j]);
                }

                maxMin = Math.max(maxMin, currMin);
            }

            res.add(maxMin);
        }

        return res;
    }
}


"""

# C++
"""
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    vector<int> maxOfMins(vector<int>& arr) {
        int n = arr.size();
        vector<int> res;

        // check for each possible length.
        for (int k = 1; k <= n; k++) {  // window size from 1 to n
            int maxMin = INT_MIN;

            for (int i = 0; i <= n - k; i++) {  // slide window
                int currMin = INT_MAX;

                for (int j = i; j < i + k; j++) {
                    currMin = min(currMin, arr[j]);
                }

                maxMin = max(maxMin, currMin);
            }

            res.push_back(maxMin);
        }

        return res;
    }
};


"""

# method 2: 
# Optimisation using stack

# Similar to q :"84. Largest Rectangle in Histogram".

# Logic: For every element find the range(length) in which it can be maxiumum.
# and any element can be minimum on it's left or right side until we don't find any smaller ele than this ele.
# 1) first find the nextsmallerLeft and nextSmallerRight for each ele
# 2) then calculate the length in which each element can be minimum.
# length = nextSmallerRight[i] - nextsmallerLeft[i] - 1

# 3) Now update the ans by traversing array again for each length by taking maximum
# value of element that can contribute for that much length.
# ans[length - 1] = max(ans[length - 1], arr[i]) 
# ans[i] : 'maximum of the minimum value' for length of all subarrays of length 'i+1'

# 4) But in 3rd case we can still left with some element in answer that won't be updated.
# for this traverse array again from right to left and update ans like:
# ans[i] = max(ans[i], ans[i + 1])
# why from right to left only?
# because right side contains answer for greater length then it can also contribute to ans of lesser length.

# Time = space = O(n)

class Solution:
    def maxOfMin(self,arr,n):
        left_smaller=  self.LeftSmallerNext(arr,n)     # will contain the indices of next smaller left for each ele
                                                           # means before that index they can go in the left
        right_smaller= self.RightSmallerNext(arr,n)
        
        ans = [float('-inf')] *n    # ans[i] : 'maximum of the minimum value' for length of all subarrays of length 'i+1'
        for i in range(n):
            length = right_smaller[i] - left_smaller[i] - 1
            ans[length - 1] = max(ans[length - 1], arr[i])  # taking value of all the elements that can contribute to ans for this length
        
        #  Some places in answer[] may not be filled yet.
	    # so fill them by taking maximum from right side because right side contains answer for greater length then it can also contribute
	    # to ans of lesser length
	    for i in range(n -2, -1, -1):
	        ans[i] = max(ans[i], ans[i+1])
        
        return ans
        
    
    def LeftSmallerNext(self,arr,n):
        stack, ans= [],[]
        for i in range(n):
            while stack and arr[stack[-1]]>= arr[i]:
                stack.pop()
            if not stack:  # if no next smaller exist means it can go till zero
                ans.append(-1)   # appending '-1' it means that ele can go before the index -1 i.e till zero
            else:  # means you have found the ans
                ans.append(stack[-1])    # in this case ele can go before the index of top of the stack in the left
            stack.append(i)
        return ans
    
    def RightSmallerNext(self,arr,n):
        stack,ans= [], []
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>= arr[i]:
                stack.pop()
            if not stack:   # if no next smaller exist means it can go till 'n'
                ans.append(n)
            else:   # means you have found the ans
                ans.append(stack[-1])   # in this case ele can go before the index of top of the stack in the right
            stack.append(i)
        return ans[::-1]

# Java Code 
"""
import java.util.*;

class Solution {
    public int[] maxOfMin(int[] arr, int n) {
        int[] leftSmaller = leftSmallerNext(arr, n); // Indices of next smaller element to the left
        int[] rightSmaller = rightSmallerNext(arr, n); // Indices of next smaller element to the right
        
        int[] ans = new int[n];
        Arrays.fill(ans, Integer.MIN_VALUE); // ans[i]: maximum of the minimum value for subarrays of length 'i+1'

        for (int i = 0; i < n; i++) {
            int length = rightSmaller[i] - leftSmaller[i] - 1;
            ans[length - 1] = Math.max(ans[length - 1], arr[i]); // Storing max of min values for given lengths
        }

        // Fill missing values by taking max from the right (greater length values can contribute)
        for (int i = n - 2; i >= 0; i--) {
            ans[i] = Math.max(ans[i], ans[i + 1]);
        }

        return ans;
    }

    private int[] leftSmallerNext(int[] arr, int n) {
        Stack<Integer> stack = new Stack<>();
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            ans[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }

        return ans;
    }

    private int[] rightSmallerNext(int[] arr, int n) {
        Stack<Integer> stack = new Stack<>();
        int[] ans = new int[n];

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            ans[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> maxOfMin(vector<int>& arr, int n) {
        vector<int> left_smaller = LeftSmallerNext(arr, n);  // Indices of next smaller element to the left
        vector<int> right_smaller = RightSmallerNext(arr, n); // Indices of next smaller element to the right
        
        vector<int> ans(n, INT_MIN); // ans[i]: maximum of the minimum value for subarrays of length 'i+1'

        for (int i = 0; i < n; i++) {
            int length = right_smaller[i] - left_smaller[i] - 1;
            ans[length - 1] = max(ans[length - 1], arr[i]); // Storing max of min values for given lengths
        }

        // Fill missing values by taking max from the right (greater length values can contribute)
        for (int i = n - 2; i >= 0; i--) {
            ans[i] = max(ans[i], ans[i + 1]);
        }

        return ans;
    }
    
private:
    vector<int> LeftSmallerNext(vector<int>& arr, int n) {
        stack<int> st;
        vector<int> ans(n);

        for (int i = 0; i < n; i++) {
            while (!st.empty() && arr[st.top()] >= arr[i]) {
                st.pop();
            }
            ans[i] = (st.empty()) ? -1 : st.top();
            st.push(i);
        }

        return ans;
    }
    
    vector<int> RightSmallerNext(vector<int>& arr, int n) {
        stack<int> st;
        vector<int> ans(n);

        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && arr[st.top()] >= arr[i]) {
                st.pop();
            }
            ans[i] = (st.empty()) ? n : st.top();
            st.push(i);
        }

        return ans;
    }
};
"""