# logic: find the 'index of first greater ele in arr2 for each number num in arr1'.
# this will give the number of ele in arr2 which is <= each number in arr1.

# for this we need to sort 'arr2' and then search the index using binary search.

# Time Complexity: O((m + n) * log n)

class Solution:
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        arr2.sort()
        ans= []
        
        def lastIndex(num):
            start, end= 0, len(arr2) -1
            while start <= end:
                mid= start + (end - start)//2
                if arr2[mid] <= num:
                    start= mid + 1
                else:
                    end= mid - 1
            return start
                    
        for num in arr1:
            ind= lastIndex(num)  # find the last index of 'num' into arr2.
            ans.append(ind)
        return ans
