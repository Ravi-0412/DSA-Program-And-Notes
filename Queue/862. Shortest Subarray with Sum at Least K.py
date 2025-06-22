# Method 1: 

# vvi: only Poistive values solution i.e q :""209. Minimum Size Subarray Sum"
#  won't work since number is "-ve" number also.
# Because inner while loop can break before finding the shortest subarray after adding the curr ele.
# e.g: [3,-2,5], k= 4. 
# if we will apply "+ve" values soln then output= 3 but ans should = 1.

# how to Handle the negative value?

# Note: "q" is storing the possible starting index from which we can start our subarray for ans.
# And in every iteration , we are removing those index which can't be starting index of our ans subarray.

# Here prefix[i] means sum till index 'i-1'.

# Note: Here length = j - q.popleft(), because 'j' is not included in prefixSum when we are at 'j'.
# So we will write length = 'j-1' - i + 1 === j- i === j - q.popleft()
# 'prefixSum[j] - prefixSum[q[0]]': denotes the curSum like prefix[j] - prefix[i] where i= q[0]

# Note vvvi:
# why not calculating prefix like prefixSum[i]= prefixSum[i- 1] + nums[i] i.e prefixSum = [0]*n.
# Because when we will run the 2nd while loop then in 'prefixSum[j] - prefixSum[q[0]]',
#  the value at index 'q[0]' will get excluded.

# So we need to make prefix array of size = n + 1.

# Note: Here we are 1st checking the condition then we are adding into 'q'.

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n= len(nums)
        prefixSum= [0] *(n+1)  # prefix[i] = sum till index 'i-1'
        for i in range(n):
            prefixSum[i+ 1]= prefixSum[i] + nums[i]
        q= collections.deque()  # will store all the 'i' index of sliding window.(Think like this).
        ans= n + 1
        j= 0  # starting from '1' will give wrong ans. 
        # our last prefixSum is at index 'n' so we will go till 'n'
        while j < n + 1:
            # for handling "+ve num" if found ans then try to shrink just like we used to do.
            # prefixSum[j] - prefixSum[q[0]] : will denote the curSum like other Q i.e here prefix[j] - prefix[i].
            while q and prefixSum[j] - prefixSum[q[0]] >= k:
                ans= min(ans, j - q.popleft())   
            # to handle the "-ve" number.
            # it means the sum from index 'q[-1]' before curr index 'j' is '<= 0'
            #  i.e prefixSum[j] - prefixSum[q[-1]] <= 0.
            
            # so if we start our ans subarray from index 'q[-1]' then it will be longer only because to reach the 
            # sum >= target from index 'q[-1]', we have to include the ele beyond curr index 'j' also.
            # so why to start from that so better remove those indexes.
            # That's why pop all those index.
            while q and prefixSum[j] <= prefixSum[q[-1]]:
                q.pop()
            q.append(j)   # every index can be possible starting index for ans subarray.
            j+= 1
        return ans if ans <=n else -1

# Java Code 
"""
import java.util.*;

class Solution {
    public int shortestSubarray(int[] nums, int k) {
        int n = nums.length;
        long[] prefixSum = new long[n + 1];  // prefix[i] = sum till index 'i-1'
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        Deque<Integer> q = new ArrayDeque<>();  // will store all the 'i' index of sliding window (Think like this).
        int ans = n + 1;
        int j = 0;  // starting from '1' will give wrong ans.

        // our last prefixSum is at index 'n' so we will go till 'n'
        while (j < n + 1) {
            // for handling "+ve num" if found ans then try to shrink just like we used to do.
            // prefixSum[j] - prefixSum[q.peekFirst()] : will denote the curSum like other Q i.e here prefix[j] - prefix[i].
            while (!q.isEmpty() && prefixSum[j] - prefixSum[q.peekFirst()] >= k) {
                ans = Math.min(ans, j - q.pollFirst());
            }

            // to handle the "-ve" number.
            // it means the sum from index 'q[-1]' before curr index 'j' is '<= 0'
            // i.e prefixSum[j] - prefixSum[q[-1]] <= 0.

            // so if we start our ans subarray from index 'q[-1]' then it will be longer only because to reach the
            // sum >= target from index 'q[-1]', we have to include the ele beyond curr index 'j' also.
            // so why to start from that so better remove those indexes.
            // That's why pop all those index.
            while (!q.isEmpty() && prefixSum[j] <= prefixSum[q.peekLast()]) {
                q.pollLast();
            }

            q.offerLast(j);  // every index can be possible starting index for ans subarray.
            j++;
        }

        return ans <= n ? ans : -1;
    }
}

"""

# C++ Code 
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefixSum(n + 1, 0); // prefix[i] = sum till index 'i-1'
        for (int i = 0; i < n; ++i) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        deque<int> q; // will store all the 'i' index of sliding window (Think like this).
        int ans = n + 1;
        int j = 0; // starting from '1' will give wrong ans.

        // our last prefixSum is at index 'n' so we will go till 'n'
        while (j < n + 1) {
            // for handling "+ve num" if found ans then try to shrink just like we used to do.
            // prefixSum[j] - prefixSum[q.front()] : will denote the curSum like other Q i.e here prefix[j] - prefix[i].
            while (!q.empty() && prefixSum[j] - prefixSum[q.front()] >= k) {
                ans = min(ans, j - q.front());
                q.pop_front();
            }

            // to handle the "-ve" number.
            // it means the sum from index 'q[-1]' before curr index 'j' is '<= 0'
            // i.e prefixSum[j] - prefixSum[q.back()] <= 0.

            // so if we start our ans subarray from index 'q[-1]' then it will be longer only because to reach the
            // sum >= target from index 'q[-1]', we have to include the ele beyond curr index 'j' also.
            // so why to start from that so better remove those indexes.
            // That's why pop all those index.
            while (!q.empty() && prefixSum[j] <= prefixSum[q.back()]) {
                q.pop_back();
            }

            q.push_back(j); // every index can be possible starting index for ans subarray.
            j++;
        }

        return ans <= n ? ans : -1;
    }
};

"""

# Extesnion: 

# Note: if you will comment the "2nd while loop" then it will work for "+ve" values
# i.e for question:  "209. Minimum Size Subarray Sum".

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n= len(nums)
        prefixSum= [0] *(n+1)
        for i in range(n):
            prefixSum[i+ 1]= prefixSum[i] + nums[i]
        q= collections.deque()
        ans= n + 1
        j= 0
        while j < n + 1:
            # if found ans then try to shrink just like we used to do for "+ve" values
            while q and prefixSum[j] - prefixSum[q[0]] >= target:
                ans= min(ans, j - q.popleft())
            # while q and prefixSum[j] <= prefixSum[q[-1]]:
            #     q.pop()
            q.append(j) 
            j+= 1
        return ans if ans <=n else 0

# Java Code 
"""
import java.util.*;

class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int[] prefixSum = new int[n + 1];  // prefixSum[i] = sum till index 'i-1'

        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        Deque<Integer> q = new ArrayDeque<>();
        int ans = n + 1;
        int j = 0;

        while (j < n + 1) {
            // if found ans then try to shrink just like we used to do for "+ve" values
            while (!q.isEmpty() && prefixSum[j] - prefixSum[q.peekFirst()] >= target) {
                ans = Math.min(ans, j - q.pollFirst());
            }

            // while (!q.isEmpty() && prefixSum[j] <= prefixSum[q.peekLast()]) {
            //     q.pollLast();
            // }

            q.offerLast(j);
            j++;
        }

        return ans <= n ? ans : 0;
    }
}

"""

# C++ Code 
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        vector<int> prefixSum(n + 1, 0); // prefixSum[i] = sum till index 'i-1'

        for (int i = 0; i < n; ++i) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        deque<int> q;
        int ans = n + 1;
        int j = 0;

        while (j < n + 1) {
            // if found ans then try to shrink just like we used to do for "+ve" values
            while (!q.empty() && prefixSum[j] - prefixSum[q.front()] >= target) {
                ans = min(ans, j - q.front());
                q.pop_front();
            }

            // while (!q.empty() && prefixSum[j] <= prefixSum[q.back()]) {
            //     q.pop_back();
            // }

            q.push_back(j);
            j++;
        }

        return ans <= n ? ans : 0;
    }
};

"""

# Related Q:
# 1) "209. Minimum Size Subarray Sum"
# 2) 239. Sliding Window Maximum
# 3) 1425. Constrained Subsequence Sum


