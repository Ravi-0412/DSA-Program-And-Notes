# Logic:
"""
just find the minimum prefix sum.
Then for ans : if min_sum = 0 return 1 else return abs(min_sum) + 1
"""

# java
"""
public int minStartValue(int[] nums) {
    int sum = 0, min_sum = 0;
    for (var n : nums) {
        sum += n;
        min_sum = Math.min(min_sum, sum);
    }
    return 1 - min_sum;   // will handle both the cases  
}
"""