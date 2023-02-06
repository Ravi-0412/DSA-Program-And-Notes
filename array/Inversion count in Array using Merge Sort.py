# if we find any ele in left part greater than right part while merging then all ele in left part from that index will make one inversion.
# since array is sorted and if lower index ele is greater then next coming index of left part will also greater.
# submitted on Gfg.
class Solution:  
    def inversionCount(self, arr, n):
        return self.merge_sort_count_inversion(arr, 0, n-1)
    
    def merge_sort_count_inversion(self, arr,low,up):
        inv_count= 0
        if(low < up):   # to check if there is more than one element.
            mid= low+ (up-low)//2
            inv_count+= self.merge_sort_count_inversion(arr, low, mid)
            inv_count+= self.merge_sort_count_inversion(arr, mid+1, up)
            inv_count+= self.merge(arr, low, mid, up)
        return inv_count
    
    # left part should be smaller and if it doesn't mean there are inversions.
    def merge(self, arr,low,mid,up):
        low1,up1,low2,up2= low,mid,mid+1,up
        inv_count= 0
        b= []
        while(low1<= up1 and low2<= up2):
            if(arr[low1] <= arr[low2]):
                b.append(arr[low1])
                low1+=1
            else:  # all ele from low1 to mid will be greater so count= mid- low + 1
                inv_count+= mid - low1 + 1   # being counted for each ele on left side.
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
        return inv_count
