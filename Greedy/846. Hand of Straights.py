

# here we are greedy about finding the 1st ele of group.
# and first ele must be minimum only and for this we will use minHeap

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n= len(hand)
        if n % groupSize!= 0:
            return False
        if groupSize== 1:
            return True
        cnt= collections.defaultdict(int)
        for num in hand:
            cnt[num]+= 1
        heapq.heapify(hand)    # since we want minimum each time for a group
        print(hand)
        for i in range(n//groupSize):
            # finding the 1st ele of group
            first_ele= heapq.heappop(hand)
            # check if this ele has already occured to it's frequency and find the ele with atleast one freq remaining.
            while cnt[first_ele]== 0:
                first_ele = heapq.heappop(hand)
            
            # now find all the elements of the group, we have got the starting ele of gr in 'start'
            # other remaining number must be consecutive to that.
            for i in range(groupSize):
                cnt[first_ele]-= 1
                if cnt[first_ele] < 0:  # means this no is not available or it has been used equal to no of times of it's frequency.
                    return False
                first_ele+= 1
        return True


# Method 2: No need of heap, we can sort and use pointer
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # Time: O(nlogn) + O(n*W)
        counter = Counter(hand) # O(n)
        hand.sort() # O(nlogn)
        i, n = 0, len(hand)
        while i < n: # O(n)
            cur = hand[i]
            for j in range(W): # O(W)
                if cur+j not in counter:
                    return False
                counter[cur+j] -= 1
                if counter[cur+j] == 0:
                    del counter[cur+j]
            # Move 'i' to the next smaller element from which we can start next group
            while i < n and hand[i] not in counter:
                i += 1
        return True
    
# Brute force will be very tough and complicated in this. so we have to find any pattern.