# simplest way: using sortedList
# we need to store the locations acc to their score in sorted order.

# Time:
# add(name, score): O(logN), where N is total number of times to call add
# get(): O(logN)
# Space: O(N)

# To know more baout 'sortedList'.
# https://grantjenks.com/docs/sortedcontainers/sortedlist.html


from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.count = 0
        self.locations= SortedList()

    def add(self, name: str, score: int) -> None:
        self.locations.add((-1*score, name))  # multiply by '-1' to get the bigger number at start then we can directly return from start itself.

    def get(self) -> str:
        self.count += 1
        return self.locations[self.count - 1][1]
        

# Note:  Above one is very bad for interview.

# Do by Two heaps