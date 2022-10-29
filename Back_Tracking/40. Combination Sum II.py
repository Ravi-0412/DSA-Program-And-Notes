# just find all the unique subsets and check sum of each subset
# unique subsets we did in Q no '78 Subsets' in last case

# giving memory limit exceeded for bigger values but correct only
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        totalSubset= self.subset(candidates)
        ans= []
        for arr in totalSubset:
            if sum(arr)== target:
                ans.append(arr)
        return ans
                
    def subset(self,arr):
        outer= [[]]
        start,end= 0,0  
        arr.sort()   # first sort the array so that all duplicates come together
        for i in range(len(arr)):
            start=0  # will start copy from index '0' only in case no duplicates 
            if(i>0 and arr[i-1]==arr[i]):  # if duplicates
                start= end+1              # will copy from previous newly added set i.e end+1
            end= len(outer) -1     # will be equal to 
            for j in range(start,len(outer)):
                internal= outer[j].copy()  
                internal.append(arr[i])       
                outer.append(internal)   
        return outer


# recursive and better way to avoid duplicates 
# read logic here or in notes    https://leetcode.com/problems/combination-sum-ii/   
# time: O(2^n *k), k= average length of subsequence(for printing/putting each subsequence into another data structure)
# space: O(k*x), k: average length of subset and x: no of combinations(ans) without recursive space
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res= []
        self.UniqueSubsequenceSum(0,candidates,target,[],res)
        return res
    
    def UniqueSubsequenceSum(self,ind,arr,target,path,res):
        if target==0:
            res.append(path)
            return
        for i in range(ind,len(arr)):
            if arr[i]>target:  # since array is sorted so if we can't add ele at curr index then how we can add ele at further index
                break
            if i>ind and arr[i]==arr[i-1]:  # simply skip to avoid duplicates
                continue                
            self.UniqueSubsequenceSum(i+1,arr,target-arr[i],path + [arr[i]],res)  # add every possible ele 


