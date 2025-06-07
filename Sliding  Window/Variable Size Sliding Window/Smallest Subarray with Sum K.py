
# just same logic as "Longest Subarray having sum= k" but here we will update every time to minimise the length.
def lenOfSmallestSubarr(A, N, K) : 
    prefix_sum= {0:-1}    # will store the extra sum(may be negative or positive).
    min_length,curr_sum= float('inf'), 0
    for i in range(N):
        curr_sum+= A[i]
        if (curr_sum-K) in prefix_sum:                                  
            min_length= min(min_length,i-prefix_sum[curr_sum-K])  
        prefix_sum[curr_sum]= i  
            
    return min_length

# arr= [2, 4, 6, 10, 2, 1]
# K = 12 

# arr= [1, 2, 4, 3, 2, 4, 1] 
# K = 7

arr= [-8, -8, -3, 8]
k= 5

n= len(arr)

print(lenOfSmallestSubarr(arr, n, k))

# Java Code
"""
import java.util.*;

class Solution {
    public int lenOfSmallestSubarr(int[] A, int N, int K) {
        Map<Integer, Integer> prefix_sum = new HashMap<>();
        prefix_sum.put(0, -1);  // will store the extra sum (may be negative or positive)
        int min_length = Integer.MAX_VALUE, curr_sum = 0;

        for (int i = 0; i < N; i++) {
            curr_sum += A[i];

            if (prefix_sum.containsKey(curr_sum - K)) {  
                min_length = Math.min(min_length, i - prefix_sum.get(curr_sum - K));
            }

            // Store the first occurrence only, to get the smallest subarray
            prefix_sum.putIfAbsent(curr_sum, i);
        }

        return (min_length == Integer.MAX_VALUE) ? -1 : min_length;
    }

    public static void main(String[] args) {
        int[] arr = {-8, -8, -3, 8};
        int k = 5;
        int n = arr.length;

        Solution sol = new Solution();
        System.out.println(sol.lenOfSmallestSubarr(arr, n, k));
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <unordered_map>
#include <climits>

using namespace std;

int lenOfSmallestSubarr(vector<int>& A, int N, int K) {
    unordered_map<int, int> prefix_sum = {{0, -1}};  // will store the extra sum (may be negative or positive)
    int min_length = INT_MAX, curr_sum = 0;

    for (int i = 0; i < N; i++) {
        curr_sum += A[i];

        if (prefix_sum.find(curr_sum - K) != prefix_sum.end()) {  
            min_length = min(min_length, i - prefix_sum[curr_sum - K]);
        }

        // Store the first occurrence only, to get the smallest subarray
        if (prefix_sum.find(curr_sum) == prefix_sum.end()) {
            prefix_sum[curr_sum] = i;
        }
    }

    return (min_length == INT_MAX) ? -1 : min_length;
}

int main() {
    vector<int> arr = {-8, -8, -3, 8};
    int k = 5;
    int n = arr.size();

    cout << lenOfSmallestSubarr(arr, n, k) << endl;
    return 0;
}
"""