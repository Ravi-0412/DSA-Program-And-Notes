# Logic: 
"""
First fill to get the 'k' distinct ele then fill the remaining number.
for this we need to fill 'k+1' ele first.

For the first k+ 1 elements, we arrange in the following way: 1, k + 1, 2, k, 3, k - 1, ....
i.e if 'i' is even then res[i]= i//2 + 1 else res[i]= (k + 1) - (i-1)//2.

seeing above pattern
for getting value at even indieces: 1, 2, 3, 4, ... for indices 0,2,4,6, ..., we will do i//2 + 1 
for getting value at odd indices: we will subtract '(i-1)//2' from 'k+1'.

By doing this we will get 'k'th(difference = k), 'k-1'th, 'k-2'th distinct ele between |ai - aj| where j= i + 1

VVI: For the remaining elements, we set a[i] = i + 1, for i = k + 1, ....,n. To main difference between them as '1'.
i.e res[i]= i + 1.
Reason: The smallest unused number will be = i + 1 for remaining one. so just fill them in ascending order to maintain difference of '1'.

Time : O(n)
"""

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]: 
        if k >= n:
            return None
        res= [0]*n
        res[0]= 1
        # filling first 'k' elements
        for i in range(1, k + 1):
            if i % 2== 0:
                res[i]= i//2 + 1   
            else:
                res[i]= (k + 1) - (i-1)//2  
        # now we have got 'k' distinct number. we only need to maintain diff= '1' 
        # filling from 'k+1' to 'n'.
        # Lowest no <= n which would not have been used yet = k + 1
        for i in range(k+1, n):
            res[i]= i + 1
        return res

# Java
"""
import java.util.*;

class Solution {
    public int[] constructArray(int n, int k) {
        if (k >= n) {
            return null;
        }

        int[] res = new int[n];
        res[0] = 1;

        // Filling first 'k' elements
        for (int i = 1; i <= k; i++) {
            if (i % 2 == 0) {
                res[i] = i / 2 + 1;
            } else {
                res[i] = (k + 1) - (i - 1) / 2;
            }
        }

        // Filling the remaining elements with difference of '1'
        for (int i = k + 1; i < n; i++) {
            res[i] = i + 1;
        }

        return res;
    }
}
"""



# Method 2: Better one
# Just easier way to write method 1

# https://leetcode.com/problems/beautiful-arrangement-ii/solutions/1154742/js-python-java-c-simple-mathematical-solution-w-explanation/
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [0] * n
        a , z = 1, k + 1  # 'a' and 'z' will help in filling ans at odd & even places respectively.
        # filling 1st 'k + 1' ele to get 'k' distinct number in difference
        for i in range(k + 1):
            if i % 2 == 0:
                ans[i] = a
                a += 1
            else:
                ans[i] = z
                z -= 1
        for i in range(k + 1, n):
            ans[i] = i + 1
        return ans

# Java
"""
import java.util.*;

class Solution {
    public int[] constructArray(int n, int k) {
        int[] ans = new int[n];
        int a = 1, z = k + 1;

        // Filling the first 'k + 1' elements to get 'k' distinct differences
        for (int i = 0; i <= k; i++) {
            if (i % 2 == 0) {
                ans[i] = a++;
            } else {
                ans[i] = z--;
            }
        }

        // Filling the remaining elements with difference of 1
        for (int i = k + 1; i < n; i++) {
            ans[i] = i + 1;
        }

        return ans;
    }
}
"""
