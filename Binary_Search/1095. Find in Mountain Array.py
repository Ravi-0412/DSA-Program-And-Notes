# find the index of peak ele
# and apply binary search on left and right of the peak index.
# TIme : o(logn)

class Solution:
        def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
            last_index= mountain_arr.length()-1
            peak= self.peakIndexInMountainArray(mountain_arr)
            # search in left part of the peak 
            # if not found then search on right side of the peak
            left= self.BinarySearch_ascending(mountain_arr,target,0,peak)
            if left!= -1:
                return left
            else:
                right= self.BinarySearch_descending(mountain_arr,target,peak+1,last_index)
                return right

        def peakIndexInMountainArray(self,mountain_arr):
            start= 0
            end= mountain_arr.length() -1
            while(start<end):
                mid= start+ (end-start)//2
                if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                    end = mid 
                else:
                    start = mid + 1
            return start
        
        # searching in the left side of the peak including peak
        # from starting till peak ele array will be in ascending order
        def BinarySearch_ascending(self,mountain_arr,key,start,end):
            low= start
            up= end
            while(low<= up):
                mid= (low+up)//2
                if mountain_arr.get(mid)== key:
                   return mid
                elif(mountain_arr.get(mid)> key):
                    up= mid-1
                else:
                    low= mid+1
            return -1
         # searching in the right side of the peak
        # after peak ele array will be in descending order
        def BinarySearch_descending(self,mountain_arr,key,start,end):
            low= start
            up= end
            while(low<= up):
                mid= (low+up)//2
                if mountain_arr.get(mid)== key:
                   return mid
                elif(mountain_arr.get(mid)> key):
                    low= mid+ 1
                else:
                    up= mid -1
            return -1
        
# Note: why here we can't apply direct binary search in single traversal 
# like "33.search in rotated sorted array" ?
# Reason: Here we can't say if one part is unsorted then other part will be sorted.
# if sorted then we can apply binary search but here we can't say.

# method 2:
# Better and concise one

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # 1. Find the peak index
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                r = mid
            else:
                l = mid + 1
        peak = l
        
        # 2. Search in the ascending part (left of peak)
        # Result found here is guaranteed to be the minimum index.
        res = self.orderAgnosticBS(mountainArr, target, 0, peak, True)
        if res != -1: return res
        
        # 3. Search in the descending part (right of peak)
        return self.orderAgnosticBS(mountainArr, target, peak + 1, n - 1, False)

    def orderAgnosticBS(self, arr, target, low, high, isAscending):
        """Standard BS with a toggle for ascending or descending logic."""
        while low <= high:
            mid = low + (high - low) // 2
            val = arr.get(mid) # Store value to minimize API calls
            
            if val == target:
                return mid
            
            # Flip logic based on direction
            if isAscending:
                if val < target: low = mid + 1
                else: high = mid - 1
            else:
                if val > target: low = mid + 1
                else: high = mid - 1
        return -1

