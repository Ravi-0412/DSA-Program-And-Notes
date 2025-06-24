# method 1: 

# just same as "Allocate minimum pages". in this we have to find the maximum instead of 'minimum' that's it.
# here we are checking for valid position for placing cow then updating the 'lastcowPOSITION',
# as here we have to palce when we will find any position.

# time: O(nlogn)
# just like we find the last index of an element in sorted array.
class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()   # we will place the cow at the leftmost available stall. so to know the 
                        # distance between the position of stall at which last cow is placed , sorting will make our work easy.
        low= 1    # minimum difference we can get is '1'.
        up=  stalls[n-1] - stalls[0]   # maximum difference can be this only when one is placed at start and one at last
        while low <= up:
            mid= low+ (up- low)//2
            # check if we can place all the cows with minDistance as 'mid'
            if self.isPossible(stalls, mid, k):  # if we can place all the cows with minDistance as 'mid'
                                                # then try to increase the minDistance so incr 'low'. or bda ans khojo.
                low= mid + 1   # search for even more bigger
            else:  # if not able to place then try to decr the minDistance so decr 'up'
                up= mid - 1
        return up

    def isPossible(self, stalls, minDistance, k):  # given a distance, tell whether we can place all cow with minimum distance between any of them = 'distance'?
        cows= 1  # we start to place 1st cow at stall[0]
        lastCowPosition= stalls[0]  # we always try at leftmost available position
        for i in range(len(stalls)):
            # only place the cow if diff  between 'curr stall number and lastcowPosition' is >= minDistance.
            if stalls[i]- lastCowPosition >= minDistance:   # if difference is >= minDistance then hm yahan pe dusra cow ko rakh sakte h.
                # means we can place the the next cow at stall[i]
                cows+= 1
                lastCowPosition= stalls[i]
                # check if we have already placed all the cows
                if cows >= k:
                    return True
        return False

# Java Code 
"""
import java.util.Arrays;

public class Solution {
    public int solve(int n, int k, int[] stalls) {
        Arrays.sort(stalls);  // we will place the cow at the leftmost available stall.
                              // so to know the distance between the position of stall at which last cow is placed,
                              // sorting will make our work easy.
        int low = 1;  // minimum difference we can get is '1'.
        int up = stalls[n - 1] - stalls[0];  // maximum difference can be this only when one is placed at start and one at last

        while (low <= up) {
            int mid = low + (up - low) / 2;
            // check if we can place all the cows with minDistance as 'mid'
            if (isPossible(stalls, mid, k)) {
                low = mid + 1;  // search for even more bigger
            } else {
                up = mid - 1;   // try to decrease the minDistance
            }
        }
        return up;
    }

    // given a distance, tell whether we can place all cows with minimum distance between any of them = 'distance'?
    private boolean isPossible(int[] stalls, int minDistance, int k) {
        int cows = 1;  // we start to place 1st cow at stall[0]
        int lastCowPosition = stalls[0];  // we always try at leftmost available position

        for (int i = 1; i < stalls.length; i++) {
            // only place the cow if diff between 'curr stall number and lastCowPosition' is >= minDistance.
            if (stalls[i] - lastCowPosition >= minDistance) {  // we can place the next cow at stall[i]
                cows++;
                lastCowPosition = stalls[i];
                // check if we have already placed all the cows
                if (cows >= k) return true;
            }
        }
        return false;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <algorithm>

class Solution {
public:
    int solve(int n, int k, std::vector<int>& stalls) {
        std::sort(stalls.begin(), stalls.end());  // we will place the cow at the leftmost available stall.
                                                  // sorting will make our work easy.
        int low = 1;  // minimum difference we can get is '1'.
        int up = stalls[n - 1] - stalls[0];  // maximum difference when one cow is at start and one at last

        while (low <= up) {
            int mid = low + (up - low) / 2;
            // check if we can place all the cows with minDistance as 'mid'
            if (isPossible(stalls, mid, k)) {
                low = mid + 1;  // search for even more bigger
            } else {
                up = mid - 1;   // try to decrease the minDistance
            }
        }
        return up;
    }

private:
    // given a distance, tell whether we can place all cows with minimum distance between any of them = 'distance'?
    bool isPossible(const std::vector<int>& stalls, int minDistance, int k) {
        int cows = 1;  // we start to place 1st cow at stall[0]
        int lastCowPosition = stalls[0];  // try to place at the leftmost available stall

        for (int i = 1; i < stalls.size(); ++i) {
            if (stalls[i] - lastCowPosition >= minDistance) {  // we can place the next cow at stall[i]
                cows++;
                lastCowPosition = stalls[i];
                // check if we have already placed all the cows
                if (cows >= k) return true;
            }
        }
        return false;
    }
};
"""