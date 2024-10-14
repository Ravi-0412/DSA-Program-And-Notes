# Time: O(n^2)
# Space: O(n)

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = [x * k for k in range(n)]  # res[k] means the result for k times operation
        # find the cost for each ele and it should be minimum only so will take min(cur_val, val_after_rotation)
        for i in range(n):
            # calculating the minimum cost to collect a specific chocolate (at index i) after k rotations.
            cur = nums[i]
            for k in range(n):
                cur = min(cur, nums[(i + k) % n]) 
                res[k] += cur  # add 'cur' as rotation cost is already added so only need to add the cur_value.
        return min(res)   # return the cost which is minimum among all.


# method 2: Try to do in O(n*logn)
# https://leetcode.com/problems/collecting-chocolates/solutions/3624079/beat-100-o-n-log-n-python-binary-search-dp-sliding-window-minimum/
# https://leetcode.com/problems/collecting-chocolates/solutions/3624087/o-n-log-n/

# my mistake:
# for chocolate having value > x, i am adding it to collected if it reaches to any index having cost <=x.
# But we should take minimum of all such postions to find the cost of chocolate having value > x.

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        cost = 0   # will store the ans
        collected= set()  # will tell the chocolate we have collected till now
        priceLessThanX= set()  # will contain the index where price of chocolate is less than 'x'.
        # we can directly collect all chocolates having price <= x for overall minimum cost
        for i , price in enumerate(nums):
            if price <= x:
                collected.add(i)
                priceLessThanX.add(i)
                cost += price
        # Now keep on rotating till you collect all chocolates
        cur = [i for i in range(n)]
        while len(collected) < n :
            for i in range(n):
                cur[i] = (cur[i] + 1) % n
            # After each rotation pick the chocolate which has come at any index which has price < = x and which is not collected already.
            for i in range(n):
                ind= cur[i]
                # if the index (i) to which curent chocolate has come has value <=x then collect the current chocolate i.e cur[i]
                if i in priceLessThanX and ind not in collected:
                    collected.add(ind)
                    cost += min(nums[ind], nums[i] + x)  # cost of taking from that index  + rotation cost
        
        return cost
