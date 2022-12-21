# Time: 
# the best thing about this q is binary search is applicable even array is unsorted

# you can reduce this problem into: Divide the given array into 'm' subarrays such that 
# 'max sum of the splitted subarrays will be minimum' OR  'sum of diff of subarrays will be minimum'.

# how binary search?: just like we did in '378. k smallest element'. 
# we can find mid and check it is valid to allocate pages acc to the mid if valid then we will find the next smaller
# else we will search for pages greater than mid.

# logic: # since every student should allocated at least one book so we can start checking
# between max(A) and sum(A) for min greatest , no need from  0 to sum(A)
# mid is denoting the max no of pages a student can be allocated.
# if it is valid to allocate pages for the given mid(max_page) then 
# we will search for another minimum in left side of mid
# and will store that mid as temporary ans in the 'res'.   
# else we will search for greater minimum on right side of the mid
# at last we will return the res

class Solution:
    def findPages(self,A, N, M):
        if M>N: return -1
        start, end= max(A), sum(A)
        while start< end:
            mid= start + (end-start)//2
            if self.IsValid(A,N,M,mid):  # search for even more smaller but mid can be the ans also.
                end= mid
            else:
                start= mid + 1
        return start

    # this will tell whether allocation is possible for the decided max_page(mid) or not
    # we will start with one student and start allocating books to them and will count the no of pages in sum for that particular student.
    def IsValid(self, A, N, M, max_page):
        student, sum= 1, 0
        # try allocating the books
        for i in range(N):
            sum+= A[i]
            if sum > max_page:  # in this case we will increase the no of student
                                # and start allocating the books to the new student
                student+= 1
                sum= A[i]
        # and at last we we will compare the no of students with M(# student given in the Q)
        # if < M means allocation is possible otherwise not possible
        return False if student > M else True
