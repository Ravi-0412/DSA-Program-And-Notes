# time: O(n*logn)

# Just same as '45. Jump Game 2'.

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        n = len(clips)
        clips.sort()
        i = 0     # will tell on which clip we are currently
        cnt = 0   # no of clips we have taken
        end = 0   # max we have reached taking 'cnt' no of clips.
        farthestWeCanReach = 0  # will tell farthest we can reach in next step taking all the clips having start_time <= end.
        while end < time:
            cnt += 1  # taken one more clip
            # check which all clips we can take after reaching end
            # we can take all those clips which will have start_time <= end.
            while i < n and clips[i][0] <= end:
                # if reachable then update 'fathestWeCanReach' with end time of cur clip.
                farthestWeCanReach = max(farthestWeCanReach, clips[i][1])   
                i += 1
            # check we have moved forward or not taking all the possible clips
            if end == farthestWeCanReach:
                # then it means not possible to cover all events
                return -1
            # else update end
            end = farthestWeCanReach
        return cnt