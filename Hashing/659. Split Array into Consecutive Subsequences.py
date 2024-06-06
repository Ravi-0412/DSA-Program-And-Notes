# Logic: check for each number whether we can add them to any sequence or not.
# Note: Sequence can start from current number or we can add current number to any of the previous sequence.
# if none of the two is possible then , ans = False

# How to solve?
# The algorithm takes two steps:

# 1) Iterate once through the array to get the number of occurrences for each number in the array. 
# Store this in a hashmap called occurrences mapping the number to its total # of occurrences.
# 2) Iterate once through the array to check if every element can be part of a consecutive sequence of at least length 3.

# The second part is the core of the algorithm. For an element to be part of a consecutive sequence, it has to either be:

# 1) Appendable to an existing sequence. For example, 5 is directly appendable to the sequence [1, 2, 3, 4]. 
# We keep track of this next number (5 in this example) in each of these sequences in a separate hashmap called next_nums.
# 2) Able to create its own sequence. For this to happen, 
# there must be at least 1 occurrence of that number + 1 and that number + 2, since that creates a sequence of length 3.

# The occurrences hashmap essentially acts as a "storage" for all the numbers, 
# and next_nums keeps track of what number can be directly appended to an existing sequence. 
# Once every number in the "storage" has been accounted for, 
# every number in the input array has been reallocated into a subsequence of at least length 3,
# so we return True. If at any point, a number cannot create its own subsequence 
# and cannot be added to an existing one, we return False.

# Time = Space = O(n)

class Solution(object):
    def isPossible(self, nums):
        from collections import defaultdict
        occurrences, next_nums = defaultdict(int), defaultdict(int)
        for num in nums:
            occurrences[num] += 1
        for num in nums:
            if occurrences[num] == 0:
                continue 
           # If next_nums contains the number, it is directly appendable to a sequence.
           # We "append" it to the sequence by incrementing the next number by 1.
            elif next_nums[num] > 0:
                next_nums[num] -= 1
                next_nums[num + 1] += 1
           # If the number + 1 and the number + 2 are both still in the occurrences hashmap,
           # We can create a new subsequence of length 3 and add the next number to next_nums.
            elif occurrences[num + 1] > 0 and occurrences[num + 2] > 0:
                occurrences[num + 1] -= 1
                occurrences[num + 2] -= 1
                next_nums[num + 3] += 1
            else:
                return False
            occurrences[num] -= 1
        return True

# Later try by heap also.

# Java
"""
import java.util.HashMap;

public class Solution {
    public boolean isPossible(int[] nums) {
        HashMap<Integer, Integer> occurrences = new HashMap<>();
        HashMap<Integer, Integer> nextNums = new HashMap<>();
        
        for (int num : nums) {
            occurrences.put(num, occurrences.getOrDefault(num, 0) + 1);
        }
        
        for (int num : nums) {
            if (occurrences.get(num) == 0) {
                continue;
            } else if (nextNums.getOrDefault(num, 0) > 0) {
                nextNums.put(num, nextNums.get(num) - 1);
                nextNums.put(num + 1, nextNums.getOrDefault(num + 1, 0) + 1);
            } else if (occurrences.getOrDefault(num + 1, 0) > 0 && occurrences.getOrDefault(num + 2, 0) > 0) {
                occurrences.put(num + 1, occurrences.get(num + 1) - 1);
                occurrences.put(num + 2, occurrences.get(num + 2) - 1);
                nextNums.put(num + 3, nextNums.getOrDefault(num + 3, 0) + 1);
            } else {
                return false;
            }
            occurrences.put(num, occurrences.get(num) - 1);
        }
        
        return true;
    }
}

"""

# Related q:
# 1) 1296. Divide Array in Sets of K Consecutive Numbers