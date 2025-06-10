# method 1: 

# Time :  O(logN) where N is the number.
# Space : O(logN)

# Logic: just we are checking if we are getting same number then there is cycle.
class Solution:
    def isHappy(self, n: int) -> bool:
        visited= set()
        while n not in visited:  # stopping condition means no can't be happy
            visited.add(n)
            n= self.sumOfsquare(n)
            if n== 1:
                return True
        return False
    
    def sumOfsquare(self, n):
        ans= 0
        while n:
            remainder= n % 10
            ans+= remainder * remainder
            n= n//10
        return ans


# Method 2: 
# Logic: the non-happy number will repeat itself.
# suppose the non-happy number does not repeat it self, the code will stuck in infinite loop and we will never get result back.

# So just we are checking if there is cycle while replacing number with square of sum. 
# If there is cycle then we can check cycle value, if it = 1 then happy else non-happy.

# For detecting cycle, we can use logic of 'detecting cycle' in a linklist i.e 'Floyd Cycle detection algorithm'.

# time: O(n), space : O(1)

class Solution:
    def isHappy(self, n: int) -> bool:

        # Just giving 'sumOfSquareOfDigit(n)'
        def next(n):
            next_no = 0
            while n:
                r = n % 10
                next_no += r *r
                n //= 10
            return next_no
        
        slow = n
        fast = next(n)
        while slow != fast:
            slow = next(slow)
            fast = next(next(fast))
        return slow == 1
        
# Java Code 
"""
    // Method 1: Using a set to track visited numbers

import java.util.HashSet;

class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> visited = new HashSet<>();
        
        while (!visited.contains(n)) { // stopping condition means n can't be happy
            visited.add(n);
            n = sumOfSquare(n);
            if (n == 1) {
                return true;
            }
        }
        return false;
    }
    
    // Helper function to compute sum of squares of digits
    private int sumOfSquare(int n) {
        int ans = 0;
        while (n > 0) {
            int remainder = n % 10;
            ans += remainder * remainder;
            n /= 10;
        }
        return ans;
    }
}

// Method 2: Using Floyd's Cycle Detection Algorithm

class Solution {
    public boolean isHappy(int n) {
        int slow = n, fast = next(n);
        while (slow != fast) {
            slow = next(slow);
            fast = next(next(fast));
        }
        return slow == 1;
    }

    // Helper function to compute sum of squares of digits
    private int next(int num) {
        int next_no = 0;
        while (num > 0) {
            int r = num % 10;
            next_no += r * r;
            num /= 10;
        }
        return next_no;
    }
}
"""

# C++ Code 
"""
#include <unordered_set>
using namespace std;

class Solution {
public:
    // Method 1: Using a set to track visited numbers
    bool isHappy(int n) {
        unordered_set<int> visited;
        
        while (visited.find(n) == visited.end()) { // stopping condition means n can't be happy
            visited.insert(n);
            n = sumOfSquare(n);
            if (n == 1) {
                return true;
            }
        }
        return false;
    }
    
private:
    // Helper function to compute sum of squares of digits
    int sumOfSquare(int n) {
        int ans = 0;
        while (n) {
            int remainder = n % 10;
            ans += remainder * remainder;
            n /= 10;
        }
        return ans;
    }
};

// Method 2: Using Floyd's Cycle Detection Algorithm

class Solution {
public:
    bool isHappy(int n) {
        int slow = n, fast = next(n);
        while (slow != fast) {
            slow = next(slow);
            fast = next(next(fast));
        }
        return slow == 1;
    }

private:
    // Helper function to compute sum of squares of digits
    int next(int num) {
        int next_no = 0;
        while (num) {
            int r = num % 10;
            next_no += r * r;
            num /= 10;
        }
        return next_no;
    }
};

"""
