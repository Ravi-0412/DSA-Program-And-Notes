"""
Logic: just find the no of pairs whose sum is divisible by 'k' where k= 60.
Intitution: When see any number 'num' then, how can we find no of element that we can take with current
number 'num' to make pair sum divisible by 'k'?
We will have to find 'count[k - remainder]'.
so for this we will have to store 'count of remainer in a map'.
But if remainder ==0 then we will have to take count of 'k' only so if remainder == 0
then, we will increment count of 'k'.

Also:
Given 2 nums 'a' and 'b':
If a % k == x and b % k == k - x 
then (a + b) is divisible by k

proof: 
 a % k == x
 b % k == k - x
 (a + b) % k = ((a + b)%k)%k = (a%k + b%k)%k = (x + k - x)%k = k%k = 0 
 Hence, (a + b) % k == 0 and (a + b) is divisible by k.

OR
a%k = x             =>       a = nk+x
b%k = k-x           =>       b = mk+k-x
a+b = nk+mk+k+x-x   =>       a+b = (m+n+1)k    => (a+b) % k = 0

So here for every number 'a', we are searching for 'b'.

# Time : O(n), sapce : O(k)
"""
import collections
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        k = 60
        count = collections.defaultdict(int)
        ans = 0
        for t in time:
            remainder = t % k
            ans += count[k - remainder]
            if remainder == 0:
                # we will have to take count of 'k' only becuase next number will search for 'k'
                count[k] += 1
            else:
                count[remainder] += 1
        return ans

# Java Code 
"""
import java.util.HashMap;
import java.util.List;

class Solution {
    public int numPairsDivisibleBy60(List<Integer> time) {
        int k = 60;
        HashMap<Integer, Integer> count = new HashMap<>(); // Stores frequency of remainders
        int ans = 0;

        for (int t : time) {
            int remainder = t % k;
            ans += count.getOrDefault(k - remainder, 0); // Count pairs forming divisible sum

            if (remainder == 0) {
                // Count 'k' as some future number may search for 'k'
                count.put(k, count.getOrDefault(k, 0) + 1);
            } else {
                count.put(remainder, count.getOrDefault(remainder, 0) + 1);
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
using namespace std;

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int k = 60;
        unordered_map<int, int> count; // Stores frequency of remainders
        int ans = 0;

        for (int t : time) {
            int remainder = t % k;
            ans += count[k - remainder]; // Count pairs forming divisible sum

            if (remainder == 0) {
                // Count 'k' as some future number may search for 'k'
                count[k]++;
            } else {
                count[remainder]++;
            }
        }
        return ans;
    }
};
"""