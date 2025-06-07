# Just same as :"560. Subarray Sum Equals K"


# method 2: 
# logic: whenever you see '0' decr the count, when you see '1' incr the count.
# when at any index you see the same value of count before means 
# you have found one of the subarray from last seen same count value to current index.

# time= space= O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count= 0   # if num== 0,  decr count by '1' by and if num== 1 incr count by '1'.
        maxLen= 0  # to handle the case when all num is either '0' or '1' only.   maxLen= float('-inf') will give '-inf' onlyin such case
        hashmap= {0: -1}   # [count: index]. initialising to handle the case when at any index count= 0 means from start to till that index we can get one of the ans.
        for i in range(len(nums)):
            if nums[i]== 0:
                count-= 1
            else:   #  nums[i]== 1
                count+= 1
            if count in hashmap:   # since we got duplicate of 'count'. so in between these two count must be '0' only then only we can get same count.
                maxLen= max(maxLen, i- hashmap[count])
            else:
                hashmap[count]= i
        return maxLen

# Note: we can apply exactly same logic(even same code) in Q asking : 
# 1) "longest substring/subarray having equal no of count of both when each ele can be of two type only".
# 2) "Find the max length of substring having equal no of lowercase and uppercase letter".

# Java Code 
"""
import java.util.*;

class Solution {
    public int findMaxLength(int[] nums) {
        int count = 0;  // if num == 0, decrease count by '1', and if num == 1, increase count by '1'.
        int maxLen = 0;  // to handle the case when all nums are either '0' or '1' only.
        Map<Integer, Integer> hashmap = new HashMap<>();
        hashmap.put(0, -1);  // [count: index], initializing to handle the case when at any index count == 0, meaning the subarray from start to that index is valid.

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                count--;
            } else {  // nums[i] == 1
                count++;
            }

            if (hashmap.containsKey(count)) {  
                // Since we got a duplicate count, the sum between these two indices must be zero, meaning a valid subarray.
                maxLen = Math.max(maxLen, i - hashmap.get(count));
            } else {
                hashmap.put(count, i);  // Store the first occurrence of this count.
            }
        }
        return maxLen;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int count = 0;  // if num == 0, decrease count by '1', and if num == 1, increase count by '1'.
        int maxLen = 0;  // to handle the case when all nums are either '0' or '1' only.
        unordered_map<int, int> hashmap = {{0, -1}};  // [count: index], initializing to handle the case when at any index count == 0, meaning the subarray from start to that index is valid.

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                count--;
            } else {  // nums[i] == 1
                count++;
            }

            if (hashmap.find(count) != hashmap.end()) {  
                // Since we got a duplicate count, the sum between these two indices must be zero, meaning a valid subarray.
                maxLen = max(maxLen, i - hashmap[count]);
            } else {
                hashmap[count] = i;  // Store the first occurrence of this count.
            }
        }
        return maxLen;
    }
};
"""