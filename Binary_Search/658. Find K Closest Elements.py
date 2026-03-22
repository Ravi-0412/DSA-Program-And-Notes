# method 1: 
# use the unsorted approach i.e min heap
# Time ; O(n * logK)

# Method 2: 
"""
Logic :
We just checking , which one will be the better starting point i.e 'mid' or 'mid + 1'
so if we start from 'mid + 1' then last element = arr[mid + k] 
And arr[mid + k] - x >= x - arr[mid] then it means 'mid' is more better candidate than 'mid + 1' and our ans can't go beyond mid.
else : arr[mid + k] - x < x - arr[mid] (strictly smaller) so obvious starting from 'mid + 1' will be better.

Time : O(log(N - K) + K)
"""
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # 'left' is the lower bound of our possible starting index (0).
        # 'right' is the upper bound of our possible starting index (n - k).
        # We cannot start a window of size k later than index n - k.
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = left + (right - left) // 2
            
            # We compare the element at 'mid' with the element at 'mid + k'.
            # 'mid + k' is the element that would enter the window if we 
            # shifted our start from 'mid' to 'mid + 1'.
            
            # Logic: Is x closer to arr[mid] or arr[mid + k]?
            # Standard distance: abs(x - arr[mid]) vs abs(arr[mid + k] - x)
            # Since arr is sorted, we can simplify the absolute values:
            if  c:
                # If arr[mid] is closer or tied, the window should stay 
                # towards the left. mid could be the start.
                right = mid
            else:
                # If arr[mid + k] is strictly closer, the window MUST 
                # shift right. mid cannot be the start.
                left = mid + 1
        
        # After the loop, 'left' is the optimal starting index.
        return arr[left : left + k]

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
