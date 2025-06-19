# method 1: 
# use hashmap to store count.
# now traverse the number from 1 to n and check if it presentor not and if present what is its count.
# time= space: O(n)

from typing import List
from collections import defaultdict

class Solution:
    def repeatedNumber(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        n = len(nums)
        A = B = -1

        # Count occurrences
        for num in nums:
            count[num] += 1

        # Check from 1 to n for duplicate and missing
        for i in range(1, n + 1):
            if count[i] == 2:
                A = i
            elif count[i] == 0:
                B = i

        return [A, B]

# Java Code 
"""
import java.util.*;

class Solution {
    public List<Integer> repeatedNumber(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        int n = nums.length;
        int A = -1, B = -1;

        // Count occurrences
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Check from 1 to n for duplicate and missing
        for (int i = 1; i <= n; i++) {
            if (count.getOrDefault(i, 0) == 2) {
                A = i;
            } else if (count.getOrDefault(i, 0) == 0) {
                B = i;
            }
        }

        return Arrays.asList(A, B);
    }
}

"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> repeatedNumber(vector<int>& nums) {
        unordered_map<int, int> count;
        int n = nums.size();
        int A = -1, B = -1;

        // Count occurrences
        for (int num : nums) {
            count[num]++;
        }

        // Check from 1 to n for duplicate and missing
        for (int i = 1; i <= n; i++) {
            if (count[i] == 2) {
                A = i;
            } else if (count[i] == 0) {
                B = i;
            }
        }

        return {A, B};
    }
};

"""

# method 2: using maths
# time= O(n)
# space: O(1)
# Note: This may give overflow in langauges like java and c++. So best solution is method 3

def missingAndRepeating(arr, n):
    s= (n *(n+1))//2   # sum of number from 1 to n
    s2= (n * (n + 1) * (2 * n + 1)) // 6  # sum of squares of number from 1 to n.
    for num in arr:
        s-=  num
        s2-= num * num
    # now 's' will be left with 'missing- repeating'.   (1)
    # now 's2' will be left with 'missing^2- repeating^2'.  (2)
    # Solve these two equations. Then you will get the ans.
    missing=    (s2//s + s)//2   # using '1' and '2'
    repeating=  missing - s      # from '1'
    return [missing, repeating]

# Java Code 
"""
class Solution {
    public int[] missingAndRepeating(int[] arr, int n) {
        long s = (long)n * (n + 1) / 2;                         // sum of number from 1 to n
        long s2 = (long)n * (n + 1) * (2 * n + 1) / 6;          // sum of squares of number from 1 to n

        for (int num : arr) {
            s -= num;
            s2 -= (long)num * num;
        }

        // now 's' will be left with 'missing - repeating'. (1)
        // now 's2' will be left with 'missing^2 - repeating^2'. (2)
        long missing = (s2 / s + s) / 2;    // using '1' and '2'
        long repeating = missing - s;       // from '1'

        return new int[]{(int)missing, (int)repeating};
    }
}

"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> missingAndRepeating(vector<int>& arr, int n) {
        long long s = (long long)n * (n + 1) / 2;                   // sum of number from 1 to n
        long long s2 = (long long)n * (n + 1) * (2 * n + 1) / 6;    // sum of squares of number from 1 to n

        for (int num : arr) {
            s -= num;
            s2 -= (long long)num * num;
        }

        // now 's' will be left with 'missing - repeating'. (1)
        // now 's2' will be left with 'missing^2 - repeating^2'. (2)
        long long missing = (s2 / s + s) / 2;    // using '1' and '2'
        long long repeating = missing - s;       // from '1'

        return {(int)missing, (int)repeating};
    }
};

"""

# method 3: 
# Bitwise manipulation

# Logic: 1) If we find x1 => xor of all elements of array and x2 => xor from '1' to 'n'
# Now if we take xor of 'x1' and 'x2' then say 'xor_result = x1 ^ x2'then, 
# 'xor_result' will contain 'xor' of 'missing and repeating number'

# How?
# when we take xor of 'x1' and 'x2' then mising number will occur three time , repeating number will occur one time
# and all other number will occur two times.
# So after taking xor all number will get cancelled because of even no of occurence 
# and we will left with 'xor' of 'missing and repeating number'.

# 2) Now we have to segregate our ans from 'xor_result'.

# time: O(n), space: O(1)


class Solution:
    def repeatedNumber(self, A):
        n= len(A)
        x1= 0  # xor of all elements of array
        for num in A:
            x1= x1^ num
        x2= 0  # xor from '1' to 'n'
        for i in range(1, n+1):
            x2= x2^ i
        xor_result= x1^x2   # this will contain 'xor' of 'missing & repeating number'.
        # now we have to find our ans from the above xor.
        rightmost_set_bit= xor_result & (-xor_result)   # it is number whose only one bit is set.
        # separate the arr number into two buckets having bit set at rightmost bit of 'xor_result'.
        set, not_set= 0, 0
        for num in A:
            if rightmost_set_bit & num:
                set= set ^ num
            else:
                not_set= not_set ^ num
        # now add number from '1' to 'n' in these two buckets to separate the number.
        for num in range(1, n+1):
            if rightmost_set_bit & num:
                set= set ^ num
            else:
                not_set = not_set ^ num
        # our number will get stored in set and not_set
        # now to return the repeating number first then missing.
        if set in A:  # means repeating
            return [set, not_set]
        else:  # means not_set is repeating one
            return [not_set, set]

# Java Code 
"""
import java.util.*;

class Solution {
    public int[] repeatedNumber(int[] A) {
        int n = A.length;
        int x1 = 0;  // xor of all elements of array
        for (int num : A) {
            x1 = x1 ^ num;
        }
        int x2 = 0;  // xor from '1' to 'n'
        for (int i = 1; i <= n; i++) {
            x2 = x2 ^ i;
        }

        int xor_result = x1 ^ x2;  // this will contain 'xor' of 'missing & repeating number'

        // now we have to find our ans from the above xor.
        int rightmost_set_bit = xor_result & -xor_result;  // it is number whose only one bit is set.

        // separate the arr number into two buckets having bit set at rightmost bit of 'xor_result'.
        int set = 0, not_set = 0;
        for (int num : A) {
            if ((num & rightmost_set_bit) != 0) {
                set = set ^ num;
            } else {
                not_set = not_set ^ num;
            }
        }

        // now add number from '1' to 'n' in these two buckets to separate the number.
        for (int i = 1; i <= n; i++) {
            if ((i & rightmost_set_bit) != 0) {
                set = set ^ i;
            } else {
                not_set = not_set ^ i;
            }
        }

        // our number will get stored in set and not_set
        // now to return the repeating number first then missing.
        for (int num : A) {
            if (num == set) {
                return new int[]{set, not_set};
            }
        }
        return new int[]{not_set, set};
    }
}

"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> repeatedNumber(vector<int>& A) {
        int n = A.size();
        int x1 = 0;  // xor of all elements of array
        for (int num : A) {
            x1 ^= num;
        }
        int x2 = 0;  // xor from '1' to 'n'
        for (int i = 1; i <= n; i++) {
            x2 ^= i;
        }

        int xor_result = x1 ^ x2;  // this will contain 'xor' of 'missing & repeating number'

        // now we have to find our ans from the above xor.
        int rightmost_set_bit = xor_result & -xor_result;  // it is number whose only one bit is set.

        // separate the arr number into two buckets having bit set at rightmost bit of 'xor_result'.
        int set = 0, not_set = 0;
        for (int num : A) {
            if (num & rightmost_set_bit) {
                set ^= num;
            } else {
                not_set ^= num;
            }
        }

        // now add number from '1' to 'n' in these two buckets to separate the number.
        for (int i = 1; i <= n; i++) {
            if (i & rightmost_set_bit) {
                set ^= i;
            } else {
                not_set ^= i;
            }
        }

        // our number will get stored in set and not_set
        // now to return the repeating number first then missing.
        for (int num : A) {
            if (num == set) {
                return {set, not_set};
            }
        }
        return {not_set, set};
    }
};

"""
