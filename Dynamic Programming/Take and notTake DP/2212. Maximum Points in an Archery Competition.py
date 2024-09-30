# Logic : 
"""
Logic: Bob has two choice either : i) don't take current score or 
ii) take current score

To take any score 'k' , bob has to use more number of arrows than 'aliceArrows[k]'
i.e 'aliceArrows[k] + 1' minimum arrows for maximum score .
But skipping any score(Bob loses this score) and taking other can also lead to better answer.
so there is two choice for each score i.e i)  either take that score or ii) not take that score.
"""


# Method 1 : Backtracking
# Time: 
"""
Time: O(2 ^ 12) in avg. But in the worst case it always update the bestScore, 
so it does copy the whole bobArrows, so it takes O(12 * 2^12) in time complexity.
Space: O(1)

"""
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.bestScore = 0
        self.bestBobArrows = None  # bobArrows list
        
        def backtracking(k, remainArrows, score, bobArrows):
            if k == 12:
                if score > self.bestScore:
                    self.bestScore = score
                    self.bestBobArrows = bobArrows.copy()
                return
            
            # Bob loses this score 
            backtracking(k+1, remainArrows, score, bobArrows)
            
            # Bob take this score i.e wins this score
            arrowsNeeded = aliceArrows[k] + 1
            if remainArrows >= arrowsNeeded:
                old = bobArrows[k]
                bobArrows[k] = arrowsNeeded  # set new
                backtracking(k+1, remainArrows - arrowsNeeded, score + k, bobArrows)
                bobArrows[k] = old  # backtrack
                
        backtracking(0, numArrows, 0, [0] * 12)
		# In case of having remain arrows then it means in all sections Bob always win 
        # then we can distribute the remain to any section, here we simple choose first section.
        self.bestBobArrows[0] += numArrows - sum(self.bestBobArrows)
        return self.bestBobArrows

# Java
"""
class Solution {
    private int bestScore;
    private int[] bestBobArrows;
    
    public int[] maximumBobPoints(int numArrows, int[] aliceArrows) {
        bestScore = 0;
        bestBobArrows = new int[12];
        
        backtracking(0, numArrows, 0, new int[12], aliceArrows);
        
        // Distribute remaining arrows if there are any left
        int totalArrowsUsed = sum(bestBobArrows);
        if (numArrows > totalArrowsUsed) {
            bestBobArrows[0] += numArrows - totalArrowsUsed;
        }
        
        return bestBobArrows;
    }
    
    private void backtracking(int k, int remainArrows, int score, int[] bobArrows, int[] aliceArrows) {
        if (k == 12) {
            if (score > bestScore) {
                bestScore = score;
                bestBobArrows = bobArrows.clone();  // copy current state
            }
            return;
        }
        
        // Bob loses this round
        backtracking(k + 1, remainArrows, score, bobArrows, aliceArrows);
        
        // Bob wins this round
        int arrowsNeeded = aliceArrows[k] + 1;
        if (remainArrows >= arrowsNeeded) {
            bobArrows[k] = arrowsNeeded;
            backtracking(k + 1, remainArrows - arrowsNeeded, score + k, bobArrows, aliceArrows);
            bobArrows[k] = 0;  // backtrack
        }
    }
    
    private int sum(int[] arr) {
        int total = 0;
        for (int num : arr) {
            total += num;
        }
        return total;
    }
}
"""


# Later try by top- down and backtracking (solution in sheet).
