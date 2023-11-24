# logic: The third ele must must be greatest among three.
# and we will get the 3rd ele on right side if we sort the array.

# so if we sort the array and for every ele on right side(after sorting max one will be on right side) say at index 'i'
# Then our Q reduces to "find no of combination of two element from index '0' to index 'i-1' such that their sum= arr[i] ".

# time: O(n^2), space= O(1)

class Solution:
    def countTriplet(self, arr, n):
	    arr.sort()
	    count= 0
	    i= n -1
	    while i > 1: 
	        target = arr[i]
	        # nowe we have to find the pair whose sum= arr[i]= target
	        start= 0
	        end= i -1
	        while start < end:
	            if arr[start]  + arr[end]== target:
	                count+= 1
	                start+= 1
	                end-= 1
	            elif arr[start]  + arr[end] > target:
	                end-= 1
	            else:
	                start+= 1
	        i-= 1
	        
	    return count


# Note: The above will give duplicate triplet also if duplicate no is also allowed.
# # for removing duplicates do exactly same as "15. 3Sum".