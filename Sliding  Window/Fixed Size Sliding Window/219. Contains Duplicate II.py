# Logic: 
"""
The front of the window is at i, the rear of the window is k steps back. The elements within that window 
are maintained using a Set. While adding new element to the set, if add() returns false, 
it means the element already exists in the set. At that point, we return true. 
If the control reaches out of for loop, it means that inner return true never executed, 
meaning no such duplicate element was found.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i in range(len(nums)):
            if i > k:
                seen.remove(nums[i - k - 1])  # Remove element if its distance to nums[i] is not less than k
            if nums[i] in seen:
                return True  # If nums[i] is already in the set, there's a duplicate within the distance k
            seen.add(nums[i])  # Add the current element to the set
        return False


# java
"""
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(i > k) set.remove(nums[i-k-1]); //remove element if its distance to nums[i] is not lesser than k
            if(!set.add(nums[i])) return true; //because all still existed elements is closer than k distance to the num[i], therefore if the add() return false, it means there's a same value element already existed within the distance k, therefore return true.
        }
        return false;
}
}
"""