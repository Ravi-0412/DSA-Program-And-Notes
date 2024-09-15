# Method 1: Recursion + Memoisation
"""
At each step you need to consider two cases:
i)  Add book to the current shelf
ii) Add book to the next shelf  && minimum of both will be answer.
"""
"""
For memoisation, we are only keeping track of two variable (i, remaining_width) not 'shelf_height) and still it's working why?
Because shelf_height we have passed to keep track of annsw
"""
# Time : O(n*w), w: shelfWidth 
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        self.cache = {}

        def solve(i, shelf_height, remaining_width):
            if remaining_width < 0 :
                return float('inf')
            if i == n :
                return shelf_height
            if (i, remaining_width) in self.cache:
                return self.cache[(i, remaining_width)]
            book_width , book_height = books[i]
            add_to_current_shelf = solve(i + 1, max(book_height, shelf_height), remaining_width - book_width)   # shelf_width will be max(book_height, shelf_height)
            add_to_next_shelf = shelf_height + solve(i + 1, book_height, shelfWidth - book_width)       # starting to put in new shelf
            self.cache[(i, remaining_width)] = min(add_to_current_shelf, add_to_next_shelf)
            return min(add_to_current_shelf, add_to_next_shelf)    # minimum of both will be ans

        return solve(0, 0, shelfWidth)

# Method 2: Taking only single paramter in function
# Logic:
"""
Start putting book assuming a new shelf only. And find the ans for current shelf and this answer to next_shelf.
Keep a varible to take minimum of these.
"""

# Time: Same as above i.e O(n*w), w: shelfWidth 

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        self.cache = {}

        def solve(i):
            if i == n:
                return 0
            if i in self.cache:
                return self.cache[i]
            cur_width = shelfWidth   # start a new shelf from 'i'
            max_height = 0
            res = float('inf')
            for j in range(i, n):
                width, height = books[j]
                if cur_width < width:
                    break
                cur_width -= width
                max_height = max(max_height, height)  # Putting at current_shelf only
                res = min(res, max_height + solve(j + 1))  # Add this max_height to next_shelf
            self.cache[i] = res
            return res

        return solve(0)

# Using Tabulation DP
# Logic:
"""
dp[i]: the min height for placing first books i - 1 on shelves.
For dp[i+1],
either place book i on a new shelve => dp[i] + height[i],
or grab previous books together with book i and move to next level together, 
utlitzing the sub problem dp[j] => min(dp[j] + max(height[j+1] .. height[i])), where sum(width[j+1] + ... + sum(width[i]) <= shelve_width.
"""

# java
"""
class Solution {
    public int minHeightShelves(int[][] books, int shelf_width) {
        int[] dp = new int[books.length + 1];
        
        dp[0] = 0;
        
        for (int i = 1; i <= books.length; ++i) {
            int width = books[i-1][0];
            int height = books[i-1][1];
            dp[i] = dp[i-1] + height;
            for (int j = i - 1; j > 0 && width + books[j-1][0] <= shelf_width; --j) {
                height = Math.max(height, books[j-1][1]);
                width += books[j-1][0];
                dp[i] = Math.min(dp[i], dp[j-1] + height);
            }
        }
        return dp[books.length];
    }
}
"""

# Other way of Tabulation with same approach
class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: no books require 0 height
        
        for i in range(1, n + 1):
            total_width = 0
            max_height = 0
            for j in range(i, 0, -1):
                total_width += books[j-1][0]
                if total_width > shelfWidth:
                    break
                max_height = max(max_height, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + max_height) 
        
        return dp[n]
  
