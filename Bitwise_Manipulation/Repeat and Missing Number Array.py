# method 1: use hashmap to store count.
# now traverse the number from 1 to n and check if it presentor not and if present what is its count.
# time= space: O(n)


# method 2: using maths
# time= O(n)
# space: O(1)
# Note: This may give overflow in other language.
def missingAndRepeating(arr, n):
    s= (n *(n+1))//2   # sum of number from 1 to n
    s2= (n * (n + 1) * (2 * n + 1)) // 6  # sum of squares of number from 1 to n.
    for num in arr:
        s-=  num
        s2-= num * num
    # now 's' will be left with 'missing- repeating'.   (1)
    # now 's' will be left with 'missing^2- repeating^2'.  (2)
    # Solve these two equations. Then you will get the ans.
    missing=    (s2//s + s)//2   # using '1' and '2'
    repeating=  missing - s      # from '1'
    return [missing, repeating]


# method 3(Best): Bitwise 
# submitted on interview Bit

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
//Method 2
import java.util.*;

class Solution {
    public int[] missingAndRepeating(int[] arr, int n) {
        long s = (n * (n + 1)) / 2; // Sum of numbers from 1 to n
        long s2 = (n * (n + 1) * (2 * n + 1)) / 6; // Sum of squares of numbers from 1 to n

        for (int num : arr) {
            s -= num;
            s2 -= (long) num * num;
        }

        // Now 's' is left with 'missing - repeating' (Equation 1)
        // Now 's2' is left with 'missing^2 - repeating^2' (Equation 2)

        // Solve for missing and repeating
        int missing = (int) ((s2 / s + s) / 2); // Using Equation 1 and 2
        int repeating = missing - (int) s; // From Equation 1

        return new int[]{missing, repeating};
    }
}
//Method 3
import java.util.*;

class Solution {
    public int[] repeatedNumber(int[] A) {
        int n = A.length;
        int x1 = 0, x2 = 0;

        // XOR of all elements in array
        for (int num : A) {
            x1 ^= num;
        }

        // XOR of numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            x2 ^= i;
        }

        int xor_result = x1 ^ x2; // XOR of missing and repeating number

        // Find the rightmost set bit
        int rightmost_set_bit = xor_result & (-xor_result);

        int set = 0, not_set = 0;

        // Separate numbers into two groups
        for (int num : A) {
            if ((num & rightmost_set_bit) != 0)
                set ^= num;
            else
                not_set ^= num;
        }

        // Separate numbers from 1 to n into two groups
        for (int num = 1; num <= n; num++) {
            if ((num & rightmost_set_bit) != 0)
                set ^= num;
            else
                not_set ^= num;
        }

        // Determine the repeating and missing numbers
        boolean setExists = false;
        for (int num : A) {
            if (num == set) {
                setExists = true;
                break;
            }
        }

        if (setExists) // If 'set' is repeating
            return new int[]{set, not_set};
        else
            return new int[]{not_set, set};
    }
}
"""

# C++ Code 
"""
//Method 2
#include <iostream>
#include <vector>

using namespace std;

vector<int> missingAndRepeating(vector<int>& arr, int n) {
    long long s = (n * (n + 1)) / 2; // Sum of numbers from 1 to n
    long long s2 = (n * (n + 1) * (2 * n + 1)) / 6; // Sum of squares of numbers from 1 to n

    for (int num : arr) {
        s -= num;
        s2 -= (long long) num * num;
    }

    // Now 's' is left with 'missing - repeating' (Equation 1)
    // Now 's2' is left with 'missing^2 - repeating^2' (Equation 2)

    // Solve for missing and repeating
    int missing = (s2 / s + s) / 2; // Using Equation 1 and 2
    int repeating = missing - s; // From Equation 1

    return {missing, repeating};
}
//Method 3
#include <iostream>
#include <vector>

using namespace std;

vector<int> repeatedNumber(vector<int>& A) {
    int n = A.size();
    int x1 = 0, x2 = 0; 

    // XOR of all elements in array
    for (int num : A) {
        x1 ^= num;
    }

    // XOR of numbers from 1 to n
    for (int i = 1; i <= n; i++) {
        x2 ^= i;
    }

    int xor_result = x1 ^ x2; // XOR of missing and repeating number

    // Find the rightmost set bit
    int rightmost_set_bit = xor_result & (-xor_result);

    int set = 0, not_set = 0;

    // Separate numbers into two groups
    for (int num : A) {
        if (num & rightmost_set_bit)
            set ^= num;
        else
            not_set ^= num;
    }

    // Separate numbers from 1 to n into two groups
    for (int num = 1; num <= n; num++) {
        if (num & rightmost_set_bit)
            set ^= num;
        else
            not_set ^= num;
    }

    // Determine the repeating and missing numbers
    if (find(A.begin(), A.end(), set) != A.end()) // If 'set' is repeating
        return {set, not_set};
    else
        return {not_set, set};
}
"""