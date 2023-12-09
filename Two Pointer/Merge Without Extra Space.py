# time: O(n*m), n: no of ele in arr1, m: no of ele in arr2.
# giving TLE.
# Insertion sort logic

# just traverse in first array and check if curr ele in first array is greater than the first ele in 2nd array.
# if greater then swap both.
# after swapping find the proper position of 'first ele at arr2' in arr2 after swapping using insertion sort technique. 
# To bring the smallest ele of arr2 at start , in this way our 'arr2' will also become sorted automatically.
class Solution:
    def merge(self,arr1,arr2,n,m):
        # we have to traverse only till end of first array.
        # if we will traverse full in first array then automatically both array will be sorted.
        for i in range(n):
            if arr1[i]> arr2[0]:
                arr1[i], arr2[0]= arr2[0], arr1[i]
            temp= arr2[0]
            # now move the this 'temp' to proper position in arr2
            # just the insertion sort method to find the proper position. Here we are moving to right to find the proper position instead left.
            k= 1
            # move 'k' and keep swapping ele at 'k' with 'k-1' until you find any ele <= temp for proper position.
            while k < m and temp> arr2[k]:  
                arr2[k-1]= arr2[k]
                k+= 1
            arr2[k-1]= temp


# method 2: using gap method(shell Sort).
# How it works: we are treating both arrays as combination of array i.e arr1 + arr2.
# And we are checking the ele at gap , if out of order then swap both .
# initially gap = len(array)= n + m. each time we update gap = ceil((gap)/ 2). And we repeat the till gap >0.
# read striver solution from sheet.

# time: O((n + m)* log(m + n))

from math import ceil
class Solution:
    def merge(self,arr1,arr2,n,m):
        gap = ceil((n + m)/ 2)    # after this step from 'i' we have to compare the ele.
        while gap > 0:
            i = 0
            j = gap
            # there can be three choice
            while j < (n + m):
                # 1) both 'i' and 'j' pointing to arr1
                if j < n and arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                # 2) 'i' pointing to arr1 and j pointing to arr2. 'j' will point to index 'j-n' in arr2.
                elif i< n and j >= n and arr1[i] > arr2[j - n]:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]
                # 3) both 'i' and 'j' pointing to arr2. 'i' will point to 'i-n' and 'j' will pointt to 'j-n' in arr2 respectively.
                elif i>= n and j >= n and arr2[i - n] > arr2[j - n]:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]
                i+= 1
                j += 1
            if gap== 1:   # this i was missing . since we have to take ceil value and if gap== 1 then ceil will also= 1 leading to infinit loop.
                gap= 0
            else:
                gap = ceil((gap)/ 2)


