# All the below methods are valid for sorted as well as unsorted array
# method 1: Brute force- Time:o(n^2) ,space: o(1)


#method 3: using hashmap- Time: o(n), space: o(n)
# Tgis method will work for sorted as well as unsorted arry
# submitted on GFG
# just subtract the given number from the sum and
# if that diffrence is presnt in the hashmap then it means 
# the pair exist 
# if difference is not present then store the arr[i] in hashmap as 'keys'
# to check this element with other remaining element
# if pair will exist then index of such pair will be the 
# 'values' of remaining sum and index of current element 'i'
class Solution:
    	def hasArrayTwoCandidates(self,arr, n, x):
	    hashmap= {}
	    for i in range(n):
	        remaining_sum= x- arr[i]
	        if remaining_sum in hashmap:
	            return True
	        else:
	            hashmap[arr[i]]= i  # storing the index as values for each element
	    return False


# method 2: giving correct output but showing time limit for few cases
# using double pointer one pointing to start and one to end
#logic: sort the array and find the sum of 1st element from start and
# first ele from end 
# Time: o(n) for sorted and o(nlogn) for unsorted array, space: o(1)
def hasArrayTwoCandidates(arr, n, x):
	    arr.sort()
	    j= n-1
	    k= 0
	    while(k<j):
    	   # if sum of ele is greater then we have to search in left side 
		   # of last ele so decr 'j' by one
		   # or else incr 'k' by 1
	       if arr[k]+ arr[j]== x:
	           return True 
	       elif arr[k]+ arr[j]> x:
	           j-= 1
	       else:
	           k+= 1
	    return False
arr= [1,2,3,4,5,6,7,9,8]
print(hasArrayTwoCandidates(arr,9,20))


