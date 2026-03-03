# Method 1: 

# logic: our ans may like betweeen [1, n + k]  (max range: when there is no missing number and num is starting from '1'.)
# store the given arr into set so that we can check in O(1).

# search number in our range i.e if they are present or not.
# if not present then decr k by '1'. and when k reaches '0' 'n' will give the ans.

# time: O(n)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num_set= set(arr)
        for n in range(1, len(arr) +k +1):
            if n not in num_set:
                k-= 1
            if k== 0:
                return n

# method 2:
# Note that the array is in strictly increasing order and hence there is no repetition.
# Think of this case, if every element in the array > k , the answer would be k.
# So, for every element <= k , you need to increment k. (i.e. when you iterate from left to right).
# And since the array is in increasing order, you can break out of the loop on the first instance this condition fails.

# time: O(n)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for n in arr:
            if n <= k:  # abhi tak ka sara ele 'k' se chota h then ans or bda hoga. so incr 'k'.
                k+= 1
            else:  # means all element from now onwards is greater than k.
                break
        return k

# method 3: using Binary Search.
"""
1. Virtual Gap Array: Imagine an array B where each entry tells you how many numbers are missing before that index.
    Formula: missing_count = arr[mid] - (mid + 1)
    Example: If arr[3] = 7, it should have been 4 (1, 2, 3, 4). Since it's 7, we know 7 - 4 = 3 numbers are missing.
2. Binary Search Goal: We search for the largest index where the number of missing elements is still less than k.
After that , answerr = Value at that element + Remaining missing count needed
3. Math: 
    When the loop while start <= end finishes, end is at the last index where missing count < k.
    Our target number is somewhere after arr[end].
    How many more do we need? k - missing_at_end.
    Final Answer = arr[end] + (k - (arr[end] - (end + 1))).
    Simplified: arr[end] + k - arr[end] + end + 1 -> k + end + 1.
    Since the loop ends with start = end + 1, the answer is simply k + start.

Note : Similar way we find the lat index in an array. Here, We search for the largest index where the number of missing elements is still less than k.

Time : O(logn)
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        # start: The index where we expect the missing count to potentially reach k
        start = 0
        # end: The last valid index in the current array
        end = n - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            # Logic: Calculate how many positive integers are missing up to arr[mid]
            # If the value were exactly (mid + 1), 0 would be missing.
            missing_count = arr[mid] - (mid + 1)
            
            if missing_count < k:
                # We haven't reached k missing numbers yet, so the kth missing 
                # must be further to the right.
                start = mid + 1
            else:
                # We found k or more missing numbers, so the kth missing 
                # must be to the left of this or at this index.
                end = mid - 1
        
        # MEANING OF POINTERS AFTER LOOP:
        # end: Points to the highest index where the number of missing elements is < k.
        # start: Points to the first index where the number of missing elements is >= k.
        
        # The kth missing number is: arr[end] + (k - missing_at_end)
        # Simplified math: (k + end + 1) OR (k + start)
        return start + k

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public int findKthPositive(int[] arr, int k) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : arr) {
            numSet.add(num);
        }

        for (int n = 1; n <= arr.length + k; n++) {
            if (!numSet.contains(n)) {
                k--;
            }
            if (k == 0) {
                return n;
            }
        }
        return -1;
    }
}

//Method 2
class Solution {
    public int findKthPositive(int[] arr, int k) {
        for (int num : arr) {
            if (num <= k) {
                k++;  // Increment K if current number <= K
            } else {
                break; // All remaining elements are greater than K
            }
        }
        return k;
    }
}


"""

# C++ Code 
"""
//Method 1

#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        unordered_set<int> num_set(arr.begin(), arr.end());

        for (int n = 1; n <= arr.size() + k; n++) {
            if (num_set.find(n) == num_set.end()) {
                k--;
            }
            if (k == 0) {
                return n;
            }
        }
        return -1;
    }
};

//Method 2
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        for (int num : arr) {
            if (num <= k) {
                k++;  // Increment K if current number <= K
            } else {
                break; // All remaining elements are greater than K
            }
        }
        return k;
    }
};
"""
