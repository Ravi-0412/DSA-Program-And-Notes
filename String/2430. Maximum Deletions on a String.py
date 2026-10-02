# Time : O(N^3)

class Solution:
      def deleteString(self, s: str) -> int:
          n = len(s)

          # dp[i] = most operations needed to delete the suffix s[i:]
          # -1 means this suffix hasn't been computed yet                                                                                                                                                                       
          dp = [-1] * n

          def dfs(i):
              # Base case: empty suffix, nothing left to delete
              if i == n:
                  return 0

              # Memo hit: this suffix is already solved                                                                                                                                                                         
              if dp[i] != -1:
                  return dp[i]

              # Fallback: delete the whole remaining suffix in one operation
              ans = 1
  
              # Try every prefix length k where s[i:i+k] could repeat right after itself.
              # k can be at most half the remaining length, since two copies must fit.
              for k in range(1, (n - i) // 2 + 1):
                  # If the next k chars equal the following k chars, we can delete
                  # the first copy (1 operation) and then solve the rest from i + k
                  if s[i : i + k] == s[i + k : i + 2 * k]:
                      ans = max(ans, 1 + dfs(i + k))

              # Save the best result for this suffix
              dp[i] = ans
              return ans
  
          # Answer for the full string
          return dfs(0)

  # Other way 
  class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 0
            ans = 0
            for k in range(1, (n - i) // 2 + 1):
                if s[i : i + k] == s[i + k: i + 2 * k]:
                    ans = max(ans, dfs(i + k))
            return ans + 1  # aage ka find karke one add kar do 

        return dfs(0)

# Method 2: Tabulation

class Solution:
      def deleteString(self, s: str) -> int:
          n = len(s)

          dp = [0] * (n + 1)                    # size n+1: the base case uses index n
          dp[n] = 0                             # base case: if i == n: return 0

          for i in range(n - 1, -1, -1):        # dfs(i) needs dfs(i + k), a larger index → fill from right to left
              ans = 1
              for k in range(1, (n - i) // 2 + 1):
                  if s[i : i + k] == s[i + k: i + 2 * k]:
                      ans = max(ans, 1 + dp[i + k])   # dfs(i + k) → dp[i + k]
              dp[i] = ans

          return dp[0]                          # dfs(0) → dp[0]


# Method 3:
"""
Gap: the slice check redoes work

  The tabulation is O(n³), because every check s[i:i+k] == s[i+k:i+2k] compares up to k characters from scratch.

  Ask: "is the comparison at (i, i+k) related to an earlier comparison?" Yes:
  compare s starting at i   with s starting at j:      a b c …   vs   a b c …
  compare s starting at i+1 with s starting at j+1:      b c …   vs     b c …
                                                       ↑ one character shorter, already computed
  If s[i] == s[j], the matching length from (i, j) is one more than the matching length from (i+1, j+1).

  Method 1: Precompute the LCP table

  LCP = longest common prefix: lcp[i][j] is how many characters match when you read s from position i and from position j side by side.

  lcp[i][j] = lcp[i+1][j+1] + 1   if s[i] == s[j]
            = 0                    otherwise

  The check becomes O(1): the first k characters starting at i equal the next k characters exactly when at least k characters match from positions i and i+k:
  s[i:i+k] == s[i+k:i+2k]   ⇔   lcp[i][i+k] >= k
  
  Example:
  s = "abab"
  lcp[0][2]: s[0]='a' == s[2]='a' → lcp[1][3] + 1
  lcp[1][3]: s[1]='b' == s[3]='b' → lcp[2][4] + 1 = 0 + 1 = 1
  → lcp[0][2] = 2
  
  i=0, k=2: lcp[0][2] = 2 ≥ 2 → "ab" == "ab" ✓  (no slicing needed)

The only line that differs from your tabulation:
  yours:     if s[i : i + k] == s[i + k: i + 2 * k]:     O(k) per check
  version A: if lcp[i][i + k] >= k:                       O(1) per check

Time = O(N^2) = space
"""

class Solution:
      def deleteString(self, s: str) -> int:
          n = len(s)
  
          # Phase 1: lcp[i][j] = how many characters match reading from i and from j
          lcp = [[0] * (n + 1) for _ in range(n + 1)]   # row/col n = past the end → 0
          for i in range(n - 1, -1, -1):
              for j in range(n - 1, i, -1):
                  if s[i] == s[j]:
                      lcp[i][j] = lcp[i + 1][j + 1] + 1  # one more than the match from (i+1, j+1)

          # Phase 2: the same DP as your tabulation, with the slice check replaced by lcp
          dp = [0] * (n + 1)
          for i in range(n - 1, -1, -1):
              ans = 1
              for k in range(1, (n - i) // 2 + 1):
                  if lcp[i][i + k] >= k:                 # was: s[i:i+k] == s[i+k:i+2k]
                      ans = max(ans, 1 + dp[i + k])
              dp[i] = ans
          return dp[0]

# Optimising Space to O(N) for Method 3
"""
 Gap: which rows of lcp are actually used?

  Look at the two places lcp appears:
  Phase 1: lcp[i][j]  reads  lcp[i + 1][j + 1]   → row i only needs row i+1
  Phase 2: dp[i]      reads  lcp[i][i + k]       → dp[i] only needs row i
  Both phases loop i from n − 1 down to 0. So if you merge them into one loop, you build row i, use it for dp[i] right away, and never need rows i+2, i+3, and so on.

  Version B: merge the loops, keep 2 rows (the optimized version)

  What maps to what:

  ┌──────────────────────────┬───────────────────────────────────────┬────────────────────────────────────────────┐
  │        Version A         │               Version B               │                    Why                     │
  ├──────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────────┤
  │ lcp[i][j]                │ lcp[j]                                │ The current row, for this i                │
  ├──────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────────┤
  │ lcp[i + 1][j + 1]        │ next_lcp[j + 1]                       │ The previous row, for i + 1                │
  ├──────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────────┤
  │ lcp[i][i + k]            │ lcp[i + k]                            │ Still the current row                      │
  ├──────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────────┤
  │ two separate for i loops │ one for i loop                        │ Row i is used for dp[i] immediately        │
  ├──────────────────────────┼───────────────────────────────────────┼────────────────────────────────────────────┤
  │ (nothing)                │ next_lcp = lcp at the end of the loop │ Row i becomes the "previous row" for i − 1 │
  └──────────────────────────┴───────────────────────────────────────┴────────────────────────────────────────────┘
"""

class Solution:
      def deleteString(self, s: str) -> int:
          n = len(s)
          dp = [0] * (n + 1)
          next_lcp = [0] * (n + 1)                   # = lcp[i + 1]; for i = n−1 that's row n → all 0

          for i in range(n - 1, -1, -1):
              lcp = [0] * (n + 1)                    # = lcp[i]
              for j in range(n - 1, i, -1):
                  if s[i] == s[j]:
                      lcp[j] = next_lcp[j + 1] + 1   # was lcp[i][j] = lcp[i+1][j+1] + 1

              ans = 1
              for k in range(1, (n - i) // 2 + 1):
                  if lcp[i + k] >= k:                # was lcp[i][i + k]
                      ans = max(ans, 1 + dp[i + k])
              dp[i] = ans

              next_lcp = lcp                         # row i becomes "row i+1" for the next iteration
          return dp[0]



        
