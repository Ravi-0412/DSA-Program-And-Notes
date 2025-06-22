# Basic: 

# But this is interesting one because of :
# 1) even no of piles
# 2) Alice will start first
# 3) The total number of stones across all the piles is odd, so there are no ties.

# Note: from above constraint , player who will start first will only win even both plays optimally.
# how? => just calculate the sum of odd and even places if odd places sum is greater than even places then choose only odd places .And same if even places has higher sum.


# Alex is first to pick pile.
# piles.length is even, and this lead to an interesting fact:
# Alex can always pick odd piles or always pick even piles!

# For example,
# If Alex wants to pick even indexed piles piles[0], piles[2], ....., piles[n-2],
# he picks first piles[0], then Bob can pick either piles[1] or piles[n - 1].
# Every turn, Alex can always pick even indexed piles and Bob can only pick odd indexed piles.

# In the description, we know that sum(piles) is odd.
# If sum(piles[even]) > sum(piles[odd]), Alex just picks all evens and wins.
# If sum(piles[even]) < sum(piles[odd]), Alex just picks all odds and wins.

# So, Alex always defeats Bob in this game.

# That's why simply return True 


# method 1:
# totally same as 486. predict winner, so didn't submit.

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n= len(piles)
        AliceScore= self.FindScore(piles, 0, n-1)
        return AliceScore >= sum(piles) - AliceScore
    
    def FindScore(self, nums, i, j):
        if i > j:
            return 0
        if i== j:  # only one ele remaining. both indexes are included so.
            return nums[i]
        return max(nums[i] + min(self.FindScore(nums, i +2, j), self.FindScore(nums, i +1, j-1)),
                nums[j] + min(self.FindScore(nums, i , j-2), self.FindScore(nums, i+1 , j-1)))

# Java Code 
"""
class Solution {
    public boolean stoneGame(int[] piles) {
        int n = piles.length;
        int AliceScore = findScore(piles, 0, n - 1);
        int total = 0;
        for (int p : piles) total += p;
        return AliceScore >= total - AliceScore;
    }

    public int findScore(int[] nums, int i, int j) {
        if (i > j)
            return 0;
        if (i == j)  // only one ele remaining. both indexes are included so.
            return nums[i];

        return Math.max(
            nums[i] + Math.min(findScore(nums, i + 2, j), findScore(nums, i + 1, j - 1)),
            nums[j] + Math.min(findScore(nums, i, j - 2), findScore(nums, i + 1, j - 1))
        );
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int n = piles.size();
        int AliceScore = findScore(piles, 0, n - 1);
        int total = 0;
        for (int p : piles) total += p;
        return AliceScore >= total - AliceScore;
    }

    int findScore(vector<int>& nums, int i, int j) {
        if (i > j)
            return 0;
        if (i == j)  // only one ele remaining. both indexes are included so.
            return nums[i];

        return max(
            nums[i] + min(findScore(nums, i + 2, j), findScore(nums, i + 1, j - 1)),
            nums[j] + min(findScore(nums, i, j - 2), findScore(nums, i + 1, j - 1))
        );
    }
};
"""
