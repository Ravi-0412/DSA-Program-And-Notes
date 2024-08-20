# Simplest way:
class Solution {
    public int findPairs(int[] nums, int k) {
        if (k < 0) return 0;
        Set<Integer> numbers = new HashSet<>();
        Set<Integer> found = new HashSet<>();
        for (int n : nums) {
            if (numbers.contains(n + k)) found.add(n);
            if (numbers.contains(n - k)) found.add(n - k);
            numbers.add(n);
        }
        return found.size();
    }
}

# Method 2: 

from collections import defaultdict

class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        
        map = defaultdict(int)
        result = 0
        
        for num in nums:
            if num in map:
                # if we have already processed i.e added the ans for 'num' 
                # then in this case we will add only when k == 0 
                if k == 0 and map[num] == 1:
                    result += 1
                map[num] += 1  # to avoid adding 'num' when 'num' will be already present
            else:
                # if we have not already processed then we will check for pair
                if (num - k) in map:
                    # positive case finding 1st ele
                    result += 1
                if (num + k) in map:
                    # negative case finding 1st ele
                    result += 1
                map[num] = 1
        
        return result


# java
"""
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findPairs(int[] nums, int k) {
        if (k < 0) {
            return 0;
        }
        Map<Integer, Integer> map = new HashMap<>();
        int result = 0;
        for (int num : nums) {
            if (map.containsKey(num)) {
                if (k == 0 && map.get(num) == 1) {
                    result++;
                }
                map.put(num, map.get(num) + 1);
            } else {
                if (map.containsKey(num - k)) {
                    result++;
                }
                if (map.containsKey(num + k)) {
                    result++;
                }
                map.put(num, 1);
            }
        }
        return result;
    }
}
"""

