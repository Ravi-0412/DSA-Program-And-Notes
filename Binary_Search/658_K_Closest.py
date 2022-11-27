# method 1: use the unsorted approach i.e min heap

# since array is sorted, all the closest element will lie i)either left
# ii) either right iii) or some left and some right of given ele
# since ele may not be in the list so we take the diff to handle this case

# in this we are finding the window of 'k' closest ele starting from 'l'
# mid will always point to the leftmost side of window  and 
# and after updating 'l' and 'r' we will get the window bw 'l:l+k'

# no need to find the absolute diff while finding the diff between target ele as array is sorted
# time: O(log(n-k) + k)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if x<= arr[0]:  return arr[0:k]
        # if x>= arr[-1]: return arr[-k:]
        l= 0
        r= len(arr)- k
        while l<r:
            mid= (l+r)//2
            if x- arr[mid]> arr[mid+k]- x: # then move the window one position right of mid as one right ele also has to be included
                l= mid +1
            else:   # note: not to 'mid-1'
                r= mid
        return arr[l:l+k]

# have to understand this properly after asking someone the 'else' condition 
# https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)
# https://leetcode.com/problems/find-k-closest-elements/discuss/462664/Python-binary-search-with-detailed-explanation