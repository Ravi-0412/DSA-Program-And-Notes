# just exactly same as "Allocate minimum no of pages". 
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end, n= max(nums), sum(nums), len(nums)
        while start< end:
            mid= start + (end-start)//2
            if self.IsValid(nums,n,m,mid):
                end= mid
            else:
                start= mid + 1
        return start
    
    def IsValid(self, a, n, m, max_sum):
        k, sum= 1, 0
        for i in range(n):
            sum+= a[i]
            if sum > max_sum:  # in this case we will increase the no of student
                                # and start allocating the books to the new student
                k+= 1
                sum= a[i]
        # and at last we we will compare the no of students with M(# student given in the Q)
        # if < M means allocation is possible otherwise not possible
        return False if k > m else True
