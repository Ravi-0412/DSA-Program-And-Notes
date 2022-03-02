# find the index of peak ele
# and apply binary search on left and right of the peak index
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
            return -1

        def peakIndexInMountainArray(self,mountain_arr):
            start= 0
            end= mountain_arr.length() -1
            while(start<end):
                mid= start+ (end-start)//2
                if mountain_arr.get(mid)< mountain_arr.get(mid+1):
                # means we are in incr part of array
                # this might be the ans, but look at left 
                # because end!= mid-1 may be 
                # so peak(maximum ele) will be on right side of mid
                    start= mid +1
                else:  #  peak(maximum ele) will be on left side of mid including mid
                    end= mid
            # after loop will fail then start= end and both will be
            # pointing to the maximum ele in the array
            # both are always trying to find max element in the array
            # which is our ans
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
