# my mistake: I didn't get the Q properly

# here we are greedy about finding the 1st ele of group.
# and first ele must be minimum only and for this we will use minHeap

import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n= len(hand)
        if n % groupSize!= 0:
            return False
        if groupSize== 1:
            return True
        cnt= collections.defaultdict(int)   # if we write like this we can direct incr or decr the count without checking the key in the dictionary.
                                            # using this only we are finding the other gr ele even if that is not present.
                                            # if ele is not present then it's count will automatically assigned to zero.
        for num in hand:
            cnt[num]+= 1
        heapq.heapify(hand)    # since we want minimum each time for a group
        for i in range(n//groupSize):    # will go till no of groups
            # finding the 1st ele of group
            first_ele= heapq.heappop(hand)
            # check if this ele has already occured to it's frequency and find the ele with atleast one freq remaining.
            while cnt[first_ele]== 0:
                first_ele= heapq.heappop(hand)
            
            # now find all the elements of the group, we have got the starting ele of gr in 'start'
            # other remaining number must be consecutive to that.
            for i in range(groupSize):
                cnt[first_ele]-= 1
                if cnt[first_ele]< 0:  # means this no is not available or it has been used equal to no of times of it's frequency.
                    return False
                first_ele+= 1
        return True


# Brute force will be very tough and complicated. so we have to find nay pattern.