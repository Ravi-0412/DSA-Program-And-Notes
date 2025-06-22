# method 1: 
# Sort based on frequency
# time: O(n*logn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        # hashmap will map each ele with their respective frequency
        for num in nums:
            hashmap[num]= 1 + hashmap.get(num, 0)
        arr= sorted(hashmap, key= hashmap.get, reverse= True) 
                                # will sort the hashmap based on freq(value of hashmap) i.e key that we had provided 
                                # and will store the key wrt each value
        return arr[:k]

# Java Code 
"""
import java.util.*;

public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        // hashmap will map each ele with their respective frequency
        for (int num : nums) {
            hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
        }
        List<Integer> arr = new ArrayList<>(hashmap.keySet());
        arr.sort((a, b) -> hashmap.get(b) - hashmap.get(a));
        // will sort the hashmap based on freq(value of hashmap) i.e key that we had provided  
        // and will store the key wrt each value
        return arr.subList(0, k);
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> hashmap;
        // hashmap will map each ele with their respective frequency
        for (int num : nums) {
            hashmap[num]++;
        }
        std::vector<int> arr;
        for (auto& [key, _] : hashmap) {
            arr.push_back(key);
        }
        std::sort(arr.begin(), arr.end(), [&](int a, int b) {
            return hashmap[b] < hashmap[a];
        });
        // will sort the hashmap based on freq(value of hashmap) i.e key that we had provided  
        // and will store the key wrt each value
        return std::vector<int>(arr.begin(), arr.begin() + k);
    }
};
"""

# Method 2: 
# just make min heap with fre of each ele
# time: O(nlogk)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap, heap= {}, []
        # hashmap will map each ele with their respective frequency
        for num in nums:
            hashmap[num]= 1 + hashmap.get(num, 0)
            
        # now make a min heap with freq as first ele and key of dict as second ele
        # when we push more than one ele in heap, it create the min/max heap acc to the 1st ele(1st pushed ele)
        for ele in hashmap:
            heapq.heappush(heap, (hashmap[ele],ele))  # value and key is pushed
            if len(heap)>k:
                heapq.heappop(heap)
                
        # now you will be left with fre of k top ele with their key
        # now print the key of each remaining ele in heap
        ans= []
        for num in heap:
            ans.append(num[1])
        return ans

        # for printing the ele with most fre first
        # ans=[]
        # for i in range(len(heap)):
        #     temp= heapq.heappop(heap)
        #     ans.append(temp[1])      # will store the ele with least fre among k top frequent first
        # # print(ans)
        # return ans[::-1]    # now return the reverse of ans

# Java Code 
"""
import java.util.*;

public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        // hashmap will map each ele with their respective frequency
        for (int num : nums) {
            hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        // now make a min heap with freq as first ele and key of dict as second ele
        // when we push more than one ele in heap, it create the min/max heap acc to the 1st ele(1st pushed ele)

        for (int ele : hashmap.keySet()) {
            heap.add(new int[]{hashmap.get(ele), ele});  // value and key is pushed
            if (heap.size() > k) {
                heap.poll();
            }
        }

        // for printing the ele with most fre first
        List<Integer> ans = new ArrayList<>();
        while (!heap.isEmpty()) {
            int[] temp = heap.poll();
            ans.add(temp[1]);      // will store the ele with least fre among k top frequent first
        }
        Collections.reverse(ans);    // now return the reverse of ans
        return ans;
        // for printing the ele with most fre first
        // List<Integer> ans = new ArrayList<>();
        // for (int i = 0; i < heap.size(); i++) {
        //     int[] temp = heap.poll();
        //     ans.add(temp[1]);      // will store the ele with least fre among k top frequent first
        // }
        // System.out.println(ans);
        // Collections.reverse(ans);    // now return the reverse of ans
        // return ans;
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
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> hashmap;
        // hashmap will map each ele with their respective frequency
        for (int num : nums) {
            hashmap[num]++;
        }

        using pii = std::pair<int, int>;
        auto cmp = [](pii a, pii b) { return a.first > b.first; };
        std::priority_queue<pii, std::vector<pii>, decltype(cmp)> heap(cmp);
        // now make a min heap with freq as first ele and key of dict as second ele
        // when we push more than one ele in heap, it create the min/max heap acc to the 1st ele(1st pushed ele)

        for (const auto& [ele, freq] : hashmap) {
            heap.push({freq, ele});  // value and key is pushed
            if (heap.size() > k) {
                heap.pop();
            }
        }

        // for printing the ele with most fre first
        std::vector<int> ans;
        while (!heap.empty()) {
            auto temp = heap.top(); heap.pop();
            ans.push_back(temp.second);      // will store the ele with least fre among k top frequent first
        }
        std::reverse(ans.begin(), ans.end());    // now return the reverse of ans
        return ans;

        // for printing the ele with most fre first
        // std::vector<int> ans;
        // for (int i = 0; i < heap.size(); ++i) {
        //     auto temp = heap.top(); heap.pop();
        //     ans.push_back(temp.second);      // will store the ele with least fre among k top frequent first
        // }
        // // std::cout << ans
        // std::reverse(ans.begin(), ans.end());    // now return the reverse of ans
        // return ans;
    }
};
"""

# method 3: 
# better one: using bucket sort
# just create the freq matrix for maximum no of count and that can be len(arr)
# time: O(n), space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= {}   # to store the count of each element
        for num in nums:
            count[num]= 1+ count.get(num, 0)   # if num is already present then incr the val by '1'
                                               # else incr the value by zero
                
        freq= [[] for i in range(len(nums)+1)]    # will contain the array of ele for a given frequency
                                                 # since freq can be equal to n so we are taking the row equal to n+1
            
        # now store the array of ele with for a given fre
        # like at index 1: will contain array of ele whose fre is 1 and so on till n
        for n,c in count.items():
            freq[c].append(n)
            
        # now traverse the freq from right to left 
        # as most freq ele will be at higher index
        # and store the ele into ans and when you have stored 'k' ele just return the ans
        ans= []
        for i in range((len(freq)-1),0,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans)==k:
                    return ans


# Java Code 
"""
import java.util.*;

public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();   // to store the count of each element
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);   // if num is already present then incr the val by '1'
                                                              // else incr the value by zero
        }

        List<List<Integer>> freq = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) {
            freq.add(new ArrayList<>());
        }
        // will contain the array of ele for a given frequency
        // since freq can be equal to n so we are taking the row equal to n+1

        // now store the array of ele with for a given fre
        // like at index 1: will contain array of ele whose fre is 1 and so on till n
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq.get(entry.getValue()).add(entry.getKey());
        }

        List<Integer> ans = new ArrayList<>();
        // now traverse the freq from right to left 
        // as most freq ele will be at higher index
        // and store the ele into ans and when you have stored 'k' ele just return the ans
        for (int i = freq.size() - 1; i > 0; i--) {
            for (int n : freq.get(i)) {
                ans.add(n);
                if (ans.size() == k) {
                    return ans;
                }
            }
        }
        return ans; // fallback, though input guarantees k valid results
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> count;   // to store the count of each element
        for (int num : nums) {
            count[num] += 1;   // if num is already present then incr the val by '1'
                               // else incr the value by zero
        }

        std::vector<std::vector<int>> freq(nums.size() + 1);
        // will contain the array of ele for a given frequency
        // since freq can be equal to n so we are taking the row equal to n+1

        // now store the array of ele with for a given fre
        // like at index 1: will contain array of ele whose fre is 1 and so on till n
        for (auto& [n, c] : count) {
            freq[c].push_back(n);
        }

        std::vector<int> ans;
        // now traverse the freq from right to left 
        // as most freq ele will be at higher index
        // and store the ele into ans and when you have stored 'k' ele just return the ans
        for (int i = freq.size() - 1; i > 0; --i) {
            for (int n : freq[i]) {
                ans.push_back(n);
                if (ans.size() == k) {
                    return ans;
                }
            }
        }
        return ans;
    }
};
"""