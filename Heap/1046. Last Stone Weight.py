# do stone ko smash karne ke bad jo aayega result usko phir se add karna hoga
# And ye step repeat karte rhna h.

# Note: Jahan bhi aisa kuch dikhe ki har ek operation me(ya bad) hmko min/max chahiye then
# think about heap.

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]= -stones[i]  # to make max heap we hav eto switch the sign of every ele
        heapq.heapify(stones)
        while len(stones)>1:
            y= -heapq.heappop(stones)
            x= -heapq.heappop(stones)
            if x!= y:
                y= y-x
            else:  # to handle the case if there only two ele at any point and both of them are equal
                y= 0
            heapq.heappush(stones,-y)
        return -stones[0]

# Another way.
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]= -stones[i]  # to make max heap we have to switch the sign of every ele.
        heapq.heapify(stones)
        while len(stones)>1:
            y= -heapq.heappop(stones)
            x= -heapq.heappop(stones)
            if x!= y:
                y= y-x
                heapq.heappush(stones,-y)
        return -1*stones[0] if stones else 0
