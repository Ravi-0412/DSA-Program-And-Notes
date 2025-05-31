# time= space= O(n)

"""
since we need the given array as integer, so for this first converted into string and then to integer.
then add with 'k'.
after that then again convert the num we go6 after addition into string and then convert into list 
finally return ans
Not a good way because of this much conversion.
"""

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        b= "".join(str(n) for n in num)  # first converting the arr into string
        s= str(int(b) + k)    # converted the array into integer and added 'k' and then into string.
        ans= [int(c) for c in s]   # fianlly converted the atring ans into list 
        return ans

# Java
"""
class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> result = new ArrayList<>();
        int n = num.length;
        int i = n - 1;
        while (i >= 0 || k > 0) {
            if (i >= 0) k += num[i--];
            result.add(0, k % 10);
            k /= 10;
        }
        return result;
    }
}
"""

# C++ 
"""
class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        vector<int> result;
        int i = num.size() - 1;
        while (i >= 0 || k > 0) {
            if (i >= 0) k += num[i--];
            result.insert(result.begin(), k % 10);
            k /= 10;
        }
        return result;
    }
};
"""
# Method 2: Same as "445. Add Two Numbers II".
# Shortcut and very good  method

# Logic: We are taking k as carry.
# We start from the last or lowest digit in array num add k.
# Then update k and move untill the highest digit.
# After traversing array if carry is > 0 then we add it to begining of num.

# Example: `num` = [2,1,5], `k` = 806
# At index 2 num = [2, 1, 811] 
# So, `k` = 81 and `num` = [2, 1, 1]

# At index 1 num = [2, 82, 1]
# So, `k` = 8 and `num` = [2, 2, 1]

# At index 0 num = [10, 2, 1]
# So, `k` = 1 and `num` = [0, 2, 1]

# Now `k` > 0
# So, we add at the beginning of num
# `num` = [1, 0, 2, 1]

# Note:  K is at most 5 digit (k <= 10**4) so after loop if k > 0 then time complexity of adding at front won't matter.

# Time = O(n) , space = O(1)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        for i in range(n-1, -1, -1):
            k , num[i] = divmod(num[i] + k , 10)
        while k > 0:
            k , a = divmod(k , 10)
            num = [a] + num
        
        return num

# Other way (More better)
from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        i = len(num) - 1
        
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1
            
            result.append(k % 10)
            k //= 10
        
        result.reverse()
        return result


# Java
"""
import java.util.*;

class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        int n = num.length;
        List<Integer> result = new ArrayList<>();
        
        for (int i = n - 1; i >= 0; i--) {
            k += num[i]; 
            result.add(k % 10);
            k /= 10;
        }
        
        while (k > 0) {
            result.add(k % 10);
            k /= 10;
        }
        
        Collections.reverse(result);
        return result;
    }
}
"""
