# Mistake: I was not getting the properly.
# Also after seeing intuition , i was directly searching for given snap in get function & and if not found then i was returning '0'.

# Note: we have to search for floor value of snap at given id.

# Note: Intuition in notes, page no : 117

# Time: O(logS)
# Space: O(S) where S is the number of set called.

# set(int index, int val) is O(1) in Python 
# snap() is O(1)
# get(int index, int snap_id) is O(logSnap)

class SnapshotArray:

    def __init__(self, length: int):
        # for every index we will store the (snap_id, val) in a list
        self.indexToSnap_Values = collections.defaultdict(list)  # will store the data in form of [(snap_id, val)] at every index
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # check if there is already some stored value at this index for same snap_id.
        # check if last index snap value is same
        if self.indexToSnap_Values[index] and self.indexToSnap_Values[index][-1][0] == self.snap_id:
            self.indexToSnap_Values[index][-1][1] = val     # only change the value and return
            return
        # go to given index and store the pair
        self.indexToSnap_Values[index].append([self.snap_id, val])
        
        # self.indexToSnap_Values[index].append([self.snap_id, val])   # only writing like this will give error when same index is called for set multiple times for same snap_id value.
        
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # return the value at floor of given snap_id.
        # so search for the floor position of snap_id and return that.
        arr = self.indexToSnap_Values[index]  # getting the 2D array i.e list of values at given index.
        start, end= 0, len(arr) -1
        while start <= end:
            mid= start + (end - start)//2
            if arr[mid][0] == snap_id:
                # if found return from here
                return arr[mid][1]
            if arr[mid][0] > snap_id:
                end = mid -1
            else:
                start= mid + 1
        # 'end' will have floor value and in case no floor value exist we will return '0' the default one(as given we should initialise with '0'.)
        return arr[end][1]  if end >= 0 else 0  


# My mistake in get function
def get(self, index: int, snap_id: int) -> int:
        # go to the given index and search position of given snap_id and return the value at that snap_id
        arr = self.indexToSnap_Values[index]  # getting the array i.e list of values at given index.
        start, end= 0, len(arr) -1
        while start <= end:
            mid= start + (end - start)//2
            if arr[mid][0] == snap_id:
                return arr[mid][1]
            if arr[mid][0] > snap_id:
                end = mid -1
            else:
                start= mid + 1
        return 0  # means there is no value at given snap_id for given index.

