# Note: if asked to move all zeroes at last without caring about order of non-zero ele then
# We can do like this.

# This logic wil work in Q like : '905. Sort Array By Parity'

# Logic: We have to move zero at last so focus on starting pointer
# Because we have to move from start to end if we find any zero at start.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l , r = 0, len(nums) -1
        while l < r:
            if nums[l] == 0:
                # swap 
                nums[l] , nums[r] = nums[r] , nums[l]
                r -= 1  # no need to incr 'l' as after swapping we can get '0' at 'l' because we are swapping without checking value at 'r'.
            else:
                # in correct position so simply move 'l'
                l += 1 
        return nums

# Java
"""
class Solution {
    public void moveZeroes(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            if (nums[l] == 0) {
                int temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
                r--;  // No need to increment 'l' as swapped value might still be zero
            } else {
                l++;
            }
        }
    }
}
"""

# C++ 
"""
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            if (nums[l] == 0) {
                swap(nums[l], nums[r]);
                r--;  // No need to increment 'l' as swapped value might still be zero
            } else {
                l++;
            }
        }
    }
};
"""

# Now coming to actual Q.

# method 1:
# Similar as '26. Remove Duplicates from Sorted Array' logic.

# logic: whenever you see any '0', search for next non-zero and swap. else skip

# Note VVI: You can't solve this Question using two nested while loop like : "905. Sort Array By Parity"
# because we have to maintain the relative order here.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        i= 0  # i will denote where we have to keep next non-zero ele.
        while i < n :
            if nums[i]== 0:
                # search for next non-zero
                k=  i+ 1
                while k < n and nums[k]== 0:
                    k+= 1
                # means array is already in desired format.
                if k >= n: return nums
                # else swap  
                nums[i], nums[k]= nums[k], nums[i]
            i+= 1
        
# Method 2: 
# optimising the above method
# In above one we are always searching from 'i+ 1' even though we have already traverses more index than 'i + 1'.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        last= 0  # will tell from where we have to search for next non-zero ele. Till here we have alraedy traversed.
        i= 0   #  i will denote where we have to keep next non-zero ele.
        while i < n :
            if nums[i]== 0:
                k=  max(last + 1, i+ 1)  # We will start only from 'i+1' so taking maximum.
                while k < n and nums[k]== 0:
                    k+= 1
                if k >= n: return nums
                nums[i], nums[k]= nums[k], nums[i]
                last= k
            i+= 1
        
# Method 3: 
# New and very creative logic:
# logic: collect all consecutive zeroes and after finding any non-zero do replacement.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n= len(nums)
        snowBallSize= 0
        for i in range(n):
            if nums[i]== 0:
                snowBallSize+= 1   # tring to gather all the zeroes together.
            elif snowBallSize > 0:  # only update the value if we have encounter any zero till now.
                temp= nums[i]
                nums[i -snowBallSize]= temp   # moving the non-zero ele to the leftmost zero. 
                nums[i]= 0   # this should be zero only after replacement.


# Method 4:
# Best one & easiest , just easy way to write method 3
"""
Trying to bring the non-zero value at start so checking non-zero value.
Best one & easiest , just easy way to write method 3

Always do using this approach where you have to find rearrange two types of element keeping order same.
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Thought Process:
        1. Keep a pointer 'pos' to track the next available spot for a non-zero.
        2. Iterate through the array with 'i'.
        3. If nums[i] is non-zero, swap it with nums[pos] and move 'pos' forward.
        """
        pos = 0
        for i in range(len(nums)):
            # If current element is non-zero
            if nums[i] != 0:
                # Swap current with the 'next available' non-zero position
                nums[pos], nums[i] = nums[i], nums[pos]
                # Increment the write-position
                pos += 1

# --- Example Walkthrough ---
# nums = [0, 1, 0, 3, 12]
# i=0 (0): Skip.
# i=1 (1): Swap nums[0] & nums[1] -> [1, 0, 0, 3, 12], pos=1
# i=2 (0): Skip.
# i=3 (3): Swap nums[1] & nums[3] -> [1, 3, 0, 0, 12], pos=2


# Related Questions 
"""
Asked in Google: 
Q) Link : https://leetcode.com/discuss/post/7642193/google-interview-experience-l4-march-202-09bf/ 
You are given an array of strings:

["ad", "awe", "cat", "apple", "dog", ...]
You are also provided with an API:

bool isValid(string s)
This API internally contains a constant string P and returns true if P is a prefix of s. Example:

P = "a"

isValid("ad")   -> true
isValid("awe")  -> true
isValid("apple")-> true
isValid("cat")  -> false
isValid("dog")  -> false
Your task is to rearrange the array so that all valid strings appear at the beginning, 
while minimizing the number of movements in-memory where the array is stored. The relative order of valid strings does not necessarily need to be preserved.

Also, tell the time and space complexity accounting for the API call as well.

Ans :
Since we want to minimize in-memory movements and don't care about relative order, we should avoid shifting elements (which is O(N)) and instead focus on swapping.

The Logic: Two-Pointer Partitioning
To solve this with the minimum number of swaps, we use a two-pointer approach (often called the Hoare Partition Scheme):
    Left Pointer (l): Starts at the beginning of the array. It looks for "invalid" strings that need to be moved out of the front.
    Right Pointer (r): Starts at the end of the array. It looks for "valid" strings that need to be brought to the front.
    The Swap: When the left pointer is stuck on an invalid string and the right pointer is stuck on a valid string, we swap them.

Complexity Analysis
Let N be the number of strings in the array and S be the average length of the strings.


Complexity Analysis
Let N be the number of strings in the array and S be the average length of the strings.
Time Complexity: O(N⋅S)
i)  Array Traversal: Each element is visited at most once by the pointers, giving O(N).
ii) API Cost: The isValid function checks if P is a prefix of s. In the worst case, it compares characters up to the length of P. 
If we assume P can be as long as S, each call is O(S).
Total: N calls × O(S) per call = O(N⋅S).

Space Complexity: O(1)

Note : can be also solved using Method 4 
"""

def rearrange_strings(arr, isValid):
    """
    Logic:
    Partition the array into two halves: [Valid... | Invalid...]
    l: scans for the first invalid string from the left
    r: scans for the first valid string from the right
    """
    l = 0
    r = len(arr) - 1
    
    while l < r:
        # Move l forward as long as it points to a valid string
        while l < r and isValid(arr[l]):
            l += 1
            
        # Move r backward as long as it points to an invalid string
        while l < r and not isValid(arr[r]):
            r -= 1
            
        # If we haven't crossed pointers, we found an invalid string 
        # at 'l' and a valid string at 'r'. Swap them!
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
            # After swap, both indices are now correct, so move pointers
            l += 1
            r -= 1
            
    return arr

# --- Example Call ---
# arr = ["ad", "cat", "awe", "dog", "apple"]
# isValid(s) returns true if it starts with 'a'
# 1. l stops at "cat" (idx 1), r stops at "apple" (idx 4)
# 2. Swap -> ["ad", "apple", "awe", "dog", "cat"]
# 3. l stops at "dog", r stops at "awe". l > r, terminate.

# Java Code 
"""
//Method 1
class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int i = 0;  // Position where next non-zero element should be placed

        while (i < n) {
            if (nums[i] == 0) {
                int k = i + 1;
                while (k < n && nums[k] == 0) {
                    k++;
                }
                if (k >= n) return;
                int temp = nums[i];
                nums[i] = nums[k];
                nums[k] = temp;
            }
            i++;
        }
    }
}
//Method 2
class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int last = 0; // Track last traversed index
        int i = 0;    // Position where next non-zero element should be placed

        while (i < n) {
            if (nums[i] == 0) {
                int k = Math.max(last + 1, i + 1); // Start search only from updated position
                while (k < n && nums[k] == 0) {
                    k++;
                }
                if (k >= n) return;
                int temp = nums[i];
                nums[i] = nums[k];
                nums[k] = temp;
                last = k;
            }
            i++;
        }
    }
}

//Method 3
class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int snowBallSize = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                snowBallSize++;  // Collect zeroes
            } else if (snowBallSize > 0) {
                int temp = nums[i];
                nums[i] = nums[i - snowBallSize];  // Move non-zero elements forward
                nums[i - snowBallSize] = temp;
            }
        }
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int i = 0;  // Position where next non-zero element should be placed

        while (i < n) {
            if (nums[i] == 0) {
                int k = i + 1;
                while (k < n && nums[k] == 0) {
                    k++;
                }
                if (k >= n) return;
                swap(nums[i], nums[k]);
            }
            i++;
        }
    }
};

//Method 2
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int last = 0; // Track last traversed index
        int i = 0;    // Position where next non-zero element should be placed

        while (i < n) {
            if (nums[i] == 0) {
                int k = max(last + 1, i + 1); // Start search only from updated position
                while (k < n && nums[k] == 0) {
                    k++;
                }
                if (k >= n) return;
                swap(nums[i], nums[k]);
                last = k;
            }
            i++;
        }
    }
};

//Method 3
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int snowBallSize = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                snowBallSize++;  // Collect zeroes
            } else if (snowBallSize > 0) {
                swap(nums[i], nums[i - snowBallSize]);  // Move non-zero elements forward
            }
        }
    }
};
"""

# Related Q: 
"""
1) 26. Remove duplicates
2) 905. Sort Array By Parity
3) 75 sort colors
4) 926. Flip String to Monotone Increasing
"""
