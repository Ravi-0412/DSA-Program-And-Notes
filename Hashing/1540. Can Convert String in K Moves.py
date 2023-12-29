# Logic: Try to convert every char one by one
# And find the no of move required to convert them.
# If some move has been already used to convert other char then find the next move that can produce that same char
# i.e keep on adding  '+26' as this will produce the same char only.

# Time : O(n * m) , n= len(s) , m = (10**9 // 26)  => TLE

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        visited = set()
        max_move = 0
        for i in range(len(s)):
            diff = ord(t[i]) - ord(s[i])
            if diff < 0 :
                diff = diff + 26
            while diff and diff in visited:
                # if char not same then find the next move we can make for conversion
                diff += 26
            visited.add(diff) 
            max_move = max(max_move, diff)
            if max_move > k:
                return False
        return True


# Optimisation
# for finding the next move for conversion, we can keep track of no of times we can see that move.
# e.g: if we have seen move '5' , '3' times then if cur char require '5' move then next move 
# that can we use to get same char after '5' move will be : 3 * 26 + 5.
    
# Time: O(n) 
# space = O(26)

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        visited = set()
        move_count = collections.defaultdict(int)
        max_move = 0
        for i in range(len(s)):
            diff = ord(t[i]) - ord(s[i])
            if diff < 0 :
                diff = diff + 26
            if diff:
                diff = 26 * move_count[diff] + diff
            visited.add(diff) 
            max_move = max(max_move, diff)
            move_count[diff % 26] += 1   # incr count of 'smallest diff' by '1'.
            if max_move > k:
                return False
        return True
        