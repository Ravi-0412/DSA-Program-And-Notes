"""
This problem is similar to Longest Increasing Subsequence problem.
The difference is that we need to consider the arithmetic difference in this problem.

LIS: me sirf bda dikha add kar diye but yahan difference bhi track karna hoga.
we need to keep track of difference as well with length i.e
Hmko har index pe, har possible difference ka AP ka length track karna hoga.

How to keep track of the length as well as the difference? 
We can use a hashmap, whose key is the (index, difference) and value is the length.

for two elements A[i] and A[j] where i < j, 
the difference between A[i] and A[j] (name it diff). 
If the hashmap at position j has the key 'diff', it means that there is 
an arithmetic subsequence ending at index j, with arithmetic difference 'diff' and length 'dp[j][diff]'. 
And we just add the length by 1. If hashmap does not have the key diff, then those two elements can form a 2-length arithmetic subsequence.

Note: LIS me bda dekh ke add kar rhe the '+1' usi 'j' wale ka length me, 
Yahan diff dekh ke add karenge i.e agar same diff ka AP h tb add karenge.

here dp[(i, diff)]= gives the sequence length of possible diff ending at index 'i'.

time: O(n^2)
"""

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n= len(nums)
        dp = collections.defaultdict()
        for i in range(n):
            for j in range(i):
                diff= nums[i] - nums[j]
                # Agar is diff ka koi sequence index 'j' pe h tb uska length me  add kar do '+1'
                # Nhi to ye dono dono ko mila ke ek nya sequence bna ko at index 'i' having length= 2
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
        return max(dp.values())

# Java Code 
"""
import java.util.*;

class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        Map<String, Integer> dp = new HashMap<>();
        int max = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int diff = nums[i] - nums[j];

                // Agar is diff ka koi sequence index 'j' pe h tb uska length me add kar do '+1'
                // Nhi to ye dono dono ko mila ke ek nya sequence bna lo at index 'i' having length = 2
                String key = i + "," + diff;
                String prevKey = j + "," + diff;

                int len = dp.getOrDefault(prevKey, 1) + 1;
                dp.put(key, len);
                max = Math.max(max, len);
            }
        }

        return max;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        int n = nums.size();
        unordered_map<string, int> dp;
        int maxLen = 0;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                int diff = nums[i] - nums[j];

                // Agar is diff ka koi sequence index 'j' pe h tb uska length me add kar do '+1'
                // Nhi to ye dono dono ko mila ke ek nya sequence bna lo at index 'i' having length = 2
                string key = to_string(i) + "," + to_string(diff);
                string prevKey = to_string(j) + "," + to_string(diff);

                int len = dp.count(prevKey) ? dp[prevKey] + 1 : 2;
                dp[key] = len;
                maxLen = max(maxLen, len);
            }
        }

        return maxLen;
    }
};
"""

# Note vvi: for  Q: "1218. Longest Arithmetic Subsequence of Given Difference" i.e 
# return the length of the longest subsequence in arr which is an arithmetic sequence 
# such that the difference between adjacent elements in the subsequence equals difference.

# I did like above but got TLE due to n= 10^5.

# Done optimisation of this q in hashing. See there 
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n= len(arr)
        dp = collections.defaultdict()
        for i in range(n):
            for j in range(i):
                diff= arr[i] - arr[j]
                if diff != difference:
                    continue
                # Agar is diff ka koi sequence index 'j' pe h tb uska length me  add kar do '+1'
                # Nhi to ye dono dono ko mila ke ek nya sequence bna ko at index 'i' having length= 2
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
        # Ab give difference ka Ap ka max length return kar do.
        ans = 1
        for key, value in dp.items():
            if key[1] == difference:
                ans = max(ans, value)
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        int n = arr.length;
        Map<String, Integer> dp = new HashMap<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int diff = arr[i] - arr[j];

                if (diff != difference)
                    continue;

                // Agar is diff ka koi sequence index 'j' pe h tb uska length me add kar do '+1'
                // Nhi to ye dono dono ko mila ke ek nya sequence bna lo at index 'i' having length = 2
                String key = i + "," + diff;
                String prevKey = j + "," + diff;

                dp.put(key, dp.getOrDefault(prevKey, 1) + 1);
            }
        }

        // Ab given difference ka Ap ka max length return kar do.
        int ans = 1;
        for (Map.Entry<String, Integer> entry : dp.entrySet()) {
            String key = entry.getKey();
            int val = entry.getValue();

            if (Integer.parseInt(key.split(",")[1]) == difference) {
                ans = Math.max(ans, val);
            }
        }

        return ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        int n = arr.size();
        unordered_map<string, int> dp;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                int diff = arr[i] - arr[j];

                if (diff != difference)
                    continue;

                // Agar is diff ka koi sequence index 'j' pe h tb uska length me add kar do '+1'
                // Nhi to ye dono dono ko mila ke ek nya sequence bna lo at index 'i' having length = 2
                string key = to_string(i) + "," + to_string(diff);
                string prevKey = to_string(j) + "," + to_string(diff);

                dp[key] = dp.count(prevKey) ? dp[prevKey] + 1 : 2;
            }
        }

        // Ab given difference ka Ap ka max length return kar do.
        int ans = 1;
        for (auto& [key, val] : dp) {
            size_t comma = key.find(',');
            int diff = stoi(key.substr(comma + 1));
            if (diff == difference) {
                ans = max(ans, val);
            }
        }

        return ans;
    }
};
"""
