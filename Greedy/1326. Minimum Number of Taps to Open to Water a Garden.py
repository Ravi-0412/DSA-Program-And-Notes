# Logic: If we store range of all taps then this Q is exactly same as "1024. Video Stitching".

# Time: O(n*logn)

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        tapRange = []
        for i, num in enumerate(ranges):
            l, r = i - num , i + num
            tapRange.append([l, r])
        # print(tapRange)
        tapRange.sort()

        i = 0     # will tell on which water taps we are currently
        cnt = 0   # no of taps we have taken
        end = 0   # max we have watered taking 'cnt' no of taps.
        maxWeCanWater = 0  # will tell max area we can water taking all the taps having tapRange[i][0] <= end.
        while end < n:
            cnt += 1  # taken one more tap
            # check which all taps we can take after reaching end
            # we can take all those taps which will have tapRange[i][0] <= end
            # here 'i' can go till 'n' 
            while i < n + 1 and tapRange[i][0] <= end:
                # if reachable then update 'maxWeCanWater' with tapRange[i][1].
                maxWeCanWater = max(maxWeCanWater, tapRange[i][1]) 
                i += 1
            # check we have moved forward or not taking all the possible taps
            if end == maxWeCanWater:
                # then it means not possible to water all garden.
                print(i, maxWeCanWater)
                return -1
            # else update end
            end = maxWeCanWater
        return cnt