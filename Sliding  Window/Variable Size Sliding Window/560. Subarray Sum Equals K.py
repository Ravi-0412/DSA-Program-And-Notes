# brute force
# time: O(n^2)
def SubArray_Sum(arr,k):
    ans= 0
    for i in range(len(arr)):
        wind_sum= 0
        for j in range(i,len(arr)):
            wind_sum+= arr[j]
            if wind_sum== k:
                ans+= 1  
    return ans

# arr= [10, 2, -2, -20, 10]
# k = -10 
arr = [9, 4, 20, 3, 10, 5]
k = 33
# arr= [1,2,3]
# k= 3
# arr= [1,1,1]
# k= 2
# print(SubArray_Sum(arr,k))     


# sliding window but valid only if all number is +ve(> 0).
# time : O(n)
def Count_SubArray(arr,k):
    i,j,win_sum,ans= 0,0,0,0
    while j < len(arr):
        win_sum+= arr[j]
        while i <= j and win_sum > k:
            winSum -= arr[i]
            i += 1
        if win_sum == k:
            ans+= 1      
        j+= 1  # you have to incr 'j' always so better write outside the loop
    return ans

# arr = [9, 4, 20, 3, 10, 5]
# k = 33
# arr= [1,2,3]
# k= 3
arr= [1,1,1,1,2,1]
k= 3
print(Count_SubArray(arr,k))


# better one: just similar to "Two sum" method.
# time: O(n)
# VVI: analyse this Q and previous Q similarity and differences properly
# Draw it on number line then you get the proper visualisation.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans,curr_sum= 0,0
        prefix_sum= {0:1}  # [sum: frequency]  # since we can get diff= 0 also because '-ve' number is also there. 
                          # This will only happen when curSum= k and there will be at least one subarray possible i.e from index '0' to index till now. 
        for n in nums:
            curr_sum+= n
            diff= curr_sum - k  # find the difference
            ans+= prefix_sum.get(diff, 0)  # if diff is present in prefix_sum then it means sum= k is possible when we remove this extra sum "diff"
                                # Also we can say from all those indexes where prefixSum[i] = diff , we can get the curSum by adding 'k'.

            # and add the curr_sum in prefix_sum. if already present then increment the count by its value else add with '1'
            prefix_sum[curr_sum]= 1+ prefix_sum.get(curr_sum, 0) 
        return ans

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public int SubArray_Sum(int[] arr, int k) {
        int ans = 0;
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            int wind_sum = 0;
            for (int j = i; j < n; j++) {
                wind_sum += arr[j];
                if (wind_sum == k) {
                    ans++;
                }
            }
        }
        return ans;
    }
}
//Method 2
class Solution {
    public int Count_SubArray(int[] arr, int k) {
        int i = 0, j = 0, win_sum = 0, ans = 0;
        int n = arr.length;

        while (j < n) {
            win_sum += arr[j];

            while (i <= j && win_sum > k) {
                win_sum -= arr[i];
                i++;
            }

            if (win_sum == k) {
                ans++;
            }

            j++;  // Always increment 'j'
        }
        return ans;
    }
}
//Method 3
import java.util.*;

class Solution {
    public int subarraySum(int[] nums, int k) {
        int ans = 0, curr_sum = 0;
        Map<Integer, Integer> prefix_sum = new HashMap<>();
        prefix_sum.put(0, 1);  // [sum: frequency]

        for (int n : nums) {
            curr_sum += n;
            int diff = curr_sum - k;  // Find the difference

            ans += prefix_sum.getOrDefault(diff, 0);  // If diff is present, subarray sum k is possible

            prefix_sum.put(curr_sum, prefix_sum.getOrDefault(curr_sum, 0) + 1);  // Update frequency
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

using namespace std;

int SubArray_Sum(vector<int>& arr, int k) {
    int ans = 0;
    int n = arr.size();

    for (int i = 0; i < n; i++) {
        int wind_sum = 0;
        for (int j = i; j < n; j++) {
            wind_sum += arr[j];
            if (wind_sum == k) {
                ans++;
            }
        }
    }
    return ans;
}
//Method 2
#include <iostream>
#include <vector>

using namespace std;

int Count_SubArray(vector<int>& arr, int k) {
    int i = 0, j = 0, win_sum = 0, ans = 0;
    int n = arr.size();

    while (j < n) {
        win_sum += arr[j];

        while (i <= j && win_sum > k) {
            win_sum -= arr[i];
            i++;
        }

        if (win_sum == k) {
            ans++;
        }

        j++;  // Always increment 'j'
    }
    return ans;
}
//Method 3
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int ans = 0, curr_sum = 0;
        unordered_map<int, int> prefix_sum = {{0, 1}};  // [sum: frequency]

        for (int n : nums) {
            curr_sum += n;
            int diff = curr_sum - k;  // Find the difference

            ans += prefix_sum[diff];  // If diff is present, subarray sum k is possible

            prefix_sum[curr_sum]++;  // Update frequency of current sum
        }
        return ans;
    }
};
"""
# Note: Extension of this Q and related Q
"""
1) 930. Binary Subarrays With Sum
2) 1248. Count Number of Nice Subarrays
3) Count Subarrays with Given XOR
4) 525. Contiguous Array
5) 974. Subarray Sums Divisible by K
6) vvi:  "1074. Number of Submatrices That Sum to Target"
"""
