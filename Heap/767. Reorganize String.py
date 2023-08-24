# nOte: "Alternate placing the most common letters. " Use this hint to know
# If there is some character c with freq(c)>(n+1)/2 then it is impossible

# Logic:  store pair of {frequency,char} in a Heap. Then while Heap.size()>1 , 
# at every iteration, take out the top two elements, append them to the ans string, 
# decrease their frequency by 1 and push them again in the Heap.

# When the loop will break, either the Heap became empty or of 1 size.

# If it's empty, return the ans string.
# if it has size == 1, check the remaining frequency of the top/last element, if its 1, append it and return ans.
# Otherwise, return ""


# Time: O(n*logn), space: O(n)

import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        frequency = collections.defaultdict(int)
        max
        for i, c in enumerate(s):
            frequency[c] += 1
        
        maxHeap = []
        for key, value in frequency.items():
            maxHeap.append((-1* value, key))  
            # while inserting converting freq into negative to get the char with max freq first

        heapq.heapify(maxHeap)   # to get char with max freq on top
        while len(maxHeap) > 1:
            f1, c1 = heapq.heappop(maxHeap)
            f2, c2 = heapq.heappop(maxHeap)
            ans += c1 + c2
            f1 , f2 = -1*f1 - 1,  -1*f2 - 1   # converting into +ve
            if f1 > 0 :
                heapq.heappush(maxHeap, (-1*f1, c1))  
            if f2 > 0 :
                heapq.heappush(maxHeap, (-1*f2 , c2))
        if len(maxHeap) == 0:
            return ans
        f, c = heapq.heappop(maxHeap)
        if -1*f == 1:
            return ans + c
        return ""


# Later try in O(n).