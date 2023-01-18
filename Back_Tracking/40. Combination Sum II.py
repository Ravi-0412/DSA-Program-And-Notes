# just find all the unique subsets and check sum of each subset
# unique subsets we did in Q no '78 Subsets' in last case


# recursive and better way to avoid duplicates.
# read logic here or in notes.       
# time: O(2^n *k), k= average length of subsequence(for printing/putting each subsequence into another data structure).
# space: O(k*x), k: average length of subset and x: no of combinations(ans) without recursive space.

# logic: All duplicates can come together in one combination but not in different different combination to avoid duplicates.
# if they will come in different combination then, we will get duplicates in the ans.\

# just same logic as '90.subset2'.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res= []
        
        def dfs(i, subset, target):   # just backtracking
            if target== 0:
                res.append(subset)
                return
                
            if i== len(candidates):
                return
            # when you include the curr index ele. but you can only include if curr index value is less than target.
            if candidates[i] <= target:
                dfs(i+1, subset + [candidates[i]], target - candidates[i])
            # when you don't include the curr index ele. But when you don't include the curr index,
            # you have to skip all the duplicates of curr ele to avoid duplicate in the ans.
            while i+1 < len(candidates) and candidates[i+1]== candidates[i]:
                i+= 1
            dfs(i+1, subset, target)

        dfs(0, [], target)  
        return res




