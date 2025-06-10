# Note vvi: What actually we need to find?
# Ans: Minimum number (when subsequence is combined as a single number) of length 'k'. 

# And minimum number we will get when number will be in increasing order if number of ele from minimum ele >= k.

# logic: Suppose min ele of nums is at index 'i' and there is >= k no of element from index 'i'.
# then we simply need to return 'k' ele starting from 'i'.

# vvvi: for this we need to maintain a increasing order stack of len(k).

# VVi:if you see smaller number , keep on poping until you find find any ele <= num.
# Note: But in doing this process we might left with ele < k at last.
# So we will only pop if "sum of ele in stack + remaining ele left to traverse including the current one" > k.

# But we will only add ele in stack if len(stack) will be < k.

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, num in enumerate(nums):
            
            # But before poping we need to check if "sum of ele in stack + remaining ele left to traverse including the current one" > k
            while stack and stack[-1] > num and (len(stack)  + (len(nums) - i)) > k:
                stack.pop()
            # only add ele in stack if len(stack) will be < k.
            if len(stack) < k:
                stack.append(num)
        return stack

# Note vvi: When you have to find smallest / greatest ele i..e number in ascending or descending order use stack.
# use stack .

# Java Code 
"""
import java.util.*;

class Solution {
    public int[] mostCompetitive(int[] nums, int k) {
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];

            // Before popping, ensure remaining elements allow forming a sequence of length 'k'
            while (!stack.isEmpty() && stack.peek() > num && (stack.size() + (nums.length - i)) > k) {
                stack.pop();
            }

            // Only add element if the stack size is less than 'k'
            if (stack.size() < k) {
                stack.push(num);
            }
        }

        // Convert stack to result array
        int[] result = new int[k];
        for (int i = k - 1; i >= 0; i--) {
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
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        vector<int> stack;
        
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];

            // Before popping, ensure remaining elements allow forming a sequence of length 'k'
            while (!stack.empty() && stack.back() > num && (stack.size() + (nums.size() - i)) > k) {
                stack.pop_back();
            }

            // Only add element if the stack size is less than 'k'
            if (stack.size() < k) {
                stack.push_back(num);
            }
        }

        return stack;
    }
};
"""

# Related Q:
# 1) 402. Remove K Digits



