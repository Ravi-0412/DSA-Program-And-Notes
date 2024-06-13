# Time: O(n *log(sum(arr)- max(arr)))
# the best thing about this q is binary search is applicable even array is unsorted

# you can reduce this problem into: Divide the given array into 'm' subarrays such that 
# 1)'max sum of the splitted subarrays should be minimum' OR 2) 'sum of absolute diff of any two divided subarrays should be minimum'.

# how binary search?: just like we did in '378. k smallest element'. 
# we can find mid and check it is valid to allocate this much max no of pages acc to the mid if valid then we will find the next smaller
# else we will search for pages greater than mid.


# logic: # since every student should allocated at least one book so we can start checking
# between max(A) and sum(A) for min greatest , no need from  0 to sum(A).
# start= max(A) , since we have to give atleast one book to each stident.
# end= sum(A), there is only one student.

# mid is denoting the max no of pages a student can be allocated.
# if it is valid to allocate pages for the given mid(max_page) then 
# we will search for another minimum in left side of mid
# and will store that mid as temporary ans in the 'res'.   
# else we will search for greater minimum on right side of the mid
# at last we will return the res

# note: Actually we are checking 'after allocating maximum of no pages as 'mid' to a student , Are we able to divide among all students?'.
# If yes then we will decrease the 'mid' and if no then we will increase the mid.
# in this we are minmising the maximum pages allocated to a student.

# 2nd template only.

class Solution:
    def findPages(self,A, N, M):
        if M > N: return -1
        start, end= max(A), sum(A)
        while start< end:
            mid= start + (end-start)//2
            if self.IsValid(A,N,M,mid):  # search for even more smaller but mid can be the ans also.
                end= mid
            else:
                start= mid + 1
        return start

    # this will tell whether allocation is possible for the decided max_page(mid) or not.
    # we will start with one student and start allocating books to them as much as possible 
    # and will count the no of pages in sum for that particular student.
    def IsValid(self, A, N, M, max_page):
        student, sum= 1, 0
        # try allocating the books
        for i in range(N):
            sum+= A[i]
            if sum > max_page: # now we can't allocate further pages to the current selected student. 
            # in this case we will increase the no of student and start allocating the books to the new student.

            # here you can update the ans to find the allocated the pages allocated to different student. we do this later 
                student+= 1
                sum= A[i]
        # and at last we we will compare the no of students with M(# student given in the Q)
        # if < M means allocation is possible otherwise not possible
        return False if student > M else True

# vvi Note: This type of logic is applied in Q asking minimise the max i.e min(max of all possible ans or distribution etc.) OR
# maximise the minimum i.e max(min of all possible ans) given some number 'k' or 'm' or both.
# And when we have to make distribution/parts for consecutive ele (applied in non-consecutive also sometime).

# for end value(in General): jisme hmko divide karna h usko minimse kar do and jisko hmko divide karna h usko maximise kar do.(Q ke anusar)
# just logically socho ki mera value kahan se kahan tak lie kar sakta h(corner case leke) according to the Q.

# Related questions:
# Note: Minimise the maximum or find minimum 

# 1) 410. Split Array Largest Sum
# 2) 1011. Capacity To Ship Packages Within D Days
# 3) 1870. Minimum Speed to Arrive on Time
# 4) 1231.Divide-Chocolate
# 5) 875. Koko Eating Bananas
# 6) 1482. Minimum Number of Days to Make m Bouquets
# 7) 774-minimize-max-distance-to-gas-station
# 8) The Painter's Partition Problem-II
# 9) 1760. Minimum Limit of Balls in a Bag




# tried to find the pages allocated also but not getting correct ans. will do it later.
class Solution:
    def findPages(self,A, N, M):
        if M>N: return -1
        start, end= max(A), sum(A)
        pages_allocated= []
        while start< end:
            mid= start + (end-start)//2
            pages_allocated= []
            # print(pages_allocated,"pages")
            if self.IsValid(A,N,M,mid, pages_allocated):  # search for even more smaller but mid can be the ans also.
                end= mid
            else:
                start= mid + 1
        print(pages_allocated)
        return start

    # this will tell whether allocation is possible for the decided max_page(mid) or not
    # we will start with one student and start allocating books to them and will count the no of pages in sum for that particular student.
    def IsValid(self, A, N, M, max_page, pages_allocated):
        student, sum= 1, 0
        # try allocating the books to student
        for i in range(N):
            sum+= A[i]
            if sum > max_page: 
                pages_allocated.append(sum- A[i])
            # in this case we will increase the no of student and start allocating the books to the new student.
            # it means the 'sum- A[i]' no of pages is allocated to the current selected student.
                student+= 1
                sum= A[i]
        # and at last we we will compare the no of students with M(# student given in the Q)
        # if < M means allocation is possible otherwise not possible
        return False if len(pages_allocated) >= M else True
