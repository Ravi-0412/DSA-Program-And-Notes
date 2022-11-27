# do stone ko smash karne ke bad jo aayega result usko phor se add karn ahoga 
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

