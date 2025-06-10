# Method 1
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
import java.util.*;

class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        StringBuilder b = new StringBuilder();
        for (int n : num) {
            b.append(n);  // first converting the arr into string
        }

        String s = String.valueOf(Long.parseLong(b.toString()) + k);  // converted the array into integer and added 'k' and then into string.
        
        List<Integer> ans = new ArrayList<>();
        for (char c : s.toCharArray()) {
            ans.add(c - '0');  // finally converted the string ans into list
        }
        
        return ans;
    }
}
"""

# C++ 
"""
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        string b;
        for (int n : num) {
            b += to_string(n);  // first converting the arr into string
        }

        string s = to_string(stoll(b) + k);  // converted the array into integer and added 'k' and then into string.

        vector<int> ans;
        for (char c : s) {
            ans.push_back(c - '0');  // finally converted the string ans into list
        }

        return ans;
    }
};

"""

# Method 2: Same as "445. Add Two Numbers II".
# Time = O(n) , space = O(1)
"""
Logic: We are taking k as carry.
We start from the last or lowest digit in array num add k.
Then update k and move untill the highest digit.
After traversing array if carry is > 0 then we add it to begining of num.

Example: `num` = [2,1,5], `k` = 806
At index 2 num = [2, 1, 811] 
So, `k` = 81 and `num` = [2, 1, 1]

At index 1 num = [2, 82, 1]
So, `k` = 8 and `num` = [2, 2, 1]

At index 0 num = [10, 2, 1]
So, `k` = 1 and `num` = [0, 2, 1]

Now `k` > 0
So, we add at the beginning of num
`num` = [1, 0, 2, 1]

Note:  K is at most 5 digit (k <= 10**4) so after loop if k > 0 then time complexity of adding at front won't matter.
"""
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
        List<Integer> result = new ArrayList<>();
        int i = num.length - 1;

        while (i >= 0 || k > 0) {
            if (i >= 0) {
                k += num[i];
                i--;
            }
            result.add(k % 10);
            k /= 10;
        }

        Collections.reverse(result);
        return result;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        vector<int> result;
        int i = num.size() - 1;

        while (i >= 0 || k > 0) {
            if (i >= 0) {
                k += num[i];
                i--;
            }
            result.push_back(k % 10);
            k /= 10;
        }

        reverse(result.begin(), result.end());
        return result;
    }
};
"""
