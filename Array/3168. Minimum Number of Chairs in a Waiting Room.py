# Logic: 
"""
# we need to keep track of how many people are in the waiting room at any given time and 
# determine the peak number of people present simultaneously. This peak value will 
# represent the minimum number of chairs required since every person needs a chair when they enter.
"""
# How to do?
# maximum no of chair = max value of count
# where we increase count by '1' when any person enter 'E' and decrease by '1' 
# when any person leave 'L'.

class Solution(object):
    def minimumChairs(self, s):
        res = 0
        max_chairs = 0
        for i in s:
            if i == 'E':
                res += 1
                max_chairs = max(res, max_chairs)
            else: 
                res -= 1
        return max_chairs
        