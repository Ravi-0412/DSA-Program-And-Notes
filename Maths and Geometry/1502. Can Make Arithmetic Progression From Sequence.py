# method 1: Brute force
# logic: just sort and check if diff between each adjacent pair is same.

# time: O(n*logn), space: O(1)

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff= arr[1] - arr[0]
        pre= arr[1]
        for i in range(2, len(arr)):
            if arr[i] - pre != diff:
                return False
            pre= arr[i]
        return True
    

# method 2: 
"""
logic: find the diff first.
we get the max_number in AP using 'min_number + (n-1)*diff' . From this we can get the difference.
diff= (max(nums) - min(nums)) / (n-1).

then we have starting ele of AP and diff so we can check if next ele of sequence is present or not.
next= min(nums) +  i * diff, i= 1, 2, 3,....n-1

time= space= O(n)
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n= len(arr)
        s= set(arr)   # storing all unique ele in a set 's'.
        minimum= min(arr) # finding min ele of arr
        maximum= max(arr) # Finding max ele of arr
        diff= (maximum - minimum) /(n-1)  # finding the diff between ele
        for i in range(1, len(arr)):
            next= minimum + i * diff
            if next not in s:
                return False
        return True


# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);
        int diff = arr[1] - arr[0];
        int pre = arr[1];

        for (int i = 2; i < arr.length; i++) {
            if (arr[i] - pre != diff) {
                return false;
            }
            pre = arr[i];
        }
        return true;
    }
}
//Method 2
import java.util.*;

class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        int n = arr.length;
        Set<Integer> s = new HashSet<>();
        for (int num : arr) {
            s.add(num);
        }

        int minimum = Arrays.stream(arr).min().getAsInt();
        int maximum = Arrays.stream(arr).max().getAsInt();
        double diff = (double)(maximum - minimum) / (n - 1);

        for (int i = 1; i < n; i++) {
            int next = minimum + i * (int)diff;
            if (!s.contains(next)) {
                return false;
            }
        }
        return true;
    }
}
"""

# C++ Code 
"""
//Method 1
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int diff = arr[1] - arr[0];
        int pre = arr[1];

        for (int i = 2; i < arr.size(); i++) {
            if (arr[i] - pre != diff) {
                return false;
            }
            pre = arr[i];
        }
        return true;
    }
};
//Method 2
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        int n = arr.size();
        unordered_set<int> s(arr.begin(), arr.end());
        int minimum = *min_element(arr.begin(), arr.end());
        int maximum = *max_element(arr.begin(), arr.end());
        double diff = (double)(maximum - minimum) / (n - 1);

        for (int i = 1; i < n; i++) {
            int next = minimum + i * diff;
            if (s.find(next) == s.end()) {
                return false;
            }
        }
        return true;
    }
};
"""

# method 3: Try Later.
# optimising space to (1).
# time: O(n), space O(1)
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/solutions/720152/o-n-time-o-1-space/
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/solutions/721352/c-counting-sort-solution-with-o-n-and-o-1-complexity/