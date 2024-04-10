# Consider example : 17,13,11,2,3,5,7
# Lets sort this because we want the result in sorted order
# After sorting: 2,3,5,7,11,13,17

# these are our indexes : 0 , 1, 2 ,3 ,4 , 5 , 6

# we know if we take the first one and skip the next, then the indexes at even places will be processed first. So we can definitely place: 2 ->0, 3 -> 2, 5 ->4, 7 -> 6.
# But here comes the problem like where to place the remaining ones because now it will be like a circular queue and we don't know directly like which one will be processed.
# So now lets take a queue of indexes and put the rules on it and the index that is going to be processed, we place our next sorted integer into that place
# sorted_deck = 2,3,5,7,11,13,17
# Queue: 0,1,2,3,4,5,6

# index 0 is getting processed , put 2 at 0 , queue : 2,3,4,5,6,1
# index 2 is getting processed, put 3 at 2, queue: 4,5,6,1,3
# index 4 is getting processed, put 5 at 4, queue: 6,1,3,5
# index 6 is getting processed, put 7 at index 6, queue: 3,5,1
# index 3 is getting processed, put 11 at index 3, queue: 1,5
# index 1 is getting processed, put 13 at index 1, queue: 5
# index 5 is getting process, put 17 at index 5

# Hence the order : [2,13,3,11,5,17,7]

# Go through code


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()   # we have put smaller element first
        q = deque([i for i in range(len(deck))])  # will tell next for which index we have find an element.
                    # we will start putting the smalelr ele at first so index sequence will be from '0' to 'n-1' at start.
        # Now put the next element in sequence from 'deck' at next index that will get processed.
        ans = [0] * len(deck)
        i = 0  # will tell which element to place next
        while q:
            ind1 = q.popleft()
            # Place next element at this index
            ans[ind1] = deck[i]
            if q:
                ind2 = q.popleft()
                q.append(ind2)
            i += 1
        return ans