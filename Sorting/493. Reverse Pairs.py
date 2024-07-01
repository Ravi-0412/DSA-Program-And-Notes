# Similar to 'inversion count in an array".

# Note: Here logic of reverse pair and merge is different.
# So we need to write code of reverse pair 1st then write code for merging array inside merge function.


# Two way to count the reverse pair:
# Method 1) Just same as 'Inversion_count'
# vvi: Here for each element on right find the no of reverse pair.
# so keep right_side same and move on left i.e 
#  Find the 1st element from left which is > 2 * cur_element_on_right.
# After that all remaining ele on left will be > 2 * cur_element_on_right.

# Method 2) Here for each element on left find the no of reverse pair.
# so keep left_side same and move on right i.e 
#  Find the 1st element from right which is <= 2 * cur_element_on_left.
# After that all element on right that we passed will be count as ans for currrent_ele on left.

# if cur_ele on left is > that much no of element on right then remaining no on left will be obvious > these elements on right.

# See the code


# Note vvi: In these type of question , if you will first merge and then find the ans 
# i.e 'inversion count' or 'no of smaller ele' etc based on Q.
# Then you will get wrong ans. Because we will get ans while merging only.

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n= len(nums)
        return self.count_reverse_pair(nums, 0, n-1)

    def count_reverse_pair(self, arr,low,up):
        inv_count= 0
        if(low < up):   # to check if there is more than one element.
            mid= low+ (up-low)//2
            inv_count+= self.count_reverse_pair(arr, low, mid)
            inv_count+= self.count_reverse_pair(arr, mid+1, up)
            inv_count+= self.merge(arr, low, mid, up)
        return inv_count

    def reverse_pair_count1(self, arr, low, mid, up):
        low1,up1,low2,up2= low,mid,mid+1,up
        count = 0
        while(low1<= up1 and low2<= up2):
            while low1 <= up1 and arr[low1] <= 2 * arr[low2]:
                low1 += 1
            count += up1 - low1 + 1
            low2 += 1
        return count
    
    # def reverse_pair_count2(self, arr, low, mid, up):
    #     # Note: no need to start with j = 0 everytime because 
    #     # agar prev ele of left agar bda h then aane wala element in left automatically bda hoga.

    #     count, j= 0, mid + 1  # 'j' point to the 1st ele on right
    #     # we have to count pair for each ele on left side
    #     for i in range(low, mid +1):
    #         while j <= up and arr[i] > 2* arr[j]:
    #             j+= 1
    #         # just subtract the 1st index of right side.
    #         count += j- (mid + 1)
    #     return count

    def merge(self, arr,low,mid,up):  
        
        # first count the reverse pair
        count = self.reverse_pair_count1(arr, low, mid, up)
            
        # now merge the array
        low1,up1,low2,up2= low,mid,mid+1,up
        b= []
        while(low1<= up1 and low2<= up2):
            if(arr[low1] <= arr[low2]):
                b.append(arr[low1])
                low1+=1
            else: 
                b.append(arr[low2])
                low2+=1
        while(low1<=up1):
            b.append(arr[low1])
            low1+=1
        while(low2<=up2):
            b.append(arr[low2])
            low2+=1
        j= low
        k= 0
        while(j<=up):
            arr[j]= b[k]
            j+= 1
            k+= 1
        return count



