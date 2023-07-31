# Very good and logical.

# Intuition: we will attend according to the ending time first.
# for this we need minHeap to get the event having minimum ending time among already ongoing event.

# Logic: 1) To check the availability of event at any day, we need to sort the events according to the start date.
# 2) At any day we will try to attend the event that will end soonest to attend the maximum event.
# for this we need to get the least end day of events among the available events till today.
# for this we will use the minHeap to keep track of least end day of event.


# Time : O(N *log(N) + D*log(N)), d= totalDays

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  # to check which all event will start today
        totalDays = max(end for start, end in events)   # max date till which we can attend the event
        maxAttended = 0
        eventId = 0  # will tell till which event we have traversed. will help in keep track of events that will start on a day.
        day = 1   # minimum start day of any event.
        endingSooner = []    # minHeap. to get the event that will end the soonest.
        # we can attend event till last end day.
        while day  <= totalDays:
            # Add the ending date of all the events that will start today
            while eventId < len(events) and events[eventId][0] == day:
                heapq.heappush(endingSooner, events[eventId][1])
                eventId += 1
            
            # Now remove the event from heap whose ending date was less than the cur day
            # since we can't attend these events now.
            while endingSooner and endingSooner[0] < day:
                heapq.heappop(endingSooner)
            
            # Now attend one of the event that is going to end soon 
            if endingSooner:
                heapq.heappop(endingSooner)
                maxAttended += 1
            
            day += 1
        return maxAttended
    

# Q: Why only sorting won't work?
# Because we can't decide the cur event we have to attend or not using the start and end date of pre one.