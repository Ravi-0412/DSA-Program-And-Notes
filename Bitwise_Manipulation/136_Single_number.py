#submitted on leetcode ,Time: o(n), space: o(n)
def singlenumber(nums):
    hashmap= {}
    for i in nums:
        if i not in hashmap:
            hashmap[i]= 1
        else:
            hashmap[i]+= 1
    for key,value in hashmap.items():
        if(value%2!=0):
            return key
            break
    # return 0   #if many elements occur odd times or no elements occur odd times(for gfg)
nums = [4,1,2,1,2]
print(singlenumber(nums))

# method 2:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

# 3rd method: best one using XOR operation
# Time: o(n), space: o(1)
# logic: xor with any number itself is zero and xor of any number with zero is the number itself.
# so when we will take xor of all ele, we will be left with the 'single number' 
# because all will be pair so they will get cancel('0') automatically.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans= 0
        for num in nums:
            ans^= num
        return ans

# Java Code
"""
//Method 1
import java.util.HashMap;

class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();

        for (int num : nums) {
            hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
        }

        for (int key : hashmap.keySet()) {
            if (hashmap.get(key) % 2 != 0) {
                return key;
            }
        }

        return 0; // If no single element found
    }
}
//Method 2
import java.util.HashSet;

class Solution {
    public int singleNumber(int[] nums) {
        HashSet<Integer> unique = new HashSet<>();
        int sumUnique = 0, sumAll = 0;

        for (int num : nums) {
            unique.add(num);
            sumAll += num;
        }

        for (int num : unique) {
            sumUnique += num;
        }

        return 2 * sumUnique - sumAll;
    }
}
//Method 3
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int num : nums) {
            ans ^= num; // XOR cancels out all paired numbers, leaving only the unique one
        }
        return ans;
    }
}

"""

# C++ Code
"""
//Method 1
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int singleNumber(vector<int>& nums) {
    unordered_map<int, int> hashmap;

    for (int num : nums) {
        hashmap[num]++;
    }

    for (auto& pair : hashmap) {
        if (pair.second % 2 != 0) {
            return pair.first;
        }
    }

    return 0; // If no single element found
}

int main() {
    vector<int> nums = {4, 1, 2, 1, 2};
    cout << singleNumber(nums) << endl;
    return 0;
}
//Method 2
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int singleNumber(vector<int>& nums) {
    unordered_set<int> unique(nums.begin(), nums.end());
    int sumUnique = 0, sumAll = 0;
    
    for (int num : unique) sumUnique += num;
    for (int num : nums) sumAll += num;
    
    return 2 * sumUnique - sumAll;
}

int main() {
    vector<int> nums = {4, 1, 2, 1, 2};
    cout << singleNumber(nums) << endl;
    return 0;
}
//Method 3
#include <iostream>
#include <vector>

using namespace std;

int singleNumber(vector<int>& nums) {
    int ans = 0;
    for (int num : nums) {
        ans ^= num; // XOR cancels out all paired numbers, leaving only the unique one
    }
    return ans;
}

int main() {
    vector<int> nums = {4, 1, 2, 1, 2};
    cout << singleNumber(nums) << endl;
    return 0;
}
"""

        