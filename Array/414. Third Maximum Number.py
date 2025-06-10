# first see 2nd distinct maximum
# Note: 2nd distinct maximum

# Code for 2nd maximum (submitted on gfg)
class Solution: 
	def print2largest(self,arr, n):
		firstMax, secondMax = -1, -1  
		for num in arr:
		    if num > firstMax:
		        # 'num' is greatest number till now
		        # so in this we will have to update both 'firstMax' and 'secondMax'
		        # Update 'secondMax' to 'firstMax' and then 'firstMax' to cur 'num'.
		        secondMax = firstMax
		        firstMax  =  num
		    elif num > secondMax and num != firstMax:  # checking num != firstMax to avoid duplicate
		        # in this case we only need to update 'secondMax' to 'num'
		        secondMax = num
		return secondMax  # if '-1' then all elements are equal and there is no 2nd maximum.

# if duplicate is also allowed then just change the 'elif' condition.
# just don't check 'num != firstMax' 
class Solution: 
	def print2largest(self,arr, n):
		firstMax, secondMax = -1, -1  
		for num in arr:
		    if num > firstMax:
		        # 'num' is greatest number till now
		        # so in this we will have to update both 'firstMax' and 'secondMax'
		        # Update 'secondMax' to 'firstMax' and then 'firstMax' to cur 'num'.
		        secondMax = firstMax
		        firstMax  =  num
		    elif num > secondMax :  # No need to check 'num != firstMax' to allow duplicate 
		        # in this case we only need to update 'secondMax' to 'num'
		        secondMax = num
		return secondMax  # if '-1' then all elements are equal and there is no 2nd maximum.


# for 1st and 2nd distinct minimum.
# for duplicate remove the 'num != firstMin' from 'elif' condition like above(maximum).
class Solution: 
	def print2largest(self,arr, n):
		firstMin, secondMin = 10**5 + 1, 10**5 + 1 
		for num in arr:
		    if num < firstMin:
		        secondMin = firstMin
		        firstMin  =  num
		    elif num < secondMin and num != firstMin:  # checking num != firstMax to avoid duplicate
		        # in this case we only need to update 'secondMax' to 'num'
		        secondMin = num
		return firstMin # if '-1' then all elements are equal and there is no 2nd maximum.

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    // Find second maximum
    public int print2largest(int[] arr, int n) {
        int firstMax = -1, secondMax = -1;

        for (int num : arr) {
            if (num > firstMax) {
                secondMax = firstMax;
                firstMax = num;
            } else if (num > secondMax && num != firstMax) {
                secondMax = num;
            }
        }

        return secondMax;  // Returns -1 if all elements are equal (no second max)
    }
}
//Method 2
class Solution {
    // Allowing duplicates
    public int print2largest(int[] arr, int n) {
        int firstMax = -1, secondMax = -1;

        for (int num : arr) {
            if (num > firstMax) {
                secondMax = firstMax;
                firstMax = num;
            } else if (num > secondMax) {  // No need to check num != firstMax
                secondMax = num;
            }
        }

        return secondMax;  // Returns -1 if all elements are equal (no second max)
    }
}
//Method 3
class Solution {
    // Find first and second distinct minimum
    public int print2smallest(int[] arr, int n) {
        int firstMin = Integer.MAX_VALUE;
        int secondMin = Integer.MAX_VALUE;

        for (int num : arr) {
            if (num < firstMin) {
                secondMin = firstMin;
                firstMin = num;
            } else if (num < secondMin && num != firstMin) {  // Avoid duplicates
                secondMin = num;
            }
        }

        return secondMin;  // Returns -1 if no second minimum exists
    }
}
"""

# C++ Code 
"""
//Method 1
#include <vector>
#include <limits>

using namespace std;

class Solution {
public:
    //Find second maximum
    int print2largest(vector<int>& arr, int n) {
        int firstMax = -1, secondMax = -1;

        for (int num : arr) {
            if (num > firstMax) {
                // 'num' is greatest number till now
                secondMax = firstMax;
                firstMax = num;
            } else if (num > secondMax && num != firstMax) {
                // Update secondMax only if num isn't equal to firstMax
                secondMax = num;
            }
        }

        return secondMax;  // Returns -1 if all elements are equal (no second max)
    }
};
//Method 2
class Solution {
public:
    // Allowing duplicates
    int print2largest(vector<int>& arr, int n) {
        int firstMax = -1, secondMax = -1;

        for (int num : arr) {
            if (num > firstMax) {
                secondMax = firstMax;
                firstMax = num;
            } else if (num > secondMax) {  // No need to check num != firstMax
                secondMax = num;
            }
        }

        return secondMax;  // Returns -1 if all elements are equal (no second max)
    }
};
//Method 3
class Solution {
public:
    // Find first and second distinct minimum
    int print2smallest(vector<int>& arr, int n) {
        int firstMin = numeric_limits<int>::max();
        int secondMin = numeric_limits<int>::max();

        for (int num : arr) {
            if (num < firstMin) {
                secondMin = firstMin;
                firstMin = num;
            } else if (num < secondMin && num != firstMin) {  // Avoid duplicates
                secondMin = num;
            }
        }

        return secondMin;  // Returns -1 if no second minimum exists
    }
};
"""

# Now come to this question

# Q) why can't use heap?
# Because heap gives kth smallest/largest that come in sequence assuming sorted array, not the kth distinct smallest/largest.

# method 1: sort and check from last and count the distinct number you have seen till now.
# time: O(n*logn)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=2:
            return max(nums)
        nums.sort()
        count= 1
        for i in range(n-1, 0, -1):
            if nums[i]  != nums[i-1]:
                count += 1
                if count == 3:
                    return nums[i-1]
        return max(nums)


# method 2: Just extension of '2nd largest number' logic.
# code of '2nd largest' you can see at the bottom.
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax, secondMax , thirdMax= float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > firstMax:
                # here we need to update all three
                thirdMax = secondMax
                secondMax = firstMax
                firstMax  =  num
            elif num > secondMax and num != firstMax:
                # here we need to update two i.e thirdMax and secondMax
                thirdMax = secondMax
                secondMax = num
            elif num > thirdMax and num != firstMax and num != secondMax:  
                # not writing the condition 'num != firstMax' will give error in case like: [1,2,2,5,3,5], [1,1,1,1,1] etc.
                # # here we need to update only thirdMax
                thirdMax = num
        return thirdMax if thirdMax != float('-inf') else max(nums)

# method 3:
# Just the shorter version of above logic.
# Updating the variable at same condition only but we don't need to check that much extra cases 

# Note: We need to handle that many cases under if-else to handle duplicate numbers in above method.
# In this we are only updating if we are getting distinct number.
# Logic of if-else condition will be same after seeing distinct no.

# keep track of first_max, 2nd_max, 3rd_max after you each ele you see any distinct number.

# Note: we can apply this logic to find '2nd largest number also' in similar way.

# time: O(3* n), space: O(3)

class Solution(object):
    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]   # [first_max, second_max, third_max]
        for num in nums:
            if num not in v:  # wil check only for distinct number
                if num > v[0]:   v = [num, v[0], v[1]]  # make first= num, second= pre_first, third= pre_2nd
                elif num > v[1]: v = [v[0], num, v[1]]  # keep first same, make  second= num &  third= pre_2nd
                elif num > v[2]: v = [v[0], v[1], num]  # keep first & second same, & make third= num
        # return max(nums) if float('-inf') in v else v[2]
        return v[2] if v[2] != float('-inf') else v[0]

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    // Method 1: Sorting and Counting Distinct Elements
    public int thirdMax(int[] nums) {
        int n = nums.length;
        if (n <= 2) return Arrays.stream(nums).max().getAsInt();

        Arrays.sort(nums);
        int count = 1;

        for (int i = n - 1; i > 0; i--) {
            if (nums[i] != nums[i - 1]) {
                count++;
                if (count == 3) {
                    return nums[i - 1];
                }
            }
        }

        return Arrays.stream(nums).max().getAsInt();
    }
}
//Method 2
class Solution {
    // Method 2: Extension of Second Largest Logic
    public int thirdMax(int[] nums) {
        long firstMax = Long.MIN_VALUE, secondMax = Long.MIN_VALUE, thirdMax = Long.MIN_VALUE;

        for (int num : nums) {
            if (num > firstMax) {
                thirdMax = secondMax;
                secondMax = firstMax;
                firstMax = num;
            } else if (num > secondMax && num != firstMax) {
                thirdMax = secondMax;
                secondMax = num;
            } else if (num > thirdMax && num != firstMax && num != secondMax) {
                thirdMax = num;
            }
        }

        return (thirdMax == Long.MIN_VALUE) ? (int) firstMax : (int) thirdMax;
    }
}
//Method 3
import java.util.*;

class Solution {
    // Method 3: Tracking Distinct Maximums
    public int thirdMax(int[] nums) {
        long[] v = {Long.MIN_VALUE, Long.MIN_VALUE, Long.MIN_VALUE};  // [firstMax, secondMax, thirdMax]

        for (int num : nums) {
            if (Arrays.stream(v).noneMatch(val -> val == num)) {  // Only update for distinct numbers
                if (num > v[0]) v = new long[]{num, v[0], v[1]};
                else if (num > v[1]) v = new long[]{v[0], num, v[1]};
                else if (num > v[2]) v = new long[]{v[0], v[1], num};
            }
        }

        return (v[2] == Long.MIN_VALUE) ? (int) v[0] : (int) v[2];
    }
}
"""

# C++ Code 
"""
//Method 1
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

class Solution {
public:
    // Method 1: Sorting and Counting Distinct Elements
    int thirdMax(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) return *max_element(nums.begin(), nums.end());

        sort(nums.begin(), nums.end());
        int count = 1;

        for (int i = n - 1; i > 0; i--) {
            if (nums[i] != nums[i - 1]) {
                count++;
                if (count == 3) {
                    return nums[i - 1];
                }
            }
        }

        return *max_element(nums.begin(), nums.end());
    }
};
//Method 2
class Solution {
public:
    // Method 2: Extension of Second Largest Logic
    int thirdMax(vector<int>& nums) {
        long long firstMax = LLONG_MIN, secondMax = LLONG_MIN, thirdMax = LLONG_MIN;

        for (int num : nums) {
            if (num > firstMax) {
                thirdMax = secondMax;
                secondMax = firstMax;
                firstMax = num;
            } else if (num > secondMax && num != firstMax) {
                thirdMax = secondMax;
                secondMax = num;
            } else if (num > thirdMax && num != firstMax && num != secondMax) {
                thirdMax = num;
            }
        }

        return (thirdMax == LLONG_MIN) ? firstMax : thirdMax;
    }
};
//Method 3
class Solution {
public:
    // Method 3: Tracking Distinct Maximums
    int thirdMax(vector<int>& nums) {
        vector<long long> v = {LLONG_MIN, LLONG_MIN, LLONG_MIN};  // [firstMax, secondMax, thirdMax]

        for (int num : nums) {
            if (find(v.begin(), v.end(), num) == v.end()) {  // Only update for distinct numbers
                if (num > v[0]) v = {num, v[0], v[1]};
                else if (num > v[1]) v = {v[0], num, v[1]};
                else if (num > v[2]) v = {v[0], v[1], num};
            }
        }

        return (v[2] == LLONG_MIN) ? v[0] : v[2];
    }
};
"""

# Related q:
# 1) 2706. Buy Two Chocolates
