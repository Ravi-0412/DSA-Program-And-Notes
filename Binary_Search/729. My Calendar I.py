# Method 1: 

# Logic : Kisi ek din 2 event nhi ho sakta i.e Already booked day pe koi or event nhi ho sakta.
# we only need to book the cur event if it is not overlapping with any of the booked event.

# # to check two event overlapping or not in single line 
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

# Method 1:

# To visualise overlapping, draw on paper.
# Time: O(n^2)
class MyCalendar:
    
    def __init__(self):
        self.booked = [] 

    def book(self, start: int, end: int) -> bool:
        # check if it is overlapping with any of the booked events
        for s, e in self.booked:
            # check if they are overlapping
            if end > s and e > start:  
                return False
        # booked one ko dal do list me
        self.booked.append((start, end))
        return True



# Method 2: 
# optimising method 1
# Logic: If somehow we can store events in sorted order acc to 'start'
# then we can find the possible position after which we can keep the booking of cur event.
# Cur one must have at least start date > start date of 'position-1'.

# After getting the position we can check whether we can keep the cur event at that position or not.

# This we can get in O(logn) if we maintain in sorted order.
# for this we can use 'sortedList'.

# time: O(n*logn)
    
from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.booked = SortedList()    # all booking will get stored in sorted order acc to start date   

    def book(self, start: int, end: int) -> bool:
        index_to_insert = self.booked.bisect_right((start, end))
        # is index pe tabhi insert kar sakte h jb
        # 1) pichla wala iske start hone se phle end kar jaye i.e ending time of pre <= start
        if index_to_insert > 0 and self.booked[index_to_insert -1][1] > start:
            return False
        # 2) Next wala iske bad me start ho i.e start time of next >= end
        if index_to_insert < len(self.booked) and self.booked[index_to_insert][0] < end:
            return False
        # we will only add those event for which booking will be allowed otherwise we will neglect that.
        self.booked.add((start, end))
        return True


# Method 3: Binary search Tree
# Easy and logical one . same logic as above method
# Logic: Same as we insert in BST.
# if we can insert the cur event in BST, then it means we can book the cur event else not.

# Every node will denote one event.
class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None
    
    # Agar hm kahin isko insert kar paye BST me to then possible else not.
    def isBookingPossible(self, start , end , cur):
        # 1 ) ye event ya to cur event ke bad start hona chahiye ya
        if start >= cur.e:
            # then it will go to right side
            if cur.right:
                # Then it will depend on the event 'cur.right'.
                return self.isBookingPossible(start , end , cur.right)
            # else means there is no event after this so we can insert i.e booking possible
            # so just insert and return True
            cur.right = Node(start, end)
            return True
        
        # 2) cur event ke start hone se phle end ho jaye
        elif end <= cur.s:
            # then it will go to left side
            if cur.left:
                # Then it will depend on the event 'cur.left'.
                return self.isBookingPossible(start , end , cur.left)
            # else means there is no event after this so we can insert i.e booking possible
            # so just insert and return True
            cur.left = Node(start, end)
            return True
        # else means insertion is not possible so return False
        return False

    def book(self, start: int, end: int) -> bool:
        if not self.root :
            self.root = Node(start, end)
            return True
        return self.isBookingPossible(start , end , self.root)

