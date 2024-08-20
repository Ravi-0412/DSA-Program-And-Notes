# Time: O(n*logn)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = collections.defaultdict(int)
        for x in words:
                dict[x] += 1
        res = sorted(dict, key = lambda x: (-dict[x], x))
        return res[:k]

# method 2: Using min-heap
class FreqWord(object):
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __cmp__(self, other):
        if self.freq != other.freq:
            return cmp(self.freq, other.freq)
        else:
            return cmp(other.word, self.word)

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, FreqWord(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)

        return [heapq.heappop(heap).word for _ in xrange(k)][::-1]


# about '__cmp__' and 'cmp()' 
"""
__cmp__ Method:

__cmp__ is a special method in Python 2 that was used to define custom comparison behavior between two objects. 
This method determines how objects of a class should be compared using comparison operators like <, >, ==, etc.
How __cmp__ Works:

    Return Values:
        A negative value if self is less than other.
        0 if self is equal to other.
        A positive value if self is greater than other.

In essence, __cmp__ defines the total ordering of objects.

cmp() is a built-in function in Python 2 that performs a comparison between two values. 
It uses the logic similar to the __cmp__ method but works on two arguments directly rather than being part of an object.
(just like compareTo in java)
How cmp() Works:

    Return Values:
        A negative value if x is less than y.
        0 if x is equal to y.
        A positive value if x is greater than y.
"""

# Java: Min Heap
# Time: O(n*logk)
"""
import java.util.*;

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        // Create a HashMap to count the frequency of each word
        Map<String, Integer> wordCount = new HashMap<>();
        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        // Create a priority queue (min-heap) to keep the top k frequent words
        // equal case me alphabetically greater phle aana chahiye kyonki small wale ko hmko preserve karna h.
        PriorityQueue<String> heap = new PriorityQueue<>(
            (w1, w2) -> wordCount.get(w1).equals(wordCount.get(w2)) ? w2.compareTo(w1) : wordCount.get(w1) - wordCount.get(w2)
        );

        // Add words to the heap and maintain the size of the heap as k
        for (String word : wordCount.keySet()) {
            heap.offer(word);
            if (heap.size() > k) {
                heap.poll();
            }
        }

        // Collect the result from the heap and reverse the order to get the correct ranking
        List<String> result = new ArrayList<>();
        while (!heap.isEmpty()) {
            result.add(heap.poll());
        }
        Collections.reverse(result);
        return result;
    }
}
"""

# Note: Later try in O(n). Solution in sheet