# Note vvi: There can be exactly one majority ele.

# method 1:
# time = space = O(n)
class Solution:
    def majorityElement(self, A, N):
        middle_index= N//2
        hashmap={}
        for i in A:
            if i not in hashmap:  # searches for 'i' in keys of dictionary
                                  # not in values
                hashmap[i] = 1
            else:
                hashmap[i] +=1
        for key,value in hashmap.items():
            if value > middle_index:
                return key
        return -1

# Method 2: 

# if given majority elements always exist and array is sorted
# in this case middle index must be the index of majority element
# in this case, time: O(1), just return the middle ele 

# but here we are sorting then returning the mid ele so,
#  time: 0(nlogn), space  = O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


# Method 3: Better one and Q is based on this only.

# Algo: (Moore’s Voting Algorithm)
# Just you have to find the winner on election.(No chance of draw)

# basic meaning: just cancel each other vote.
# it gives the majority ele i.e that has occured more than n/2 times
# by balancing the count i.e after seeing any other element, it 
# decreases the count if count is zero and  'm' is not equal to the current element.
# at alst 'm' will give the majority element

# note vvi: only valid for majority ele if they occur for sure. will not give the ele which has occured maximum no of times
# if the max_fre ele occur at the start then count will get decrement to '0' later and 'm' will have different ele at last
# then will give incorrect ans 

# Time: O(n) , space : O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)
        cnt=0
        m= None     # m storing elements with maximum frequency ele till any index
        for i in range(n):
            if cnt==0:  # only update the m when count= 0 because if count!= 0 then it means m is the most occuring ele till that index
                m= nums[i]  
                cnt+= 1
            else:
                if nums[i] == m:  # if m and array ele is same then increase the count by 1 
                    cnt+= 1
                else:  # else decrease the count by 1
                    cnt-= 1
        return m


# Method 4: Better one to write the 'Moore’s Voting Algorithm' in other way
# on this approach, we can solve the Q :"229. Majority Element II".

# Just relate to real life counting of votes in ele i.e how a condidate wins.
# Time: O(n) , space : O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = None  
        count = 0   
        for n in nums:
            if n == m:
                # vote of majority ele will increase.
                count += 1
            # Agar majority 'm' nhi h and count = 0 h then cur ele majority ban jayega.
            elif count == 0:
                # cur ele will become majority ele (current winning condidate)
                m , count = n, 1
            # # Agar majority 'm' nhi h and count > 0 h then 'm' ka count kamega.
            else:  # count > 0
                # cur ele can't be the winning condidate, it will just reduce the vote of cur winning condidate i.e cur majority ele
                count -= 1
        return m

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    // Method 1: Using HashMap
    public int majorityElement(int[] nums) {
        int middle_index = nums.length / 2;
        Map<Integer, Integer> hashmap = new HashMap<>();

        for (int num : nums) {
            hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) {
            if (entry.getValue() > middle_index) {
                return entry.getKey();
            }
        }

        return -1;
    }
}

//Method 2
import java.util.*;

class Solution {
    // Method 2: Sorting and taking the middle index
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
}

//Method 3
class Solution {
    // Method 3: Moore’s Voting Algorithm
    public int majorityElement(int[] nums) {
        int cnt = 0, m = 0;
        for (int num : nums) {
            if (cnt == 0) {
                m = num;
                cnt++;
            } else {
                cnt += (num == m) ? 1 : -1;
            }
        }
        return m;
    }
}

// Method 4
class Solution {
    public int majorityElement(int[] nums) {
        Integer m = null;
        int count = 0;

        for (int n : nums) {
            if (n == m) {
                // vote of majority ele will increase.
                count += 1;
            }
            // Agar majority 'm' nhi h and count = 0 h then cur ele majority ban jayega.
            else if (count == 0) {
                // cur ele will become majority ele (current winning condidate)
                m = n;
                count = 1;
            }
            // Agar majority 'm' nhi h and count > 0 h then 'm' ka count kamega.
            else {
                // cur ele can't be the winning condidate, it will just reduce the vote of cur winning condidate i.e cur majority ele
                count -= 1;
            }
        }
        return m;
    }
}

"""

# C++ Code 
"""
//Method 1
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Method 1: Using HashMap
    int majorityElement(vector<int>& nums) {
        int middle_index = nums.size() / 2;
        unordered_map<int, int> hashmap;

        for (int num : nums) {
            hashmap[num]++;
        }

        for (const auto& entry : hashmap) {
            if (entry.second > middle_index) {
                return entry.first;
            }
        }

        return -1;
    }
};

//Method 2
class Solution {
public:
    // Method 2: Sorting and taking the middle index
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums[nums.size() / 2];
    }
};

//Method 3
class Solution {
public:
    // Method 3: Moore’s Voting Algorithm
    int majorityElement(vector<int>& nums) {
        int cnt = 0, m = 0;
        for (int num : nums) {
            if (cnt == 0) {
                m = num;
                cnt++;
            } else {
                cnt += (num == m) ? 1 : -1;
            }
        }
        return m;
    }
};

// method 4:
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int m = 0;
        int count = 0;

        for (int n : nums) {
            if (n == m) {
                // vote of majority ele will increase.
                count += 1;
            }
            // Agar majority 'm' nhi h and count = 0 h then cur ele majority ban jayega.
            else if (count == 0) {
                // cur ele will become majority ele (current winning condidate)
                m = n;
                count = 1;
            }
            // Agar majority 'm' nhi h and count > 0 h then 'm' ka count kamega.
            else {
                // cur ele can't be the winning condidate, it will just reduce the vote of cur winning condidate i.e cur majority ele
                count -= 1;
            }
        }
        return m;
    }
};


"""