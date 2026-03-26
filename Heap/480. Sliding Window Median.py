# method 1:
# very easy and simple using "sortedList"
# Read about "sorteContainers here": 
# https://grantjenks.com/docs/sortedcontainers/sortedlist.html

# logic: SortedList store the ele in sorted order and after removing also it maintain the sorted order.
# time complexity of adding 'lst.add(num)' and removing "lst.remove()" is logn. n= no of ele in list.

# Note: may interviewer may not accept this and may ask for some other solution i. using heaps.
# time: O(n*logk)

from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans= []
        lst= SortedList()
        i, j= 0, 0
        while j < len(nums):
            lst.add(nums[j])
            if j - i + 1 >= k:
                if k & 1:
                    median= lst[k//2]
                    ans.append(median)
                else:
                    median= (lst[k//2 -1] + lst[k//2])/2
                    ans.append(median)

                lst.remove(nums[i])
                i+= 1
            j+= 1
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        List<Double> ans = new ArrayList<>();
        TreeMap<Integer, Integer> window = new TreeMap<>();
        int i = 0, j = 0;

        while (j < nums.length) {
            window.put(nums[j], window.getOrDefault(nums[j], 0) + 1);

            if (j - i + 1 >= k) {
                int count = 0;
                double median = 0.0;
                int mid1 = (k - 1) / 2, mid2 = k / 2;
                int total = 0;
                for (Map.Entry<Integer, Integer> entry : window.entrySet()) {
                    total += entry.getValue();
                    if (count <= mid1 && mid1 < total) median += entry.getKey();
                    if (count <= mid2 && mid2 < total) median += entry.getKey();
                    count = total;
                }
                ans.add(median / 2.0);

                int outNum = nums[i];
                window.put(outNum, window.get(outNum) - 1);
                if (window.get(outNum) == 0) window.remove(outNum);
                i++;
            }
            j++;
        }

        double[] result = new double[ans.size()];
        for (int x = 0; x < ans.size(); x++) result[x] = ans.get(x);
        return result;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <set>

class Solution {
public:
    std::vector<double> medianSlidingWindow(std::vector<int>& nums, int k) {
        std::vector<double> ans;
        std::multiset<int> window;
        auto mid = window.begin();

        for (int i = 0; i < nums.size(); ++i) {
            window.insert(nums[i]);
            if (i >= k) {
                window.erase(window.find(nums[i - k]));
            }

            if (i >= k - 1) {
                auto it = window.begin();
                std::advance(it, k / 2);
                if (k % 2 == 0) {
                    auto it2 = it;
                    std::advance(it2, -1);
                    double median = (*it + *it2) / 2.0;
                    ans.push_back(median);
                } else {
                    ans.push_back(*it);
                }
            }
        }
        return ans;
    }
};
"""

# method 2: 
# using heaps
# Understand properly the intuition behind 'if nums[i] <= large[0][0]:'

# Note: we are putting extra one ele in case 'k' is odd into large(minHeap).

import heapq

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        # small: Max-Heap 
        # large: Min-Heap
        self.small, self.large = [], []
        
        # 1. Initialize the first window
        for i in range(k):
            heapq.heappush(self.small, (-nums[i], i))
        
        # Balance: Move the largest from small to large until large has (k - k//2) elements
        # so that in case of odd element , large heap(minHeap) contains one extra element.
        for _ in range(k - k // 2):
            val, idx = heapq.heappop(self.small)
            heapq.heappush(self.large, (-val, idx))
            
        ans = [self._get_median(k)]
        
        # 2. Slide the window
        for i in range(len(nums) - k):
            new_val_idx = i + k
            old_val_idx = i
            
            # Use helper to handle insertion and logical rebalancing
            self._handle_sliding_transition(nums[new_val_idx], new_val_idx, nums[old_val_idx])
            
            # Use helper to clean up "garbage" elements from the tops
            self._prune_expired_elements(old_val_idx)
            
            ans.append(self._get_median(k))
            
        return ans

    def _handle_sliding_transition(self, x, x_idx, outgoing_val):
        """
        Logic: Adds new element x and ensures the heaps stay balanced 
        relative to the outgoing_val.
        """
        # If new element belongs in the large (right) half
        if x >= self.large[0][0]:
            heapq.heappush(self.large, (x, x_idx))
            # Rebalance: If the value leaving the window was in the small (left) half,
            # then 'large' now has one extra net element. Move top of large to small.
            # "=" sig"
            if outgoing_val <= self.large[0][0]:
                val, idx = heapq.heappop(self.large)
                heapq.heappush(self.small, (-val, idx))
        else:
            # New element belongs in the small (left) half
            heapq.heappush(self.small, (-x, x_idx))
            # Rebalance: If the value leaving was in the large (right) half,
            # then 'small' now has one extra net element. Move top of small to large.
            if outgoing_val >= self.large[0][0]:
                neg_val, idx = heapq.heappop(self.small)
                heapq.heappush(self.large, (-neg_val, idx))

    def _prune_expired_elements(self, expired_idx):
        """
        Logic: Only the top of the heap matters for median calculation.
        We 'lazily' remove elements whose indices are no longer in the current window.
        """
        while self.small and self.small[0][1] <= expired_idx:
            heapq.heappop(self.small)
        while self.large and self.large[0][1] <= expired_idx:
            heapq.heappop(self.large)

    def _get_median(self, k):
        """Logic: Calculates median based on heap tops."""
        if k & 1: # Odd
            return float(self.large[0][0])
        else: # Even
            return (self.large[0][0] - self.small[0][0]) / 2.0

# Java Code 
"""
import java.util.*;

class Solution {
    public List<Double> medianSlidingWindow(int[] nums, int k) {
        PriorityQueue<long[]> small = new PriorityQueue<>((a, b) -> Long.compare(b[0], a[0])); // maxHeap
        PriorityQueue<long[]> large = new PriorityQueue<>(Comparator.comparingLong(a -> a[0])); // minHeap

        List<Double> ans = new ArrayList<>();

        for (int i = 0; i < k; i++) {
            small.offer(new long[]{-nums[i], i});
        }

        // Now move half of the ele from small to large to balance heaps.
        // doing like this to keep extra ele in 'large' in case 'k' is odd.
        // for i in range(k//2): won't put extra ele in 'large' in case 'k' is odd.
        for (int i = 0; i < k - k / 2; i++) {
            long[] top = small.poll();
            large.offer(new long[]{-top[0], top[1]});
        }

        ans.add(getMed(small, large, k));

        for (int i = 0; i < nums.length - k; i++) {
            int x = nums[i + k];

            if (x >= large.peek()[0]) {
                large.offer(new long[]{x, i + k});
                if (nums[i] <= large.peek()[0]) {
                    long[] top = large.poll();
                    small.offer(new long[]{-top[0], top[1]});
                }
            } else {
                small.offer(new long[]{-x, i + k});
                if (nums[i] >= large.peek()[0]) {
                    long[] top = small.poll();
                    large.offer(new long[]{-top[0], top[1]});
                }
            }

            while (!small.isEmpty() && small.peek()[1] <= i) small.poll();
            while (!large.isEmpty() && large.peek()[1] <= i) large.poll();

            ans.add(getMed(small, large, k));
        }

        return ans;
    }

    private double getMed(PriorityQueue<long[]> h1, PriorityQueue<long[]> h2, int k) {
        return (k & 1) == 1 ? h2.peek()[0] : ((double) h2.peek()[0] - h1.peek()[0]) / 2;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <queue>
#include <utility>

using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> small; // maxHeap
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> large; // minHeap
        vector<double> ans;

        for (int i = 0; i < k; i++) {
            small.emplace(nums[i], i);
        }

        // Now move half of the ele from small to large to balance heaps.
        // doing like this to keep extra ele in 'large' in case 'k' is odd.
        // for i in range(k//2): won't put extra ele in 'large' in case 'k' is odd.
        for (int i = 0; i < k - k / 2; i++) {
            auto top = small.top(); small.pop();
            large.emplace(top.first, top.second);
        }

        ans.push_back(getMed(small, large, k));

        for (int i = 0; i < nums.size() - k; i++) {
            int x = nums[i + k];

            if (x >= large.top().first) {
                large.emplace(x, i + k);
                if (nums[i] <= large.top().first) {
                    auto top = large.top(); large.pop();
                    small.emplace(top);
                }
            } else {
                small.emplace(x, i + k);
                if (nums[i] >= large.top().first) {
                    auto top = small.top(); small.pop();
                    large.emplace(top);
                }
            }

            while (!small.empty() && small.top().second <= i) small.pop();
            while (!large.empty() && large.top().second <= i) large.pop();

            ans.push_back(getMed(small, large, k));
        }

        return ans;
    }

private:
    double getMed(priority_queue<pair<int, int>>& h1,
                  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>>& h2,
                  int k) {
        return (k & 1) ? h2.top().first : ((double)h2.top().first + h1.top().first) / 2;
    }
};
"""
