# method 1: use the unsorted approach i.e min heap

# since array is sorted, all the closest element will lie i) either left
# ii) either right iii) or some left and some right of given ele
# since ele 'x' may not be in the list so we take the diff to handle this case.

# Implementation: We are finding the starting index of our ans.
# 'if arr[mid + k]- x >= x - arr[mid]': # then we can't get the ans subarray starting beyond mid.
# Reason: if beyond mid say from 'mid +1' is starting index of ans then , last ele will be at 'mid + k'.
# so if diff between 'last_index - x ' (if start from mid + 1) >= 'x - first_index' (if start from mid)
# Then, we will get closest element till mid only.

# 2nd template only.

# time: O(log(n-k) + k)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if x<= arr[0]:  return arr[0:k]
        # if x>= arr[-1]: return arr[-k:]
        left, right= 0, len(arr) - k   # maximum our starting window can start from 'n-k'.
        while left < right:
            mid= left + (right - left)//2
            if arr[mid + k]- x >= x - arr[mid] : # then we can't get the ans subarray starting beyond mid.
                right= mid
            else:  # here our starting subarray must start from beyond 'mid' i.e mid+1
                left= mid + 1
        return arr[left: left + k]

# Java Code 
"""
import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int left = 0, right = arr.length - k;  // Maximum starting window position

        while (left < right) {
            int mid = left + (right - left) / 2;

            // Check which part has closer values to x
            if (arr[mid + k] - x >= x - arr[mid]) {
                right = mid;
            } else { // The subarray must start beyond 'mid'
                left = mid + 1;
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = left; i < left + k; i++) {
            result.add(arr[i]);
        }
        return result;
    }
}
"""

# C++ Code 
"""
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0, right = arr.size() - k;  // Maximum starting window position

        while (left < right) {
            int mid = left + (right - left) / 2;

            // Check which part has closer values to x
            if (arr[mid + k] - x >= x - arr[mid]) {
                right = mid;
            } else { // The subarray must start beyond 'mid'
                left = mid + 1;
            }
        }

        return vector<int>(arr.begin() + left, arr.begin() + left + k);
    }
};
"""