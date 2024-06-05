# Method 1:
# Check for max in every window
# Time : O(n - k + 1)*k

# Method 3:
# using 'SortedList' in python.
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

# Method 3: 
# Optimisation. Accepted 
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

# Understand 'method 3' and 'method 4' later.

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


# Java
"""
// Method 3: 

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);

        // Insert first 'k' elements in 'maxHeap' to get the answer for the 1st window.
        // We need to remove elements that are out of the window, so we insert indices as well.
        for (int i = 0; i < k; i++) {
            maxHeap.offer(new int[]{nums[i], i});
        }
        ans[0] = maxHeap.peek()[0];  // for 1st window

        // Now find the answer for remaining windows
        for (int i = k; i < n; i++) {
            // First, add the current element into the heap, because this can also be the answer for the current window.
            maxHeap.offer(new int[]{nums[i], i});

            // Then remove elements from the heap which are not part of the current window if they are on top of the heap.
            // Elements out of the current window can be in the heap even after removal from the top,
            // but if not on top, then they won't affect our answer.
            // Due to this, for each element, time complexity will be 'log n' not 'log k' as there can be more than 'k' elements in the heap.
            while (!maxHeap.isEmpty() && maxHeap.peek()[1] <= i - k) {
                maxHeap.poll();
            }

            // Now the top of the heap will be the answer for the current window.
            ans[i - k + 1] = maxHeap.peek()[0];
        }
        return ans;
    }
}


// Method 5:

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> deque = new ArrayDeque<>(); // will store indices of elements in monotonically decreasing order
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        int index = 0;

        for (int j = 0; j < n; j++) {
            // Remove elements from the deque that are smaller than the current element
            while (!deque.isEmpty() && nums[j] > nums[deque.peekLast()]) {
                deque.pollLast();
            }

            // Add the current element at the end of the deque
            deque.offerLast(j);

            // If the window has hit size k, update the results
            if (j + 1 >= k) {
                // The element at the front of the deque is the largest
                ans[index++] = nums[deque.peekFirst()];
                
                // Remove the elements which are out of this window
                if (deque.peekFirst() == j - k + 1) {
                    deque.pollFirst();
                }
            }
        }
        return ans;
    }
}

"""