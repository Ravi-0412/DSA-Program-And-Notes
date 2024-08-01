# How to check two interval overlap with each other?
# check if any interval start time lies in other interval.

# Method 1:
# Convert into minutes and check overlapping.
# example : 14 : 34 then (1 * 10 + 4) * 60 + (3 * 10 + 4)

# method 2:
# compare directly

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # i) check if the start time of event2 falls within the time span of event1
        # ii) checks if the start time of event1 falls within the time span of event2.
        return (event1[0] <= event2[0] <= event1[1]) or (event2[0] <= event1[0] <= event2[1])


# java
"""
class Solution {
    public boolean haveConflict(String[] event1, String[] event2) {
        return (event1[0].compareTo(event2[0]) <= 0 && event2[0].compareTo(event1[1]) <= 0) || 
               (event2[0].compareTo(event1[0]) <= 0 && event1[0].compareTo(event2[1]) <= 0);
    }
"""

# Method 3: 
# to check two event overlapping or not in single line 
"""
Given 2 segment [left1, right1], [left2, right2],
how can we check whether they overlap?

If these two intervals overlap then, there should exist a value x such that:
left1 <= x <= right1 && left2 <= x <= right2
which implies 'max(left1, left2) <= x <= min(right1, right 2)'.

# since left1 <= right1 and left2 <= right2 is already given.
# so we only need to check : left1 <= right2 && left2 <= right1

These two are the sufficient and necessary conditions,
for two interval overlaps.

"""

class Solution:
    def haveConflict(self, e1: List[str], e2: List[str]) -> bool:
        return e1[0] <= e2[1] and e2[0] <= e1[1]

# java
"""
class Solution {
    public boolean haveConflict(String[] e1, String[] e2) {
        return e1[0].compareTo(e2[1]) <= 0 && e2[0].compareTo(e1[1]) <= 0;
    }
}
"""