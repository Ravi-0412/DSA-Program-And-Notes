# logic: Given a diff can be find 'p' pairs such that absolute diff between those pair  <= diff.
# if yes find even more smaller 'diff' and if no increase the diff.

# time: O(n(log(A))), A= max(nums)- min(nums)

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        def isPossible(diff):  # At least 'p' pair available h kya with absolute diff between pair <= 'diff'?
            count= 0
            i= 1  # start checking between index '1' and index '0'.
            while i < n:
                if nums[i]- nums[i-1] <= diff:  # sirf adjacent ke saath hi mil sakta h kyonki aage or bda diff hota jayega. && hmko same pair index ko exclude bhi karna h..
                    count+= 1
                    i+= 1  # is pair ka koi bhi index kisi or pair me nhi hona chahiye. isliye next time 'i+2' se check karenge.
                i+= 1
            return count>= p     
        
        nums.sort()  # for chekcing the diff easily 
        n= len(nums)
        start, end= 0, nums[-1] - nums[0]
        while start < end:
            mid= start + (end- start)//2
            if isPossible(mid):  # or chota diff khojo khojo.
                end= mid
            else:
                start= mid +1
        return start