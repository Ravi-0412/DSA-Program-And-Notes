"""
For every index, we have two choice: either take or notTake.

Time: O(n*n*10) , 10: length of words to check hamming distance between them
"""

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]  # dp[cur][pre + 1] handles -1 index safely

        def hammingDistance(a: str, b: str) -> int:
            # Hamming distance: count differing characters at same positions
            return sum(x != y for x, y in zip(a, b))

        def solve(cur: int, pre: int) -> List[str]:
            if cur >= n:
                return []
            
            if dp[cur][pre + 1] != []:
                return dp[cur][pre + 1]

            notTake = solve(cur + 1, pre)

            take = []
            # Valid if first word (pre == -1) OR meets all 3 conditions:
            # - different groups
            # - same word length
            # - hamming distance = 1
            if pre == -1 or (
                groups[cur] != groups[pre]
                and len(words[cur]) == len(words[pre])
                and hammingDistance(words[cur], words[pre]) == 1
            ):
                take = [words[cur]] + solve(cur + 1, cur)

            dp[cur][pre + 1] = take if len(take) > len(notTake) else notTake
            return dp[cur][pre + 1]

        return solve(0, -1)

# Java
"""
import java.util.*;

public class Solution {
    public List<String> getWordsInLongestSubsequence(String[] words, int[] groups) {
        int n = words.length;
        List<String>[][] dp = new ArrayList[n + 1][n + 1]; // Use pre+1 indexing

        for (int i = 0; i <= n; i++) {
            Arrays.fill(dp[i], null);
        }

        return solve(0, -1, words, groups, dp);
    }

    private List<String> solve(int cur, int pre, String[] words, int[] groups, List<String>[][] dp) {
        int n = words.length;

        if (cur >= n) return new ArrayList<>();

        if (dp[cur][pre + 1] != null) return dp[cur][pre + 1];

        // Option 1: skip the current word
        List<String> notTake = solve(cur + 1, pre, words, groups, dp);

        // Option 2: take the current word if valid
        List<String> take = new ArrayList<>();

        if (pre == -1 || (
            groups[cur] != groups[pre] &&
            words[cur].length() == words[pre].length() &&
            hammingDistance(words[cur], words[pre]) == 1
        )) {
            take.add(words[cur]);
            take.addAll(solve(cur + 1, cur, words, groups, dp));
        }

        // Store the longer list
        dp[cur][pre + 1] = take.size() > notTake.size() ? take : notTake;
        return dp[cur][pre + 1];
    }

    // Hamming distance: count differing positions between equal-length strings
    private int hammingDistance(String a, String b) {
        int dist = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                dist++;
            }
        }
        return dist;
    }
}
"""
