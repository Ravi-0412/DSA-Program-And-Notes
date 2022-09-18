# just exactly same as "Allocate minimum no of pages"
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end, res, n= max(nums), sum(nums), -1, len(nums)
        while start<= end:
            mid= start + (end-start)//2
            if self.IsValid(nums,n,m,mid):
                res= mid
                end= mid -1
            else:
                start= mid + 1
        return res
    
    def IsValid(self, A, N, M, max_page):
        student, sum= 1, 0
        for i in range(N):
            sum+= A[i]
            if sum > max_page:  # in this case we will increase the no of student
                                # and start allocating the books to the new student
                student+= 1
                sum= A[i]
        # and at last we we will compare the no of students with M(# student given in the Q)
        # if < M means allocation is possible otherwise not possible
        return False if student > M else True