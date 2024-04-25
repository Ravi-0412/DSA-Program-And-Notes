# just same as "Allocate minimum pages". in this we have to find the maximum instead of 'minimum' that's it.
# here we are checking for valid position for placing cow then updating the 'lastcowPOSITION',
# as here we have to palce when we will find any position.

# submitted on GFG. But Q is more clear and meaningful on codeStudio and leetcode discussion link in sheet.
# https://leetcode.com/discuss/general-discussion/1302335/aggressive-cows-spoj-fully-explained-c

# time: O(nlogn)
# just like we find the last index of an element in sorted array.
class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()   # we will place the cow at the leftmost available stall. so to know the 
                        # distance between the position of stall at which last cow is placed , sorting will make our work easy.
        low= 1    # minimum difference we can get is '1'.
        up=  stalls[n-1] - stalls[0]   # maximum difference can be this only when one is placed at start and one at last
        while low <= up:
            mid= low+ (up- low)//2
            # check if we can place all the cows with minDistance as 'mid'
            if self.isPossible(stalls, mid, k):  # if we can place all the cows with minDistance as 'mid'
                                                # then try to increase the minDistance so incr 'low'. or bda ans khojo.
                low= mid + 1   # search for even more bigger
            else:  # if not able to place then try to decr the minDistance so decr 'up'
                up= mid - 1
        return up

    def isPossible(self, stalls, minDistance, k):  # given a distance, tell whether we can place all cow with minimum distance between any of them = 'distance'?
        cows= 1  # we start to place 1st cow at stall[0]
        lastCowPosition= stalls[0]  # we always try at leftmost available position
        for i in range(len(stalls)):
            # only place the cow if diff  between 'curr stall number and lastcowPosition' is >= minDistance.
            if stalls[i]- lastCowPosition >= minDistance:   # if difference is >= minDistance then hm yahan pe dusra cow ko rakh sakte h.
                # means we can place the the next cow at stall[i]
                cows+= 1
                lastCowPosition= stalls[i]
                # check if we have already placed all the cows
                if cows >= k:
                    return True
        return False

