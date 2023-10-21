# Similar to 'inversion count in an array".

# Note: Here logic of reverse pair and merge is different.
# So we need to write code of reverse pair 1st then write code for merging array inside merge function.

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
    
    # left part should be smaller and if it doesn't mean there are inversions.
    def merge(self, arr,low,mid,up):
        # first count the reverse pair
        # Note: no need to start with j = 0 everytime because 
        # agar prev ele of left agar bda h then aane wala element in left automatically bda hoga.
        # time : O(m + n)

        count, j= 0, mid + 1  # 'j' point to the 1st ele on right
        # we have to count pair for each ele on left side
        for i in range(low, mid +1):
            while j <= up and arr[i] > 2* arr[j]:
                j+= 1
            # just subtract the 1st index of right side.
            count+= j- (mid + 1)  # pichla ele wala count + cur ele ka pair.  

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

