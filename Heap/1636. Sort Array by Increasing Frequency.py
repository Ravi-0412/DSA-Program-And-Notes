# method 1: 

# using min heap
# time: O(nlogn)
# but not able to break the tie for equal fre elements
import heapq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count= {}
        for num in nums:
            count[num]= 1+ count.get(num, 0)
        heap= []  
        # create a min heap with freq , key 
        for k,v in count.items():
            # add the num with negative sign to bring the num with larger value first in case of equal frequency
            heapq.heappush(heap,(v,-1*k))   
        # now add the ele into ans arr as many times they have occured(equal to their freq)
        ans= []
        while(len(heap)):
            temp = heapq.heappop(heap)
            for i in range(temp[0]):     # temp[0] will contain the fre of the ele
                ans.append(-1*temp[1])      # temp[1] will contain the ele
        return ans
    
# Shortcut of above method
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        # sorting nums
        # count[x] sorts by frequency, and if two values are equal, it will sort the keys in decreasing order.
        return sorted(nums, key=lambda x: (count[x], -x))  

# Java Code 
"""
import java.util.*;

public class Solution {
    public List<Integer> frequencySort(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);
        // create a min heap with freq , key 
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            // add the num with negative sign to bring the num with larger value first in case of equal frequency
            heap.add(new int[]{entry.getValue(), -1 * entry.getKey()});
        }
        // now add the ele into ans arr as many times they have occured(equal to their freq)
        List<Integer> ans = new ArrayList<>();
        while (!heap.isEmpty()) {
            int[] temp = heap.poll();
            for (int i = 0; i < temp[0]; i++) {     // temp[0] will contain the fre of the ele
                ans.add(-1 * temp[1]);      // temp[1] will contain the ele
            }
        }
        return ans;
    }

    // Shortcut of above method
    public List<Integer> frequencySortShortcut(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) count.put(num, count.getOrDefault(num, 0) + 1);
        // sorting nums
        // count[x] sorts by frequency, and if two values are equal, it will sort the keys in decreasing order.
        List<Integer> list = new ArrayList<>();
        for (int num : nums) list.add(num);
        list.sort((a, b) -> count.get(a) == count.get(b) ? b - a : count.get(a) - count.get(b));
        return list;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>

class Solution {
public:
    std::vector<int> frequencySort(std::vector<int>& nums) {
        std::unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        using pii = std::pair<int, int>;
        auto cmp = [](const pii& a, const pii& b) {
            return a.first == b.first ? b.second < a.second : a.first > b.first;
        };
        std::priority_queue<pii, std::vector<pii>, decltype(cmp)> heap(cmp);
        // create a min heap with freq , key 
        for (const auto& [k, v] : count) {
            // add the num with negative sign to bring the num with larger value first in case of equal frequency
            heap.push({v, -1 * k});
        }
        // now add the ele into ans arr as many times they have occured(equal to their freq)
        std::vector<int> ans;
        while (!heap.empty()) {
            auto temp = heap.top();
            heap.pop();
            for (int i = 0; i < temp.first; ++i) {     // temp[0] will contain the fre of the ele
                ans.push_back(-1 * temp.second);      // temp[1] will contain the ele
            }
        }
        return ans;
    }

    // Shortcut of above method
    std::vector<int> frequencySortShortcut(std::vector<int>& nums) {
        std::unordered_map<int, int> count;
        for (int num : nums) count[num]++;
        // sorting nums
        // count[x] sorts by frequency, and if two values are equal, it will sort the keys in decreasing order.
        std::sort(nums.begin(), nums.end(), [&](int a, int b) {
            return count[a] == count[b] ? b < a : count[a] < count[b];
        });
        return nums;
    }
};
"""

# method 2: can be optimised to O(n) using bucket sort
# Try later

