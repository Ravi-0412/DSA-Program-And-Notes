# just before merging check for reverse pair

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
        count, j= 0, mid + 1
        # we have to count pair for each ele on left side
        for i in range(low, mid +1):
            while j <= up and arr[i] > 2* arr[j]:
                j+= 1
            # when while loop will end that will be reverse pair for that ele and next coming ele pair mat increase also.
            count+= j- (mid + 1)  # just subtract the 1st index of right side.

        # now merge the array
        low1,up1,low2,up2= low,mid,mid+1,up
        inv_count= 0
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
