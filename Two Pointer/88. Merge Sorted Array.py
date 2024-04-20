# time-O(m+n), space= O(m)
# submitted on letcode
# just same way we merge in merge sort
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:        
        nums= nums1[:m]
        i,j,k= 0,0,0
        while(i<m and j <n):
            if nums[i]>= nums2[j]:
                nums1[k]= nums2[j]
                k+= 1
                j+= 1
            if j<n and nums2[j]>=nums[i]:   # 'j<n' because j after incr j in above step it can go out of bound
                nums1[k]= nums[i] 
                k+= 1
                i+= 1
        while(i<m):
            nums1[k]= nums[i]
            k+= 1
            i+= 1
        while(j<n):
            nums1[k]= nums2[j]
            k+= 1
            j+= 1


# method 2: in place merging(best one)
# logic: just think of utilising the extra zero.
# for in place we can replace the zeroes at last 
# as replacing these will not affect the nums1.
# but if we start putting from start in nums1 then ele of nums1 will get affected.   
# Putting from last means put the maximum ele of both the arr from last.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:  
        while m>0 and n>0:
            if nums1[m-1]>= nums2[n-1]:
                nums1[m+n-1]= nums1[m-1]
                m-= 1
            else:
                nums1[m+n-1]= nums2[n-1]
                n-= 1
            
        # after this we only need to check whether n>0, no need to check m>0 separately
        # but m may be greater than zero .
        # if n>0 means ele of nums2 is smaller but since we are doing in place in nums1 only
        # so all ele of nums1 will be automaticaly at proper position
        # so only need to put remaining ele of nums2
    
        if n>0:
            nums1[:n]= nums2[:n]


# Java code and better on than above.
# No need of slicing

""""
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m-1 , p2 = n-1 ,i = m+n-1;
        while(p2 >=0 ){
            if(p1 >=0 && nums1[p1] > nums2[p2]){
                nums1[i--] = nums1[p1--];
            } 
            else{
                nums1[i--] = nums2[p2--];
            }
        }
       }
}
"""