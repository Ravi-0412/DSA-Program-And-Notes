class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(i, n, combination):
            if i >= 10:
                return
            if n == 0:
                if len(combination) == k:
                    ans.append(combination)
                return 
            dfs(i + 1, n, combination)
            if n >= i:
                dfs(i + 1, n - i , combination + [i])
        
        dfs(1, n, [])
        return ans
