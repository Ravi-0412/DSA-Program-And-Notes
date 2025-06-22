# Method 1:
# Check for max in every window
# Time : O(n - k + 1)*k

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n - k + 1):
            window_max = max(nums[i:i+k])
            res.append(window_max)

        return res

# Java Code 
"""
import java.util.*;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[n - k + 1];

        for (int i = 0; i <= n - k; i++) {
            int windowMax = Integer.MIN_VALUE;
            for (int j = i; j < i + k; j++) {
                windowMax = Math.max(windowMax, nums[j]);
            }
            res[i] = windowMax;
        }

        return res;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> res;

        for (int i = 0; i <= n - k; i++) {
            int windowMax = nums[i];
            for (int j = i; j < i + k; j++) {
                windowMax = max(windowMax, nums[j]);
            }
            res.push_back(windowMax);
        }

        return res;
    }
};
"""

# Method 2:
# using 'SortedList' in python and similar thing in java & C++.

from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sorted_list = SortedList([])
        for i in range(k):
            sorted_list.add(nums[i])
        ans = []
        ans.append(sorted_list[- 1])
        for i in range(k, n):
            sorted_list.add(nums[i])
            sorted_list.remove(nums[i - k])
            ans.append(sorted_list[-1])
        return ans 

# Java Code 
"""
import java.util.*;

class Solution {
    public List<Integer> maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        TreeMap<Integer, Integer> sortedMap = new TreeMap<>();
        for (int i = 0; i < k; i++) {
            sortedMap.put(nums[i], sortedMap.getOrDefault(nums[i], 0) + 1);
        }

        List<Integer> ans = new ArrayList<>();
        ans.add(sortedMap.lastKey());

        for (int i = k; i < n; i++) {
            sortedMap.put(nums[i], sortedMap.getOrDefault(nums[i], 0) + 1);
            int toRemove = nums[i - k];
            if (sortedMap.get(toRemove) == 1) {
                sortedMap.remove(toRemove);
            } else {
                sortedMap.put(toRemove, sortedMap.get(toRemove) - 1);
            }
            ans.add(sortedMap.lastKey());
        }

        return ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        multiset<int> window;
        for (int i = 0; i < k; ++i) {
            window.insert(nums[i]);
        }

        vector<int> ans;
        ans.push_back(*window.rbegin());

        for (int i = k; i < n; ++i) {
            window.insert(nums[i]);
            window.erase(window.find(nums[i - k]));
            ans.push_back(*window.rbegin());
        }

        return ans;
    }
};
"""

# Method 3: 
# Easier one
# Use heap for finding the max ele in each window.

# Time: O(n*logn)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        maxHeap = []
        # insert first 'k' element in 'maxHeap' to get ans for 1st window.
        # We need to remove the also after each ele if their index is out of window so inserting index as well.
        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i)) 
        ans.append(-maxHeap[0][0])  # for 1st window
        # Now find the ans for remaining window
        for i in range(k, n):
            # 1st add the cur ele into heap, because this can also be the answer for current window.
            heapq.heappush(maxHeap, (-nums[i], i))
            # Then remove the ele from heap which is not part of cur window if on top of heap.
            # Ele out of cur window can be in heap even after removal from top, 
            # but if not on top then, that won't affect our ans.
            # Due to this for each ele time complexity will be 'logn' not 'logk' as there can be more than 'k' ele in heap.
            while maxHeap and (i - maxHeap[0][1]) >= k:
                heapq.heappop(maxHeap)
            # Now top of heap will be ans for cur window
            ans.append(-maxHeap[0][0])
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]); 
        // insert first 'k' element in 'maxHeap' to get ans for 1st window.
        // We need to remove the also after each ele if their index is out of window so inserting index as well.
        for (int i = 0; i < k; i++) {
            maxHeap.offer(new int[]{nums[i], i});
        }
        ans[0] = maxHeap.peek()[0];  // for 1st window

        // Now find the ans for remaining window
        for (int i = k; i < n; i++) {
            // 1st add the cur ele into heap, because this can also be the answer for current window.
            maxHeap.offer(new int[]{nums[i], i});

            // Then remove the ele from heap which is not part of cur window if on top of heap.
            // Ele out of cur window can be in heap even after removal from top,
            // but if not on top then, that won't affect our ans.
            // Due to this for each ele time complexity will be 'logn' not 'logk' as there can be more than 'k' ele in heap.
            while (!maxHeap.isEmpty() && i - maxHeap.peek()[1] >= k) {
                maxHeap.poll();
            }

            // Now top of heap will be ans for cur window
            ans[i - k + 1] = maxHeap.peek()[0];
        }

        return ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans;
        priority_queue<pair<int, int>> maxHeap;

        // insert first 'k' element in 'maxHeap' to get ans for 1st window.
        // We need to remove the also after each ele if their index is out of window so inserting index as well.
        for (int i = 0; i < k; ++i) {
            maxHeap.push({nums[i], i});
        }
        ans.push_back(maxHeap.top().first);  // for 1st window

        // Now find the ans for remaining window
        for (int i = k; i < n; ++i) {
            // 1st add the cur ele into heap, because this can also be the answer for current window.
            maxHeap.push({nums[i], i});

            // Then remove the ele from heap which is not part of cur window if on top of heap.
            // Ele out of cur window can be in heap even after removal from top,
            // but if not on top then, that won't affect our ans.
            // Due to this for each ele time complexity will be 'logn' not 'logk' as there can be more than 'k' ele in heap.
            while (!maxHeap.empty() && i - maxHeap.top().second >= k) {
                maxHeap.pop();
            }

            // Now top of heap will be ans for cur window
            ans.push_back(maxHeap.top().first);
        }

        return ans;
    }
};
"""

# Method 4:
# say NUMS : 1, 3, -1, -3, 5, 3, 6, 7

# 1) divide array into blocks of K starting from index 0.
# Here divide into blocks of size K=3. then,

# NUMS : 1, 3, -1, | -3, 5, 3, | 6, 7

# 2) We have divided into blocks because we will calculate maximum in 2 ways:
#  A.) by traversing from left to right B.) by traversing from right to left.

# Why two ways:
# Because if we keep track of maximum from either left or right only then won't be maximum for all window.
# e.g: in above 'nums' , '1' is not maximum for index '0'  but it is maximum seen from left till index '0'.
# But if we can keep track of max from right also for cur window then max_right[0] then we can get correct ans = 3

# 3) Traversing from Left to Right. For each element ai in block we will find maximum till that element 'ai' 
# starting from START of Block to END of that block. So here,
# NUMS : 1, 3, -1, | -3, 5, 3, | 6, 7
# Left : 1, 3, 3,  | -3, 5, 5, | 6, 7

# 4) Secondly, traversing from Right to Left. For each element 'ai' in block we will find maximum till that element 'ai' 
# starting from END of Block to START of that block. So Here,
# NUMS : 1, 3, -1, | -3, 5, 3, | 6, 7
# Right : 3, 3, -1, | 5, 5, 3, | 7, 7

# 5) Now we have to find maximum for each subarray or window of size K. So, starting from index = 0 to index = N-K+1 .
# NUMS :  1, 3, -1, | -3, 5, 3,  | 6, 7
# Left :  1, 3, 3,  | -3, 5, 5,  | 6, 7
# Right : 3, 3, -1, | 5, 5,  3,  | 7, 7

# max_val[index] = max(Rgt[index], Lft[index+k-1]);
# So Final Answer : 3, 3, 5, 5, 6, 7
# Time Complexity: O(n)



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [-10**4 -1] *n  # Will track of maximum ele seen till now in each window from left to right
                               # Initialising with minimum possible value
        right = [-10**4 -1] *n  # Will track of maximum ele seen till now in each window from right to left
        # First finding for 'left'
        for i in range(n):
            # if 'i' is start of window
            if i % k == 0:
                # Then 'nums[i]' will be max 
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
        
        # Now find for right
        right[n-1] = nums[n-1]
        # here we have to start from 'n-2' because after dividing array into window of size 'k', we may left with less than 'k' ele in last subarary
        for i in range(n-2, -1, -1):   
            # if 'i' is the end of window from right i.e 1st ele from left
            if i % k == k-1:
                # Then 'nums[i]' will be max 
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])
        
        # Now find the ans for possible window from left
        # Max we have to find till 'n-k'
        ans = []
        for i in range(n -k + 1):
            # = maximum when cur ele will be 1st ele for window
            # left[i +k-1] :  is the maximum of the element on the right of boundary.
            # right[i]     : the maximum of elements on the left of boundary.
            ans.append(max(right[i], left[i + k -1]))
        return ans

# Java Code 
"""
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] left = new int[n];  // Will track of maximum ele seen till now in each window from left to right
                                  // Initialising with minimum possible value
        int[] right = new int[n]; // Will track of maximum ele seen till now in each window from right to left
        for (int i = 0; i < n; i++) {
            if (i % k == 0) {
                // Then 'nums[i]' will be max 
                left[i] = nums[i];
            } else {
                left[i] = Math.max(left[i - 1], nums[i]);
            }
        }

        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (i % k == k - 1) {
                // Then 'nums[i]' will be max 
                right[i] = nums[i];
            } else {
                right[i] = Math.max(right[i + 1], nums[i]);
            }
        }

        int[] ans = new int[n - k + 1];
        for (int i = 0; i <= n - k; i++) {
            // left[i +k-1] :  is the maximum of the element on the right of boundary.
            // right[i]     : the maximum of elements on the left of boundary.
            ans[i] = Math.max(right[i], left[i + k - 1]);
        }

        return ans;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> left(n, -10001);  // Will track of maximum ele seen till now in each window from left to right
                                      // Initialising with minimum possible value
        vector<int> right(n, -10001); // Will track of maximum ele seen till now in each window from right to left

        for (int i = 0; i < n; ++i) {
            if (i % k == 0) {
                // Then 'nums[i]' will be max 
                left[i] = nums[i];
            } else {
                left[i] = max(left[i - 1], nums[i]);
            }
        }

        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            if (i % k == k - 1) {
                // Then 'nums[i]' will be max 
                right[i] = nums[i];
            } else {
                right[i] = max(right[i + 1], nums[i]);
            }
        }

        vector<int> ans;
        for (int i = 0; i <= n - k; ++i) {
            // left[i +k-1] :  is the maximum of the element on the right of boundary.
            // right[i]     : the maximum of elements on the left of boundary.
            ans.push_back(max(right[i], left[i + k - 1]));
        }

        return ans;
    }
};
"""

# Method 5: 
# Using Mono deque

# See the method '3' of q : "1425. Constrained Subsequence Sum" for better understanding.
# And try to do this by similar approach.

# Time = space = O(n)

import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        de= collections.deque()   # will store ele in mono decreaseing order as we need maximum ele.
        i,j,ans,n= 0,0,[],len(nums)
        while j < n:
            # if curr ele is greater than the last elements then pop until you find any ele greater the curr ele
            # Because agar cur ele 'j' bda h then for upcoming window ans me isko lena h , pichle wale ka koi matlab nhi.
            while de and nums[j] > de[-1]:  
                de.pop()
            de.append(nums[j])   # Ab isko append kar do kyonki upcoming window ke liye ye max ho sakta h.
            if j+1 >= k:    # or j-i+1== k:
                # if we have seen elements >= k then we can update our ans.
                ans.append(de[0])  # for that subarray first ele of 'deque' will give the ans because 1st ele will be maximum only.
                                    # as deque maintaing ele in mono decreasing order.
                if nums[i] == de[0]:  # before sliding the window check whether the max ele is at the 'ith' index
                    de.popleft()    # here we have to pop from left since only leftmost was giving the ans
                i+= 1
            j+= 1
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> de = new ArrayDeque<>();  // will store ele in mono decreasing order as we need maximum ele.
        int i = 0, j = 0, n = nums.length;
        List<Integer> ans = new ArrayList<>();

        while (j < n) {
            // if curr ele is greater than the last elements then pop until you find any ele greater the curr ele
            // Because agar cur ele 'j' bda h then for upcoming window ans me isko lena h , pichle wale ka koi matlab nhi.
            while (!de.isEmpty() && nums[j] > de.peekLast()) {
                de.pollLast();
            }
            de.addLast(nums[j]);  // Ab isko append kar do kyonki upcoming window ke liye ye max ho sakta h.

            if (j + 1 >= k) {  // or j - i + 1 == k:
                // if we have seen elements >= k then we can update our ans.
                ans.add(de.peekFirst());  // for that subarray first ele of 'deque' will give the ans because 1st ele will be maximum only.
                                           // as deque maintaing ele in mono decreasing order.
                if (nums[i] == de.peekFirst()) {  // before sliding the window check whether the max ele is at the 'ith' index
                    de.pollFirst();  // here we have to pop from left since only leftmost was giving the ans
                }
                i++;
            }
            j++;
        }

        return ans.stream().mapToInt(x -> x).toArray();
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> de;  // will store ele in mono decreasing order as we need maximum ele.
        int i = 0, j = 0, n = nums.size();
        vector<int> ans;

        while (j < n) {
            // if curr ele is greater than the last elements then pop until you find any ele greater the curr ele
            // Because agar cur ele 'j' bda h then for upcoming window ans me isko lena h , pichle wale ka koi matlab nhi.
            while (!de.empty() && nums[j] > de.back()) {
                de.pop_back();
            }
            de.push_back(nums[j]);  // Ab isko append kar do kyonki upcoming window ke liye ye max ho sakta h.

            if (j + 1 >= k) {  // or j - i + 1 == k:
                // if we have seen elements >= k then we can update our ans.
                ans.push_back(de.front());  // for that subarray first ele of 'deque' will give the ans because 1st ele will be maximum only.
                                            // as deque maintaing ele in mono decreasing order.
                if (nums[i] == de.front()) {  // before sliding the window check whether the max ele is at the 'ith' index
                    de.pop_front();  // here we have to pop from left since only leftmost was giving the ans
                }
                i++;
            }
            j++;
        }

        return ans;
    }
};
"""
