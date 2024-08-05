# 1st method: brute force(two nested loops)

# 2nd method: using dictionary 
# time: O(n), space: O(n)
# logic: for every ele, find the remaining sum then 
# check the remaining sum is present in the hashamp or not 
# if remaining sum is already present in the dictionary return its value 
# if not present then add the current ele into hashmap with its index
def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}
        for i in range(len(nums)):
            rem_sum= target- nums[i]  # search for rem_sum in dictionary
            # searching will take O(1)
            if rem_sum in hashmap:  # if present then return the ans
                return hashmap[rem_sum], i  
            else:  # if not present then store the array val as key with index as values
                hashmap[nums[i]]= i   # since we have to return index so store index as value with remaining sum

# Now if asked to find the no of such pair then keep track of count as well.
# see 1st method of q: "2006. Count Number of Pairs With Absolute Difference K"


# 1) Note vvi: whenever you are asked to check the pair or count the pair for any operation 
# like 'Sum' ,'Subtraction' , 'multiplication' , 'division'
# think of 'Two sum' logic only like how you can get the 2nd number using 1st one. 
# Another number we will get by complement of 1st according to the behaviour of operator.

# Note: In case of pair count always store the frequency.
# You can traverse and check for pair in parallel.

# 2) Note: Store 'what you need to find(for pair i.e by help of which you will get one of ans) as key' and 
# 'what you need in ans(or due to which you can get the ans after some operation) as value' in hashmap.
# e.g: "in Two sum Q", we want to check remaining sum(another number) so kept this as 'key' and
# in ans we wanted the index so kept 'index' as value.

# It will help in lot of Q like : "2006. Count Number of Pairs With Absolute Difference K",
#  "1679. Max Number of K-Sum Pairs", "2183. Count Array Pairs Divisible by K" etc...

# 3) Note: whenever you have to find the subarray length or count of subarray with given sum 'k' or
#  given xor 'k' or related to nay operation. => Apply two sum logic.
# since "+" has complement "-" i.e given a sum say 'target' then say till any index 'j' totalSum= curSum 
# then if we can find any ele 'x' at index 'i' having such that x= curSum - target,  
# then we can get  the target by doing sum of all ele from index 'i+1' to 'j'.

# same way xor work because of its property : if res= a^b then res^a= b and res^b= a.
# replace res->curSum , b= target then if we will find 'a' such that a= res ^ b then means we can get the target 'b'.

# e.g : "523. Continuous Subarray Sum" , "974. Subarray Sums Divisible by K" , 
# "Longest Sub-Array with Sum K" ,"Smallest Subarray with Sum K",
# "560. Subarray Sum Equals K", "Count Subarrays with Given XOR"  etc....



# Extension:
# q)  If had asked count no of such pair then,
# In parallel we have to store the frequency and will check for ans.

class Solution:
    def getPairsCount(self, arr, n, k):
        unordered_map = {}
        count = 0
        for i in range(n):
            if k - arr[i] in unordered_map:
                count += unordered_map[k - arr[i]]
            if arr[i] in unordered_map:
                unordered_map[arr[i]] += 1
            else:
                unordered_map[arr[i]] = 1
        return count


# Note: First counting the frequency and then calculating the sum will give wrong ans.
# Must be >= expected one because there will be a lot of duplicates ans and unnecessary pair.

# e.g: k = 10, arr = [1 5 5 5 5 7]
# this will give count = 16 but should be '6' only.
# Here same index will also get counted in ans with a lot of duplicates one.

from collections import Counter
class Solution:
    def getPairsCount(self, arr, n, k):
        unordered_map = Counter(arr)
        count = 0
        for i in range(n):
            if k - arr[i] in unordered_map:
                count += unordered_map[k - arr[i]]
        return count


# Realted Q:
# 1) 2441. Largest Positive Integer That Exists With Its Negative
class Solution:
    def findMaxK(self, nums):
        visited = set()
        ans = -1
        for num in nums:
            if -1*num in visited:
                if abs(num) > ans:   # taking abs because we don't know whether this num is positive or negative.
                    ans = abs(num)
            visited.add(num)
        return ans 

# Java: Two sum
"""
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (numMap.containsKey(complement)) {
                return new int[]{numMap.get(complement), i};
            }
            numMap.put(nums[i], i);
        }

        return new int[]{}; // No solution found
    }
}
"""

# Related Question:
# 1) 2006. Count Number of Pairs With Absolute Difference K
# 2) Print all unique pairs with given sum
# 3) 167. Two Sum II - Input Array Is Sorted
