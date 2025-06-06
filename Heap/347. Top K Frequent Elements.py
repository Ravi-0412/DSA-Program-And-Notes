# method 1: Sort based on frequency
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


# method 2: using bucket sort(better one)
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




# Link: https://leetcode.com/problems/top-k-frequent-elements/solutions/1927648/one-of-the-best-explanation/

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> hashmap = new HashMap<>();

        // Store frequency of each element
        for (int num : nums) {
            hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
        }

        // Sort hashmap keys by frequency in descending order
        List<Integer> arr = new ArrayList<>(hashmap.keySet());
        arr.sort((a, b) -> Integer.compare(hashmap.get(b), hashmap.get(a)));

        return arr.stream().limit(k).mapToInt(i -> i).toArray();
    }
}
//Method 2
import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>(Comparator.comparingInt(Map.Entry::getValue));

        // Store frequency of each element
        for (int num : nums) {
            hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
        }

        // Maintain a min heap of k most frequent elements
        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) {
            minHeap.offer(entry);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        // Extract elements from the heap
        int[] ans = new int[k];
        int index = 0;
        while (!minHeap.isEmpty()) {
            ans[index++] = minHeap.poll().getKey();
        }
        
        return ans;
    }
}
//Method 3
import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();

        // Store frequency of each element
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Create buckets based on frequency
        List<List<Integer>> freq = new ArrayList<>(Collections.nCopies(nums.length + 1, new ArrayList<>()));
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq.get(entry.getValue()).add(entry.getKey());
        }

        // Collect top k elements
        List<Integer> ans = new ArrayList<>();
        for (int i = freq.size() - 1; i > 0 && ans.size() < k; --i) {
            for (int num : freq.get(i)) {
                ans.add(num);
                if (ans.size() == k) {
                    return ans.stream().mapToInt(Integer::intValue).toArray();
                }
            }
        }
        
        return new int[0];
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hashmap;
        
        // Store frequency of each element
        for (int num : nums) {
            hashmap[num]++;
        }

        // Sort hashmap keys by frequency in descending order
        vector<int> arr;
        for (const auto& pair : hashmap) {
            arr.push_back(pair.first);
        }

        sort(arr.begin(), arr.end(), [&](int a, int b) {
            return hashmap[a] > hashmap[b];
        });

        return vector<int>(arr.begin(), arr.begin() + k);
    }
};
//Method 2
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hashmap;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;

        // Store frequency of each element
        for (int num : nums) {
            hashmap[num]++;
        }

        // Maintain a min heap of k most frequent elements
        for (const auto& pair : hashmap) {
            minHeap.push({pair.second, pair.first});
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }

        // Extract elements from the heap
        vector<int> ans;
        while (!minHeap.empty()) {
            ans.push_back(minHeap.top().second);
            minHeap.pop();
        }
        
        return ans;
    }
};

//Method 3
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        
        // Store frequency of each element
        for (int num : nums) {
            count[num]++;
        }

        // Create buckets based on frequency
        vector<vector<int>> freq(nums.size() + 1);
        for (const auto& pair : count) {
            freq[pair.second].push_back(pair.first);
        }

        // Collect top k elements
        vector<int> ans;
        for (int i = freq.size() - 1; i > 0 && ans.size() < k; --i) {
            for (int num : freq[i]) {
                ans.push_back(num);
                if (ans.size() == k) {
                    return ans;
                }
            }
        }
        
        return ans;
    }
};
"""