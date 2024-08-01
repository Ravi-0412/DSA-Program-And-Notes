# 
""""
class Solution {
    public int findFinalValue(int[] nums, int original) {
        boolean[] m = new boolean[1001]; // Boolean array to mark the presence of numbers
        // Mark the presence of numbers in the nums array
        for (int num : nums) {
            m[num] = true;
        }
        // Double the original value while it is present in the array
        while (original <= 1000 && m[original]) {
            original *= 2;
        }
        return original; // Return the final value of original
    }
}
"""

# method 2:
""""
import java.util.HashSet;

class Solution {
    public int findFinalValue(int[] nums, int original) {
        HashSet<Integer> set = new HashSet<>();
        // Add all elements from nums to the set
        for (int num : nums) {
            set.add(num);
        }
        // Double the original value as long as it's found in the set
        while (set.contains(original)) {
            original *= 2;
        }
        return original;
    }
"""