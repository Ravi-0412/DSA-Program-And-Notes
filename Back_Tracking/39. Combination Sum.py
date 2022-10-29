# just same as we did in "subsequnce with given some". only difference is
# here in case arr[0]<=k i.e when we are including that index don't increment that index as we can include any ele any no of times
# this we already did in "coin change problem" also

# time: O(2^t *k), t= target , k= length of every subsequence(for printing/putting each subsequence into another data structure)
# every ele will have t possibility in worst case i.e let target= 10 and 1st ele =1 
# space: O(k*x), k: average length of subset and x: no of combinations(ans) without recursive space
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        self.SubsequenceSum(candidates,target,[],res)
        return res
    
    def SubsequenceSum(self,arr,k,path,res):
        if not arr:
            if k==0:
                res.append(path)
            return
        # if we include the current ele, then add arr[ind] into the ans
        if arr[0]<=k:   # i was skipping this condition. my mistake
                        # without this condition it will go into infinite loop will never stop
            self.SubsequenceSum(arr,k-arr[0],path+ [arr[0]],res)   # don't incr the index as repitition is allowed
        # if we don't include the current ele 
        self.SubsequenceSum(arr[1:],k,path,res)

