# Method 1: Marking visited in input array only.
# Logic: when you see any number nums[i] then, mark it as visited by making 
# value at index 'nums[i]' as negative i.e nums[nums[i]] = - nums[nums[i]]. it means we have seen 'nums[i]'.
# So for each element nums[i], check if we have already visited 'nums[i]' by checking if 'nums[nums[i]] < 0'.
# if negative then nums[i] is our ans.

# When can we apply this logic?
# when value of array element lies in range '0' to 'n-1' i.e 0 <= nums[i] <= n - 1 . n = len(array)
# Then we can mark visited in same array only.
class Solution(object):
    def findDuplicate(self, nums):
        for i  in range(len(nums)):    
            ind = abs(nums[i])  # nums[i] can be negative so make it +ve first to check at its index
            if nums[ind] < 0:
                # means we have visited 'nums[i]' before so return abs(nums[i]) as nums[i] can be negative also
                return abs(nums[i])
            nums[ind] = -nums[ind]    # nums[nums[i]] = - nums[nums[i]] will give wrong and because 'nums[i]' can be negative
                                      # e.g: [1, 2, 2]
        return 1

# Method 2: 

# here that number can repeat any no of times
# time: O(n), space: O(1)
# logic: sb number ko pointer mano, like index 1 pe jo number h usko kahan point karna chahiye apne value ke anusar(kis index pe)
# diagram banao like: 'i' index pe kon sa number h say 'x' then 'x' should point to number sitting on index 'i' ,
# isi tarah se diagram banao
# finally ek linklist jaisa banega diagram or jo number repeat ho rha hoga wahan pe more than one pointer hoga
# (you will get that number directly).

# since only 'n' different number is kept as 'n+1' location then there must be atleast one no repeaetd and there must be a cycle.

# Note: now this Q reduces to , find the starting node in a cyclic linklist that will be the ans.

# for this , 1) first find the intersection point of slow and fast pointer 
# 2) now take one pointer from start say as 'slow2' and move 'slow' and 'slow2' one step ahead till they meet 
# 3) the node at which they will meet will be the starting node of the cycle

# Note: the distance of 'node at which cycle start' from start and from the node where 'slow' and 'fast' has intersected will be always same
# always keep in mind the above things

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find whether cycle exist or not , but here it will exist for sure
        # for this , find the intersection point of  slow and fast
        slow, fast= 0, 0  # we have to start with number from index '0' only
        while True:
            slow= nums[slow]
            fast= nums[nums[fast]]   # we have to incremenet fast two times so wrote like this
            if fast== slow:
                break
        # now find the starting node of the cycle
        slow1= 0
        while True:
            slow= nums[slow]
            slow2= nums[slow2]
            if slow== slow1:
                return slow


# java
"""
// method 1:
class Solution {
    public int findDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]);
            if (nums[index] < 0) {
                return index;
            }
            nums[index] = -nums[index];
        }
        return 1;  // only for sake for returning int
    }
}


// Method 2:

class Solution {
    public int findDuplicate(int[] nums) {
        // find whether cycle exist or not , but here it will exist for sure
        // for this , find the intersection point of  slow and fast
        int slow = 0, fast = 0;
        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];   // we have to increment fast two times so wrote like this
            if (fast == slow) {
                break;
            }
        }
        // now find the starting node of the cycle
        slow = 0;
        while (true) {
            slow = nums[slow];
            fast = nums[fast];
            if (slow == fast) {
                return slow;
            }
        }
    }
}


"""