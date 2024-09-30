# Note: why binary search ?: Timestamps are strictly increasing. so we can use binary search to find the closest value.
# simple only but i didn't get the Q.

class TimeMap:   
    def __init__(self):
        self.hashmap= collections.defaultdict(list)   # key: list of [value, timestamp]   (list of list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])
    
    # Just like we find the floor
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
        return self.hashmap[key][end][0] if end >=0 else  ""  

# Java
"""
import java.util.*;

class TimeMap {
    // A HashMap where the key is a String and the value is a list of pairs (value, timestamp)
    private Map<String, List<Pair>> hashmap;

    // Constructor
    public TimeMap() {
        hashmap = new HashMap<>();
    }

    // Method to store key-value with timestamp
    public void set(String key, String value, int timestamp) {
        if (!hashmap.containsKey(key)) {
            hashmap.put(key, new ArrayList<>());
        }
        hashmap.get(key).add(new Pair(value, timestamp));
    }

    // Method to get the value associated with the given key and timestamp
    public String get(String key, int timestamp) {
        if (!hashmap.containsKey(key)) {
            return "";
        }
        
        List<Pair> pairs = hashmap.get(key);
        int start = 0, end = pairs.size() - 1;
        
        // Binary search to find the correct timestamp or closest one below it
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (pairs.get(mid).timestamp == timestamp) {
                return pairs.get(mid).value;
            } else if (pairs.get(mid).timestamp > timestamp) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        
        return end >= 0 ? pairs.get(end).value : "";
    }

    // Helper class to represent a (value, timestamp) pair
    private class Pair {
        String value;
        int timestamp;

        Pair(String value, int timestamp) {
            this.value = value;
            this.timestamp = timestamp;
        }
    }
}
"""
