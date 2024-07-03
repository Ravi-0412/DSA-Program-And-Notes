# Method 1: Using hashmap

# Time: O(M + N), where M <= 1000 is length of nums1 array, N <= 1000 is length of nums2 array.
# Space: O(min(M, N))

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
            
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans


# Method 2: Sorting + Two pointer
# Time: O(MlogM + NlogN), where M <= 1000 is length of nums1 array, N <= 1000 is length of nums2 array.
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans

# follow up:
# 1) 2nd method is best
# 2) 1st method is best
# 3) a) nums1 fits into the memory, we can use Approach 1 which stores all elements of nums1 in the HashMap. 
# Then, we can sequentially load and process nums2.
# b) If neither nums1 nor nums2 fits into the memory, we split the numeric range into numeric sub-ranges that fit into the memory.
# We modify Approach 1 to count only elements which belong to the given numeric sub-range.
# We process each numeric sub-ranges one by one, util we process all numeric sub-ranges.

# java
# Method 1: 
"""
import java.util.*;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return intersect(nums2, nums1);
        }
        
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int num : nums1) {
            cnt.put(num, cnt.getOrDefault(num, 0) + 1);
        }
        
        List<Integer> ans = new ArrayList<>();
        for (int num : nums2) {
            if (cnt.getOrDefault(num, 0) > 0) {
                ans.add(num);
                cnt.put(num, cnt.get(num) - 1);
            }
        }
        
        int[] result = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            result[i] = ans.get(i);
        }
        return result;
    }
}

"""

# Method 2:
"""
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        List<Integer> ans = new ArrayList<>();
        int i = 0, j = 0;
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] < nums2[j]) {
                i++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                ans.add(nums1[i]);
                i++;
                j++;
            }
        }
        
        int[] result = new int[ans.size()];
        for (int k = 0; k < ans.size(); k++) {
            result[k] = ans.get(k);
        }
        return result;
    }
}


"""