# Method 1: 

# exactly same as "22. generate valid parantheis"

# In above Q: No of '(' will be always >= no of ')'.

# Just replace '(' -> 1 and ')' -> 0.

# Q: we have to fill 'n' boxes in such a way that no of '1' is >= no of '0' for all prefix.
# logic in Q: "22. generate valid parantheis"

class Solution:
    def NBitBinary(self, N):
        ans= []
        
        def AllNumber(noOne, noZero, number):
            if noOne + noZero== N:
                ans.append(number)
                return
            if noOne < N:
                AllNumber(noOne + 1, noZero, number + "1")
            if noZero < noOne:
                AllNumber(noOne , noZero + 1, number + "0")
        
        AllNumber(0,0,"")  # (noOne, noZero, number)
        return ans


# Java Code 
"""
import java.util.*;

class Solution {
    List<String> ans = new ArrayList<>();

    private void AllNumber(int noOne, int noZero, String number, int N) {
        if (noOne + noZero == N) {  
            // means we have generated one valid N-bit binary number.
            ans.add(number);
            return;
        }
        // Can only add '1' if the number of ones is less than N
        if (noOne < N) {
            AllNumber(noOne + 1, noZero, number + "1", N);
        }
        // Can only add '0' if the number of zeros is less than the number of ones
        if (noZero < noOne) {
            AllNumber(noOne, noZero + 1, number + "0", N);
        }
    }

    public List<String> NBitBinary(int N) {
        ans.clear();
        AllNumber(0, 0, "", N);  // (noOne, noZero, number)
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
    vector<string> ans;

    void AllNumber(int noOne, int noZero, string number, int N) {
        if (noOne + noZero == N) {  
            // means we have generated one valid N-bit binary number.
            ans.push_back(number);
            return;
        }
        // Can only add '1' if the number of ones is less than N
        if (noOne < N) {
            AllNumber(noOne + 1, noZero, number + "1", N);
        }
        // Can only add '0' if the number of zeros is less than the number of ones
        if (noZero < noOne) {
            AllNumber(noOne, noZero + 1, number + "0", N);
        }
    }

    vector<string> NBitBinary(int N) {
        ans.clear();
        AllNumber(0, 0, "", N);  // (noOne, noZero, number)
        return ans;
    }
};
"""
