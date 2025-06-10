# method 1: 
# logic: Are we have enough coins to generate next row?
# if yes then decrease the coin by current row number and increase the number of row by '1'.

# time: Sqrt(n)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        row= 1
        while n >= row:
            n-= row
            row+= 1
        return row -1   # '-1' because last row is incomplete. 


# method 2:
# just solve the quadratic equation: (K * (K+1))/2 <= N
# at last we will get: K <= sqrt(2N + 1/4) - 1/2

# How we came at this?
# 1st row we need '1' coin, 2nd coin -> 2, 3rd coin -> 3 and so on.
# so if there is 'k' rows then total number of coins used in making 'k' rows must be less than 'N'.
# i.e Summation from '1' to 'k' <= N => (K * (K+1))/2 <= N


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.sqrt(2*n + 1/4)- 1/2)
    

# method 3: Best
# using binary search

# How to think of binary search?
# number of coins required for the kth row will be equal to 1 + 2 + 3 + ... + k = k * (k + 1) / 2.

# logic: just we find the 'last index of an element'.

# Time: O(logn)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        start= 1
        end= n
        while start <= end:
            row= start + (end- start)//2  # just like mid
            # find the no of coins required to form till row no= row
            coinsNeeded= (row *(row + 1))//2
            # we may form more rows.
            if n>= coinsNeeded:
                start= row + 1
            else:
                end= row -1
        return end

# Java Code 
"""
//Method 1
class Solution {
    public int arrangeCoins(int n) {
        int row = 1;
        while (n >= row) {
            n -= row;
            row++;
        }
        return row - 1; // '-1' because last row is incomplete
    }
}
//Method 2
class Solution {
    public int arrangeCoins(int n) {
        return (int)(Math.sqrt(2.0 * n + 0.25) - 0.5);
    }
}
//Method 3
class Solution {
    public int arrangeCoins(int n) {
        int start = 1, end = n;

        while (start <= end) {
            long row = start + (end - start) / 2; // Calculate mid (potential row count)
            long coinsNeeded = (row * (row + 1)) / 2; // Total coins required for `row` rows

            if (coinsNeeded == n) { // Exactly fills all rows
                return (int) row;
            }
            if (coinsNeeded < n) { // Try forming more rows
                start = (int) (row + 1);
            } else { // Reduce row count if too many coins are required
                end = (int) (row - 1);
            }
        }
        return end; // `end` represents the last fully completed row
    }
}
"""

# C++ Code 
"""
//Method 1
class Solution {
public:
    int arrangeCoins(int n) {
        int row = 1;
        while (n >= row) {
            n -= row;
            row++;
        }
        return row - 1; // '-1' because last row is incomplete
    }
};
//Method 2
#include <cmath>

class Solution {
public:
    int arrangeCoins(int n) {
        return int(sqrt(2.0 * n + 0.25) - 0.5);
    }
};
//Method 3
class Solution {
public:
    int arrangeCoins(int n) {
        int start = 1, end = n;

        while (start <= end) {
            long row = start + (end - start) / 2; // Just like mid
            long coinsNeeded = (row * (row + 1)) / 2;

            if (n >= coinsNeeded) { // We may form more rows
                start = row + 1;
            } else {
                end = row - 1;
            }
        }
        return end; // Last index where complete rows were formed
    }
};
"""