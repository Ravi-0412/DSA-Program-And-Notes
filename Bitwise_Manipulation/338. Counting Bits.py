# method 1: 
# apply the logic of counting set bits with "n= n & n-1".

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            x = i
            while x:
                x = x & (x - 1)  # remove the lowest set bit
                count += 1
            res.append(count)
        return res


# Java
"""
class Solution {
    public int[] countBits(int n) {
        int[] res = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            int count = 0;
            int x = i;

            while (x != 0) {
                x = x & (x - 1);  // remove the lowest set bit
                count++;
            }

            res[i] = count;
        }

        return res;
    }
}


"""

# C++
"""
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res(n + 1);

        for (int i = 0; i <= n; i++) {
            int count = 0;
            int x = i;

            while (x != 0) {
                x = x & (x - 1);  // remove the lowest set bit
                count++;
            }

            res[i] = count;
        }

        return res;
    }
};


"""

# method 2:
# write down in notebook you will get this pattern for even and odd number.

# Reason: Agar kisi number ko double kare to binary me bs ek '0' first me badhega baki sb same rhega.
# isliye no of one increase nhi karega agar kisi number ka multiple le binary me.
# e.g: 2 -> 10, 4 -> 100  ;   3 -> 11 , 6 -> 110  ; 5 -> 101 , 10 -> 1010 
# For add number 'num' we need to add '1' to ans of 'num//2'.

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans= [0]*(n+1)
        for num in range(1, n+1):
            if num %2 == 0:
                ans[num]= ans[num//2]
            else: 
                ans[num]= ans[num -1] + 1   # or ans[num]= ans[num//2] +1
        return ans

# Java Code
"""
import java.util.*;

class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];

        for (int num = 1; num <= n; num++) {
            if (num % 2 == 0) {
                ans[num] = ans[num / 2]; // Even numbers have same bit count as num/2
            } else {
                ans[num] = ans[num - 1] + 1; // Odd numbers have one more bit than num-1
            }
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n + 1, 0);

        for (int num = 1; num <= n; num++) {
            if (num % 2 == 0) {
                ans[num] = ans[num / 2]; // Even numbers have same bit count as num/2
            } else {
                ans[num] = ans[num - 1] + 1; // Odd numbers have one more bit than num-1
            }
        }

        return ans;
    }
};
"""