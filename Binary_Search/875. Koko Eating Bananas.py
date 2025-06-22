# Method 1: 

# the lower bound of the search space is 1, and upper bound is max(piles), 
# because Koko can only choose one pile of bananas to eat every hour. 
# so end= max(piles) 
# time: O(log(max(piles)))

# len(piles) <= 'h' then only koko can eat all the bananas. since in one hour she can eat only one pile
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end, n= 1, max(piles), len(piles)
        while start  < end:
            mid= start+ (end-start)//2
            if self.isValid(piles, h, mid):
                end= mid
            else:
                start= mid+ 1
        return start

    # agar koko is speed se khata h then kya 'h' hour me pura banana kha payega? 
    def isValid(self, piles, h, speed):
        hour= 0
        for pile in piles:
            hour+= math.ceil(pile/speed)
        return hour <= h

# Java Code 
"""
import java.util.*;

class Solution {
    // agar koko is speed se khata h then kya 'h' hour me pura banana kha payega? 
    public boolean isValid(int[] piles, int h, int speed) {
        int hour = 0;
        for (int pile : piles) {
            hour += Math.ceil((double) pile / speed);
        }
        return hour <= h;
    }

    public int minEatingSpeed(int[] piles, int h) {
        int start = 1, end = Arrays.stream(piles).max().getAsInt();

        while (start < end) {
            int mid = start + (end - start) / 2;
            if (isValid(piles, h, mid)) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }

        return start;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    // agar koko is speed se khata h then kya 'h' hour me pura banana kha payega? 
    bool isValid(vector<int>& piles, int h, int speed) {
        int hour = 0;
        for (int pile : piles) {
            hour += ceil((double)pile / speed);
        }
        return hour <= h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int start = 1, end = *max_element(piles.begin(), piles.end());

        while (start < end) {
            int mid = start + (end - start) / 2;
            if (isValid(piles, h, mid)) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }

        return start;
    }
};
"""