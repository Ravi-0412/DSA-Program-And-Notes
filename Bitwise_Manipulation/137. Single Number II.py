# Method 1: 

# store in dictionary and count the value 
# time: o(n), space= o(n)
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
# Java Code 
"""
import java.util.*;

class Solution {
    public int singleElement(int[] arr, int N) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        for (int num : arr) {
            if (!hashmap.containsKey(num)) {
                hashmap.put(num, 1);
            } else {
                hashmap.put(num, hashmap.get(num) + 1);
            }
        }
        for (int i = 0; i < N; i++) {
            if (hashmap.get(arr[i]) != 3) {
                return arr[i];
            }
        }
        return -1;
    }
}

"""

# C++ Code 
"""
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int singleElement(vector<int>& arr, int N) {
        unordered_map<int, int> hashmap;
        for (int num : arr) {
            if (hashmap.find(num) == hashmap.end()) {
                hashmap[num] = 1;
            } else {
                hashmap[num]++;
            }
        }
        for (int i = 0; i < N; i++) {
            if (hashmap[arr[i]] != 3) {
                return arr[i];
            }
        }
        return -1;
    }
};

"""

# method 2: 
# Logic: find the 3*(sum of all distinct no) - sum(array)
# after this you will left with 2*missing_number
# so now divide it by two
#  and we can get sum of all distinct no by storing in set

# this is valid for all this type of problem for every frequency

# time: O(n), space: O(n)

class Solution:
    def singleElement(self,arr, N):
        return (3*sum(set(arr))-sum(arr))//2

# Java Code 
"""
import java.util.*;

class Solution {
    public int singleElement(int[] arr, int N) {
        Set<Integer> set = new HashSet<>();
        int sum = 0, setSum = 0;

        for (int num : arr) {
            sum += num;
            set.add(num);
        }

        for (int num : set) {
            setSum += num;
        }

        return (3 * setSum - sum) / 2;
    }
}

"""

# C++ Code 
"""
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    int singleElement(vector<int>& arr, int N) {
        unordered_set<int> set;
        int sum = 0, setSum = 0;

        for (int num : arr) {
            sum += num;
            set.insert(num);
        }

        for (int num : set) {
            setSum += num;
        }

        return (3 * setSum - sum) / 2;
    }
};

"""

# method 3: 
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
# Java Code 
"""
import java.util.*;

class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> frequency = new HashMap<>();  // a dictionary will be created storing
                                                             // the freq of each ele
        for (int num : nums) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }

        for (int key : frequency.keySet()) {
            if (frequency.get(key) == 1) {
                return key;
            }
        }

        return -1;  // fallback in case no single element found
    }
}

"""

# C++ Code 
"""
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> frequency;  // a dictionary will be created storing
                                            // the freq of each ele
        for (int num : nums) {
            frequency[num]++;
        }

        for (auto& pair : frequency) {
            if (pair.second == 1) {
                return pair.first;
            }
        }

        return -1;  // fallback in case no single element found
    }
};

"""
# method 4 :
# find the sum of set bits at all the positions and divide by 3
# if sum of set bits at that position is not divisible by 3 then it means the single number has set bit at that position.
# time: O(32* n)

# Note vvi: This method will work only for positive number in case of python.

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
# Java Code 
"""
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {  // since max bits in any number can be 32
            int check_set = 1 << i;     // to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            int no_set_bits = 0;
            for (int num : nums) {
                if ((num & check_set) != 0) {  // if 1 then
                    no_set_bits += 1;         // add to the set_bit
                }
            }
            // now check whether sum of set bits at that position is divisible by 3 or not
            if (no_set_bits % 3 != 0) {
                // update the ans
                ans = ans | check_set;  // put '1' at ith position in the ans keeping other bit same in ans.
            }
        }
        return ans;
    }
}

"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {  // since max bits in any number can be 32
            int check_set = 1 << i;     // to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            int no_set_bits = 0;
            for (int num : nums) {
                if (num & check_set) {  // if 1 then
                    no_set_bits += 1;   // add to the set_bit
                }
            }
            // now check whether sum of set bits at that position is divisible by 3 or not
            if (no_set_bits % 3 != 0) {
                // update the ans
                ans = ans | check_set;  // put '1' at ith position in the ans keeping other bit same in ans.
            }
        }
        return ans;
    }
};

"""

# Method 5 : 
# Same as method '4' that will work in case of both negative and positive numbers.
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
# Java Code 
"""
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {  // since max bits in any number can be 32
            int check_set = 1 << i;     // to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            int no_set_bits = 0;
            for (int num : nums) {
                if ((num & check_set) != 0) {  // if 1 then 
                    no_set_bits += 1;          // add to the set_bit
                }
            }
            // now check whether sum of set bits at that position is divisible by 3 or not
            if (no_set_bits % 3 == 1) {
                // update the ans
                ans = ans | check_set;  // put '1' at ith position in the ans keeping other bit zero
            }
        }

        // check sign bit (31st bit). If positive return as-is else convert to negative
        boolean isPositive = ((ans >> 31) & 1) == 0;
        return isPositive ? ans : -((~ans + 1) & 0xffffffff);
    }
}

"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {  // since max bits in any number can be 32
            int check_set = 1 << i;     // to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            int no_set_bits = 0;
            for (int num : nums) {
                if ((num & check_set) != 0) {  // if 1 then 
                    no_set_bits += 1;         // add to the set_bit
                }
            }
            // now check whether sum of set bits at that position is divisible by 3 or not
            if (no_set_bits % 3 == 1) {
                // update the ans
                ans = ans | check_set;  // put '1' at ith position in the ans keeping other bit zero
            }
        }

        // check sign bit (31st bit). If positive return as-is else convert to negative
        bool isPositive = ((ans >> 31) & 1) == 0;
        return isPositive ? ans : -((~ans + 1) & 0xffffffff);
    }
};

"""

# method 6: 
# Better & easier one than method 5

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

# method 6: 
# needs a lot of thinking but better method
# when any ele will occur three times then twos and ones wil be '0' for that number.
# This Q was made for checking this method only.
# time: O(n)

# Java Code 
"""
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {  // since max bits in any number can be 32
            int check_set = 1 << i;     // to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            int no_set_bits = 0;
            for (int num : nums) {
                if ((num & check_set) != 0) {  // if 1 then 
                    no_set_bits += 1;         // add to the set_bit
                }
            }
            // now check whether sum of set bits at that position is divisible by 3 or not
            if (no_set_bits % 3 == 1) {
                // update the ans
                ans = ans | check_set;  // put '1' at ith position in the ans keeping other bit zero
            }
        }

        if (ans <= (int)(Math.pow(2, 31) - 1)) {  // in 2's complement notation, +ve number can have value representation till 2**(n-1) -1.
            // Means ans is +ve number then only we can get ans less than this
            return ans;
        }

        // if negative then just find the positive value and return with '-ve' sign to get the actual number.
        return -(int)(Math.pow(2, 32) - ans);
    }
}

"""

# C++ Code 
"""
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {  // since max bits in any number can be 32
            int check_set = 1 << i;     // to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            int no_set_bits = 0;
            for (int num : nums) {
                if ((num & check_set) != 0) {  // if 1 then 
                    no_set_bits += 1;         // add to the set_bit
                }
            }
            // now check whether sum of set bits at that position is divisible by 3 or not
            if (no_set_bits % 3 == 1) {
                // update the ans
                ans = ans | check_set;  // put '1' at ith position in the ans keeping other bit zero
            }
        }

        if (ans <= (int)pow(2, 31) - 1) {  // in 2's complement notation, +ve number can have value representation till 2**(n-1) -1.
            // Means ans is +ve number then only we can get ans less than this
            return ans;
        }

        // if negative then just find the positive value and return with '-ve' sign to get the actual number.
        return -(int)((unsigned int)pow(2, 32) - ans);
    }
};

"""

"""
Note: if we would have to return the number the single number that appear two and 
all other appear three times then simply we would have returned 'two' in this method.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos= 0, 0
        for num in nums:
            ones= (ones ^ num) & ~twos
            twos= (twos ^ num) & ~ones
        return ones

# Java Code 
"""
class Solution {
    public int singleNumber(int[] nums) {
        int ones = 0, twos = 0;
        for (int num : nums) {
            ones = (ones ^ num) & ~twos;
            twos = (twos ^ num) & ~ones;
        }
        return ones;
    }
}

"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0, twos = 0;
        for (int num : nums) {
            ones = (ones ^ num) & ~twos;
            twos = (twos ^ num) & ~ones;
        }
        return ones;
    }
};

"""


