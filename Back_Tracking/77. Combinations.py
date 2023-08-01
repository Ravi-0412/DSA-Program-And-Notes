# Logic: start from each number and find all combination we can make of 'k' numbers.
# Note: we only taking combination in increasing order because arrangement doesn't matter in combination.

# Note: All will be unique combination only because we are taking in increasing order only.

# Note: method of '39. Combination Sum' won't work here because here we are taking care of issues.

# time : O(n, k)  => 'n' choose 'k'.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def combination(num , remainin_no, comb):
            if remainin_no == 0:
                # we got one combination
                ans.append(comb)
                return
            # we can take next number from any of greater reamining number till 'n'.
            for i in range(num + 1, n + 1):
                combination(i, remainin_no - 1, comb + [i])

        # starting from each number one by one
        # we need to go till 'n- k + 1' not 'n' because when we will start with number > 'n- k + 1', we will not get 'k' numbers.
        for num in range(1, n + 1): 
            combination(num, k-1, [num])
        return ans