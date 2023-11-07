# Just two sum logic.

# Just keep on traversing coordinates say (x1, y2)
# And when you see any already visited coordiantes say (x2, y2) that can pair with cur coordinate to get the sum == k
# incr ans by frequenccy of (x2, y2) i.e ans += seen[(x2, y2)].

# But how to get the possible coordinate pair?
# Here we have two variable and one equation unlike two sum(one variable one equation).

# So how we need to find the relation between x2 and y2.

# steps to find the relation:
# 1) Suppose that x = 'x1 XOR x2' and y = 'y1 XOR y2' then we can get x2 = 'x XOR x1' and 'y2 = y XOR y1'.
# 2) We are supposed to have 'k = x + y' so we can get x2 = 'x XOR x1' and 'y2 = (k - x) XOR y1'.

# 3) We can iterate over all possible values of 'x' and count the number of points (x1, x2) and (x2, y2).

# But what can be the possible value of 'x'?
# 'x' must between '0' to 'k'.
# e.g: if x == 0 then 'y' should be = k
# if x == 1 then 'y' should be = k -1 i.e sum = k   and so on

# time = O(n *k)

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        seen = collections.defaultdict(int)
        ans = 0
        for i in range(n):
            x1, y1 = coordinates[i]
            for x in range(k+1):
                x2 = x ^ x1
                y2 = (k - x) ^ y1
                if (x2 , y2) in seen:
                    ans += seen[(x2, y2)]   # if present then add the freq 
            seen[(x1, y1)] += 1
        return ans

