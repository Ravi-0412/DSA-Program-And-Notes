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
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        
        def get_med(h1, h2, k):
            return h2[0][0] if k & 1 else (h2[0][0]-h1[0][0]) / 2

        small = []  # maxHeap
        large = []  # minHeap
        for i, x in enumerate(nums[:k]): 
            heapq.heappush(small, (-x,i))
        # Now move half of the ele from small to large to balance heaps.

        # doing like this to keep extra ele in 'large' in case 'k' is odd.
        # for i in range(k//2) : won't put extra ele in 'large' in case 'k' is odd.
        for _ in range(k - k//2):   
            x, ind = heapq.heappop(small)
            heapq.heappush(large, (-x, ind))
        # calculate the ans for 1st subarray i.e till index 'k-1'.
        ans = [get_med(small, large, k)]
        
        for i, x in enumerate(nums[k:]):
            # print(i, nums[i], ans, "index")
            # print(small, large, "Before")
            
            if x >= large[0][0]:
                # x belongs to 'large' heap. so put this in large heap.
                heapq.heappush(large, (x, i+k))
                # check if nums[i] belong to opposite heap as 'x' i.e small to rebalance
                if nums[i] <= large[0][0]:
                    # Nums[i] belongs to small heap. 
                    # In this case move one element from 'large' to 'small' to
                    # rebalance heap as after poping nums[i] from small
                    # diff in length of 'large' and small will be > 1 .
                    x, ind = heapq.heappop(large)
                    heapq.heappush(small, (-x, ind))
                # if nums[i] belongs to 'large' then in case any ele we pop heap will be balanced only.
            else:
                # x belongs to 'small' heap. so put this in small heap.
                heapq.heappush(small, (-x, i+k))
                # check if 'nums[i]' belongs to 'small' heap.
                if nums[i] >= large[0][0]:
                    # Nums[i] belongs to large heap. 
                    # In this case move one element from 'small' to 'large' to
                    # rebalance heap as after poping nums[i] from small
                    # diff in length of 'small' and large will be > 1 .
                    x, ind = heapq.heappop(small)
                    heapq.heappush(large, (-x, ind))
                # if nums[i] belongs to 'small' then in case any ele we pop heap will be balanced only.
            # Now remove elements till index 'i' from both the heaps 
            # if index at top is <= i.
            # because only top ele will giev the median and element till index 'i'
            # shouldn't contribute to median so remove from top.

            # print(small, large, "heaps")
            while small and small[0][1] <= i: 
                heapq.heappop(small)
            # print(small, "small after")
            while large and large[0][1] <= i: 
                heapq.heappop(large)
            # print(small, large, "after")

            # Note: may happen at no ele is removed from any of the heap
            # if index of top of both the heap > 'i'.
            # And may happen that a lot of element may get removed later for other index.
            # if index of top of both the heap <= 'i'.

            # But we will get the correct median.
            ans.append(get_med(small, large, k))
        return ans

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