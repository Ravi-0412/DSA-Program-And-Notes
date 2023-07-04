# simplest way: using sortedList

# Time:
# add(name, score): O(logN), where N is total number of times to call add
# get(): O(logN)
# Space: O(N)


from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.count = 0
        self.locations= SortedList()

    def add(self, name: str, score: int) -> None:
        self.locations.add((-1*score, name))  # multiply by '-1' to get the bigger number at start then we can directly return from start itself.

    def get(self) -> str:
        self.count += 1
        n = len(self.locations)
        return self.locations[self.count - 1][1]
        

# vvi: Try by other good approaches.
# Above one is very bad for interview.
