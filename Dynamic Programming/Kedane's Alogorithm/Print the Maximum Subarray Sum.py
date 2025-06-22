# method 1: 

# Q: Given an array of integers, 
# find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Time: O(n)
# space: O(1)

def printSubarraySum(arr):
    ansStart, ansEnd= 0, 0   # store the start and endIndex of final ans subArray.
    curSum= 0
    start= 0
    maxSum= float('-inf')
    for i, n in enumerate(arr):
        if curSum < 0:
            start= i
            curSum= n
        else:
            curSum+= n
        # update our ans index , and maxSum
        if curSum > maxSum:
            ansStart= start
            ansEnd= i
            maxSum= curSum
    
    print("SubArray with maximum sum ", arr[ansStart: ansEnd+ 1], "with sum: ", maxSum)
            
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# arr = [-2, -5, 6, -2, -3, 1, 5, -6] 
# arr= [-2,-3,-4, -1]
printSubarraySum(arr)

# Java Code 
"""
class Solution {
    public void printSubarraySum(int[] arr) {
        int ansStart = 0, ansEnd = 0;  // store the start and endIndex of final ans subArray
        int curSum = 0;
        int start = 0;
        int maxSum = Integer.MIN_VALUE;

        for (int i = 0; i < arr.length; i++) {
            if (curSum < 0) {
                start = i;
                curSum = arr[i];
            } else {
                curSum += arr[i];
            }

            // update our ans index, and maxSum
            if (curSum > maxSum) {
                ansStart = start;
                ansEnd = i;
                maxSum = curSum;
            }
        }

        System.out.print("SubArray with maximum sum: [");
        for (int i = ansStart; i <= ansEnd; i++) {
            System.out.print(arr[i]);
            if (i != ansEnd) System.out.print(", ");
        }
        System.out.println("] with sum: " + maxSum);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] arr = {-2, -3, 4, -1, -2, 1, 5, -3};
        sol.printSubarraySum(arr);
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    void printSubarraySum(vector<int>& arr) {
        int ansStart = 0, ansEnd = 0;  // store the start and endIndex of final ans subArray
        int curSum = 0;
        int start = 0;
        int maxSum = INT_MIN;

        for (int i = 0; i < arr.size(); ++i) {
            if (curSum < 0) {
                start = i;
                curSum = arr[i];
            } else {
                curSum += arr[i];
            }

            // update our ans index, and maxSum
            if (curSum > maxSum) {
                ansStart = start;
                ansEnd = i;
                maxSum = curSum;
            }
        }

        cout << "SubArray with maximum sum: [";
        for (int i = ansStart; i <= ansEnd; ++i) {
            cout << arr[i];
            if (i != ansEnd) cout << ", ";
        }
        cout << "] with sum: " << maxSum << endl;
    }
};

int main() {
    Solution sol;
    vector<int> arr = {-2, -3, 4, -1, -2, 1, 5, -3};
    sol.printSubarraySum(arr);
    return 0;
}
"""
