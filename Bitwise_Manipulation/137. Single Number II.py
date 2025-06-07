# store in dictionary and count the value 
# time: o(n), space= o(n)
# submitted on GFG
class Solution:
    def singleElement(self, arr, N):
        hashmap= {}
        for num in arr:
            if num not in hashmap:
                hashmap[num]= 1
            else:
                hashmap[num]+= 1
        for i in range(N):
            if hashmap[arr[i]]!=3:
                return arr[i]


# method 2: (submitted on GFG): Good one
# Logic: find the 3*(sum of all distinct no) - sum(array)
# after this you will left with 2*missing_number
# so now divide it by two
#  and we can get sum of all distinct no by storing in set

# this is valid for all this type of problem for every frequency

# time: O(n), space: O(n)

class Solution:
    def singleElement(self,arr, N):
        return (3*sum(set(arr))-sum(arr))//2


# method 3: submitted on Leetcode
# using 'Counter' object
# counter counts  fre of all the obj in a list,tuple
# internally it creates a dictionary only
# time: n, space: n
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency= Counter(nums) # a dictionary will be created storing
                                 # the fre of each ele
        for i in frequency:
            if frequency[i]==1:
                return i

# method 4 vvi: find the sum of set bits at all the positions and divide by 3
# if sum of set bits at that position is not divisible by 3 then it means the single number has set bit at that position.
# time: O(32* n)

# Note vvi: This method will work only for positive number in case of python.
# Detailed explanation in notes, page : 137

def singleNumber(self, nums: List[int]) -> int:
        ans= 0
        for i in range(32): # since max bits in any number can be 32
            check_set= 1<< i   # to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            no_set_bits = 0      
            for num in nums:
                if num & check_set:  # if 1 then 
                    no_set_bits += 1    # add to the set_bit
            # now check whether sum of set bits at that position is divisible by 3 or not
            if no_set_bits %3!= 0:      
                # update the ans
                ans= ans | check_set   # put '1' at ith position in the ans keeping other bit same in ans.
        return ans


# Method 4.1 : Same above method that will work in case of both negative and positive numbers.
# Analyse this properly 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans= 0
        for i in range(32): # since max bits in any number can be 32
            check_set= 1<< i   # to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            no_set_bits = 0      
            for num in nums:
                if num & check_set !=0:  # if 1 then 
                    no_set_bits += 1    # add to the set_bit
            # now check whether sum of set bits at that position is divisible by 3 or not
            if no_set_bits %3 == 1:      
                # update the ans
                ans= ans | check_set   # put '1' at ith position in the ans keeping other bit zero
        # print(ans, ~ans + 1 , (~ans + 1) & 0xffffffff)
        # print(0xffffffff)
        isPositive = (ans >> 31)  & 1 == 0
        return ans if isPositive else -((~ans + 1) & 0xffffffff)

# method 4.2: 
# Better & easier one than 4.1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans= 0
        for i in range(32): # since max bits in any number can be 32
            check_set= 1<< i   # to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            no_set_bits = 0      
            for num in nums:
                if num & check_set !=0:  # if 1 then 
                    no_set_bits += 1    # add to the set_bit
            # now check whether sum of set bits at that position is divisible by 3 or not
            if no_set_bits %3 == 1:      
                # update the ans
                ans= ans | check_set   # put '1' at ith position in the ans keeping other bit zero
        if ans <= 2**31 - 1:  # in 2's complement notation, +ve number can have value representation till 2**(n-1) -1.
            # Means ans is +ve number then only we can get ans less than this
            return ans
        # if negative then just find the positive value and return with '-ve' sign to get the actual number.
        return -(2**32 - ans)

# method 5 vvi: needs a lot of thinking but better method

# This Q was made for checking this method only.
# time: O(n)

# logic:  Page no: 141

# when any ele will occur three times then twos and ones wil be '0' for that number.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos= 0, 0
        for num in nums:
            ones= (ones ^ num) & ~twos
            twos= (twos ^ num) & ~ones
        return ones


# if we would have to return the number the single number that appear two and 
# all other appear three times then simply we would have returned 'two' in above logic.

# Java Code
"""
//Method 1: Using HashMap (O(n) time, O(n) space)
import java.util.HashMap;

class Solution {
    public int singleElement(int[] arr, int N) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();

        for (int num : arr) {
            hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
        }

        for (int i = 0; i < N; i++) {
            if (hashmap.get(arr[i]) != 3) {
                return arr[i];
            }
        }

        return 0; // If no single element found
    }
}
//Method 2: Using Sum Formula (O(n) time, O(n) space)
import java.util.HashSet;

class Solution {
    public int singleElement(int[] arr, int N) {
        HashSet<Integer> unique = new HashSet<>();
        int sumUnique = 0, sumAll = 0;

        for (int num : arr) {
            unique.add(num);
            sumAll += num;
        }

        for (int num : unique) {
            sumUnique += num;
        }

        return (3 * sumUnique - sumAll) / 2;
    }
}
//Method 3: Using Counter Equivalent (O(n) time, O(n) space)
import java.util.HashMap;

class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> frequency = new HashMap<>();

        for (int num : nums) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }

        for (int key : frequency.keySet()) {
            if (frequency.get(key) == 1) {
                return key;
            }
        }

        return 0;
    }
}
//Method 4: Using Bitwise Sum of Set Bits (O(32 * n) time, O(1) space)
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;

        for (int i = 0; i < 32; i++) {
            int check_set = 1 << i; // Checking ith bit position
            int noSetBits = 0;

            for (int num : nums) {
                if ((num & check_set) != 0) { // If set
                    noSetBits++;
                }
            }

            if (noSetBits % 3 != 0) { // If not divisible by 3
                ans |= check_set; // Set the bit in result
            }
        }

        if (ans <= (1 << 31) - 1) {
            return ans;
        }
        return -(1 << 32 - ans);
    }
}
"""

# C++ Code
"""
//Method 1: Using HashMap (O(n) time, O(n) space)
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int singleElement(vector<int>& arr, int N) {
        unordered_map<int, int> hashmap;

        for (int num : arr) {
            hashmap[num]++;
        }

        for (int i = 0; i < N; i++) {
            if (hashmap[arr[i]] != 3) {
                return arr[i];
            }
        }

        return 0; // If no single element found
    }
};
//Method 2: Using Sum Formula (O(n) time, O(n) space)
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int singleElement(vector<int>& arr, int N) {
        unordered_set<int> unique(arr.begin(), arr.end());
        int sumUnique = 0, sumAll = 0;

        for (int num : unique) sumUnique += num;
        for (int num : arr) sumAll += num;

        return (3 * sumUnique - sumAll) / 2;
    }
};
//Method 3: Using Counter Equivalent (O(n) time, O(n) space)
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> frequency;

        for (int num : nums) {
            frequency[num]++;
        }

        for (auto& pair : frequency) {
            if (pair.second == 1) {
                return pair.first;
            }
        }

        return 0;
    }
};
//Method 4: Using Bitwise Sum of Set Bits (O(32 * n) time, O(1) space)
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            int check_set = 1 << i; // Checking ith bit position
            int no_set_bits = 0;

            for (int num : nums) {
                if (num & check_set) { // If set
                    no_set_bits++;
                }
            }

            if (no_set_bits % 3 != 0) { // If not divisible by 3
                ans |= check_set; // Set the bit in result
            }
        }

        return ans;
    }
};
"""

