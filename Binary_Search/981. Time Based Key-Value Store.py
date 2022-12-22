# Note: why binary search ?: Timestamps are strictly increasing. so we can use binary search to find the closest value.
# simple only but i didn't get the Q.

class TimeMap:   
    def __init__(self):
        self.hashmap= collections.defaultdict(list)   # key: list of [value, timestamp]   (list of list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap: return ""
        start, end= 0, len(self.hashmap[key]) -1
        while start <= end:
            mid= start + (end-start)//2
            if self.hashmap[key][mid][1]== timestamp:
                return self.hashmap[key][mid][0]
            elif self.hashmap[key][mid][1]> timestamp:
                end=  mid-1
            else:
                start= mid +1
        return self.hashmap[key][end][0] if end>=0 else  ""