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

# Accepted solution in java:
# code explanation of priority Queue line:
    
# Meaning of =>  pq = new PriorityQueue<>((a, b) -> a.score == b.score ? a.name.compareTo(b.name) : b.score - a.score); 
# creates a priority queue (pq) with a custom comparator that compares elements based on their scores. 
# If the scores are equal, it further compares their names lexicographically. 
# The elements with higher scores or lexicographically smaller names will have higher priority in the queue.

# Meaning of: pq1 = new PriorityQueue<>((a, b) -> a.score == b.score ? b.name.compareTo(a.name) : a.score - b.score);
# If the scores are equal, it further compares their names lexicographically in reverse order. 
# The elements with higher scores or lexicographically larger names will have higher priority in the queue.

# Logic: 'pq1' : will contain 'i' ele having maximum score ('i' : No of get call made till now).
# because if it is called 2 times then 2 elements having largest score can't be ans for next until we add any new ele.
# This works exactly same as 'minHeap' of question '295. find median'.

# 'pq' will store all the remaining ele.
# top of 'pq' will get the ans. (in case of equal ele also since in this case smallest alphabetical will be on top only).
# This works exactly same as 'maxHeap' of question '295. find median'.

# Now come to Q:

# Exactly similar logic as "295. Find Median from Data Stream".
# all elements in 'pq1' must have priority >= all elements in 'pq' and
# priority of ele on top of 'pq1' is  one more than or equal to priority of ele on top of 'pq'.

# 1) Add():
# 'pq' should get one more ele and that can be possible ans.
# All elements that can be possible ans are already there in 'pq' except '1'.
# So that one element must have lowest priority than all the ele in 'pq1'.
# that's why first add in 'pq1' then pop one ele from 'pq1' and add that to 'pq'.

# 2) get()
# Always top pf 'pq' will give the ans i.e element having maximum priority among all minimum.
# Also top of 'pq' can't be ans if again 'get()' is called without adding any ele.
# So pop one ele from 'pq' and add it to 'pq1'.

# That one ele should have maximum score till 

# class Node {
# String name;
# int score;

# public Node(String name, int score) {
#     this.name = name;
#     this.score = score;
# }
# }

# class SORTracker {
#     PriorityQueue<Node> pq;
#     PriorityQueue<Node> pq1;
#     public SORTracker() {
#         pq = new PriorityQueue<>((a, b) -> a.score == b.score ? a.name.compareTo(b.name) : b.score - a.score);
#           // lexicographically smaller names will have higher priority in case of equal score.
    
#         pq1 = new PriorityQueue<>((a, b) -> a.score == b.score ? b.name.compareTo(a.name) : a.score - b.score);
#          // lexicographically larger names will have higher priority
#     }
    
#     public void add(String name, int score) {
#         pq1.add(new Node(name, score));
#         pq.add(pq1.remove());
#     }
    
#     public String get() {
#         String ans = pq.peek().name;
#         pq1.add(pq.remove());
#         return ans;
#     }
# }


# Note: Try to convert above code in python later.

# Later understand this solution also.
# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/solutions/3842245/python-two-solutions-sortedcontainers-and-minheap-maxheap-with-explanation/

