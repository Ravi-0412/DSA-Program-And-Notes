# just same logic as "alllocate minimum no of pages".
# Difference between both Q: Here we can excatly allocate 'k' no of adjacent books to each student,
# instead of allocating any no of books if no of pages in that book is <= max_page_allowed.(i.e mid) .
# And we must allocate to at least 'k' students.

# our ans will lie in range [min(bloomDay), max(bloomDay)]. At least we will have to wait till min(bloomDay) and max can go upto max(bloomDay)

# time: O(n*log(max(bloomDay)))
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):  # not possible 
            return -1
        start, end= min(bloomDay), max(bloomDay) 
        while start < end:
            mid= start + (end- start)//2
            if self.isPossible(bloomDay, mid, m , k):
                end= mid 
            else:
                start= mid + 1
        return start 

    def isPossible(self, arr, mid, m , k):
        bouquet, count= 0, 0
        for i in range(len(arr)):
            if arr[i] > mid:
                count= 0   # we have start searching from '0' only
            else:
                count+= 1
            if count== k:  # means we have found 'k' adjacent flower so we can make one bouquet.
                bouquet+= 1
                count= 0  # to chekc for next possible bouquet.
        return True if bouquet >= m else False
    
# other methods just for more clarity. only differnce in range and while loop condition.
# when trying to return -1 at last only.
# in end i have to take 'max(bloomDay) + 1' don't know why.
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        start, end= min(bloomDay), max(bloomDay) + 1
        canMakeBouquet= False  # will tell whether we can form bouquets or not.
        while start < end:
            mid= start + (end- start)//2
            if self.isPossible(bloomDay, mid, m , k):
                canMakeBouquet= True
                end= mid 
            else:
                start= mid + 1
        return start if canMakeBouquet else -1
    
    def isPossible(self, arr, mid, m , k):
        bouquet, count= 0, 0
        for i in range(len(arr)):
            if arr[i] > mid:
                count= 0   # we have start searching from '0' only
            else:
                count+= 1
            if count== k:  # means we have found 'k' adjacent flower so we can make one bouquet.
                bouquet+= 1
                count= 0  # to chekc for next possible bouquet.
        return True if bouquet >= m else False


# method 2: 
# when i took end= max(bloomDay)  then i had to run while loop for "=" condition also.
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        start, end= min(bloomDay), 
        canMakeBouquet= False
        while start <= end:
            mid= start + (end- start)//2
            if self.isPossible(bloomDay, mid, m , k):
                canMakeBouquet= True
                end= mid - 1
            else:
                start= mid + 1
        return start if canMakeBouquet else -1
    
    def isPossible(self, arr, mid, m , k):
        bouquet, count= 0, 0
        for i in range(len(arr)):
            if arr[i] > mid:
                count= 0   # we have start searching from '0' only
            else:
                count+= 1
            if count== k:  # means we have found 'k' adjacent flower so we can make one bouquet.
                bouquet+= 1
                count= 0  # to chekc for next possible bouquet.
        return True if bouquet >= m else False
