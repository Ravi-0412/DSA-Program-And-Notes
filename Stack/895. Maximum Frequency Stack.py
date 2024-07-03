# Method 1: MaxHeap
# Storing (count, index, number) in min-heap and keeping map of counts. 
# Since its a min-heap, I am negating the count and index while pushing in the heap.

# The intuition is, heap will always keep the element with max count on top, 
# and if two elements have same count, the second element (index) 
# will be considered while doing pop operation. Also, the count map, 
# is useful when the new occurence of the exisiting element is pushed.

# Taking index: to break the tie in case of same frequency

class FreqStack:
    
    def __init__(self):
        self.heap = []
        self.m = collections.defaultdict(int)
        self.counter = 0
        
    def push(self, x):
        self.m[x] +=1
        heapq.heappush(self.heap,(-self.m[x], -self.counter, x))
        self.counter+=1
    
    def pop(self):
        toBeRemoved = heapq.heappop(self.heap)
        self.m[toBeRemoved[2]] -=1
        return toBeRemoved[2]

# Method 2: Understand this later properly

# Hash map 'freq' will count the frequence of elements.
# Hash map 'm' is a map of stack.
# If element x has n frequency, we will push x, n times in m[1], m[2] .. m[n]
# maxfreq records the maximum frequence.

# push(x) will push x tom[++freq[x]]
# pop() will pop from the m[maxfreq]

def __init__(self):
    self.freq = collections.Counter()
    self.m = collections.defaultdict(list)
    self.maxf = 0
def push(self, x):
    freq, m = self.freq, self.m
    freq[x] += 1
    self.maxf = max(self.maxf, freq[x])
    m[freq[x]].append(x)

def pop(self):
    freq, m, maxf = self.freq, self.m, self.maxf
    x = m[maxf].pop()
    if not m[maxf]: self.maxf = maxf - 1
    freq[x] -= 1
    return x


# java
"""
// Method 1:
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class FreqStack {
    
    private PriorityQueue<int[]> heap;
    private Map<Integer, Integer> frequencyMap;
    private int counter;

    public FreqStack() {
        heap = new PriorityQueue<>(
            (a, b) -> a[0] == b[0] ? Integer.compare(b[1], a[1]) : Integer.compare(b[0], a[0])
        );
        frequencyMap = new HashMap<>();
        counter = 0;
    }

    public void push(int x) {
        frequencyMap.put(x, frequencyMap.getOrDefault(x, 0) + 1);
        heap.offer(new int[]{frequencyMap.get(x), counter, x});
        counter++;
    }

    public int pop() {
        int[] element = heap.poll();
        int value = element[2];
        frequencyMap.put(value, frequencyMap.get(value) - 1);
        return value;
    }
}
"""

"""
// Method 2:
class FreqStack {
    HashMap<Integer, Integer> freq = new HashMap<>();
    HashMap<Integer, Stack<Integer>> m = new HashMap<>();
    int maxfreq = 0;

    public void push(int x) {
        int f = freq.getOrDefault(x, 0) + 1;
        freq.put(x, f);
        maxfreq = Math.max(maxfreq, f);
        if (!m.containsKey(f)) m.put(f, new Stack<Integer>());
        m.get(f).add(x);
    }

    public int pop() {
        int x = m.get(maxfreq).pop();
        freq.put(x, maxfreq - 1);
        if (m.get(maxfreq).size() == 0) maxfreq--;
        return x;
    }
}
"""