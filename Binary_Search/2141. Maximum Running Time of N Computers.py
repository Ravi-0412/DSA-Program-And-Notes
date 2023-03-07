# intuition:
# The staright idea, is to use all baterial evenly.
# So we take advantage of all the energy wihout any left.
# In this case, we can run up to sum(A) / n minutes.
# This average value is an upper bounde of the final result.
# It's great to start with this enviromental intuition.


# logic: For each battery,
# if its running time is greater than t, it can contribute t minutes for simutaneously running.
# if its running time is less than t, it can contribute all its power for simutaneously running.

# also: If the computers cannot run simultaneously for t1 minutes, then definitely they cannot run simultaneously for t2 > t1 minutes

# Time complexity: O(len(batteries) * log (sum(batteries) / n))
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def canRunSimultaneously(time):  # will tell whether it is possible to run all computers simultaneously for t= "time".
            curSum= 0
            for t in batteries:
                # every battery will contribute for min(t, time) simultaneously.
                if t >= time:  
                    curSum += time
                else:
                    curSum += t
                # curSum+= min(t, time)   # shoretr one
            return curSum >= n * time   # n*time = Average battery time of all battery needed to run the run 'n' computer for t= time minutes continously.
    
        start= min(batteries)  # since n <= len(batteries)
        # end=   max(batteries) *max(batteries)    # will give the wrong ans
        end= sum(batteries) // n   # time time for which they can run simultaneously 
        while start <= end:
            guess= start + (end- start)//2  # mid only
            if canRunSimultaneously(guess):
                start= guess + 1
            else:
                end=   guess - 1
        return end