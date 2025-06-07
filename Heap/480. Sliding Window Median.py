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

# method 2: using heaps
# Try later agai and understand properly the intuition
# behind 'if nums[i] <= large[0][0]:'

# Note: we are putting extra one ele in case 'k' is odd into large(minHeap).
    
# Link: https://leetcode.com/problems/sliding-window-median/

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
//Method 1
import java.util.*;

class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        double[] ans = new double[n - k + 1];
        TreeSet<Integer> window = new TreeSet<>(); // Maintains ordered elements in the window

        for (int i = 0; i < k; i++) {
            window.add(nums[i]);
        }

        for (int i = k; i <= n; i++) {
            // Compute median
            List<Integer> sortedList = new ArrayList<>(window);
            if (k % 2 == 1) {
                ans[i - k] = sortedList.get(k / 2);
            } else {
                ans[i - k] = (sortedList.get(k / 2) + sortedList.get(k / 2 - 1)) / 2.0;
            }

            // Remove leftmost element from window (except at last iteration)
            if (i < n) {
                window.add(nums[i]);
                window.remove(nums[i - k]);
            }
        }
        return ans;
    }
}
//Method 2
import java.util.*;

class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        double[] ans = new double[n - k + 1];
        PriorityQueue<int[]> small = new PriorityQueue<>((a, b) -> b[0] - a[0]); // maxHeap
        PriorityQueue<int[]> large = new PriorityQueue<>((a, b) -> a[0] - b[0]); // minHeap

        // Initialize heaps with first 'k' elements
        for (int i = 0; i < k; i++) {
            small.offer(new int[]{nums[i], i});
        }

        // Move half from 'small' to 'large' to balance heaps
        for (int i = 0; i < k - k / 2; i++) {
            large.offer(new int[]{-small.poll()[0], small.peek()[1]});
        }

        ans[0] = k % 2 == 1 ? large.peek()[0] : (large.peek()[0] - small.peek()[0]) / 2.0;

        for (int i = k; i < n; i++) {
            int x = nums[i], idx = i;
            if (x >= large.peek()[0]) {
                large.offer(new int[]{x, idx});
                if (nums[i - k] <= large.peek()[0]) {
                    small.offer(new int[]{-large.poll()[0], large.peek()[1]});
                }
            } else {
                small.offer(new int[]{-x, idx});
                if (nums[i - k] >= large.peek()[0]) {
                    large.offer(new int[]{-small.poll()[0], small.peek()[1]});
                }
            }

            while (!small.isEmpty() && small.peek()[1] <= i - k) small.poll();
            while (!large.isEmpty() && large.peek()[1] <= i - k) large.poll();

            ans[i - k + 1] = k % 2 == 1 ? large.peek()[0] : (large.peek()[0] - small.peek()[0]) / 2.0;
        }

        return ans;
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> ans;
        multiset<int> window(nums.begin(), nums.begin() + k); // Ordered container for window elements
        auto mid = next(window.begin(), k / 2); // Iterator pointing to median position

        for (int i = k; i <= nums.size(); i++) {
            // Compute median
            if (k % 2) {
                ans.push_back(*mid);
            } else {
                ans.push_back((*mid + *prev(mid)) / 2.0);
            }

            // Remove leftmost element from window (except at last iteration)
            if (i < nums.size()) {
                window.insert(nums[i]);
                if (nums[i] < *mid) mid--;
                if (nums[i - k] <= *mid) mid++;
                window.erase(window.lower_bound(nums[i - k]));
            }
        }
        return ans;
    }
};
//Method 2
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> ans;
        priority_queue<pair<int, int>> small; // maxHeap
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> large; // minHeap

        // Initialize heaps with first 'k' elements
        for (int i = 0; i < k; i++) {
            small.push({-nums[i], i});
        }

        // Move half from 'small' to 'large' to balance heaps
        for (int i = 0; i < k - k / 2; i++) {
            large.push({-small.top().first, small.top().second});
            small.pop();
        }

        ans.push_back(k % 2 ? large.top().first : (large.top().first - small.top().first) / 2.0);

        for (int i = k; i < nums.size(); i++) {
            int x = nums[i], idx = i;
            if (x >= large.top().first) {
                large.push({x, idx});
                if (nums[i - k] <= large.top().first) {
                    small.push({-large.top().first, large.top().second});
                    large.pop();
                }
            } else {
                small.push({-x, idx});
                if (nums[i - k] >= large.top().first) {
                    large.push({-small.top().first, small.top().second});
                    small.pop();
                }
            }

            while (!small.empty() && small.top().second <= i - k) small.pop();
            while (!large.empty() && large.top().second <= i - k) large.pop();

            ans.push_back(k % 2 ? large.top().first : (large.top().first - small.top().first) / 2.0);
        }

        return ans;
    }
};
"""