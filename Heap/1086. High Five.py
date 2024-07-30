# Logic: MinHeap + hashmap
# use priority queue for each id
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        
        for idx, val in items:
            heapq.heappush(d[idx], val)
            
            if len(d[idx]) > 5:
                heapq.heappop(d[idx])
        
        res = [[i, sum(d[i]) // len(d[i])] for i in sorted(d)]
        
        return res

# Method 2:  first sort reversely by id and score, and then calculate average for each id
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(reverse=True)
        
        res = []
        curr = []
        idx = items[0][0]
        
        for i, val in items:
            if i == idx:
                if len(curr) < 5:
                    curr.append(val)
            else:
                res.append([idx, sum(curr) // len(curr)])
                curr = [val]
                idx = i
        
        res.append([idx, sum(curr) // len(curr)])
        
        res = res[::-1]
        
        return res


# java
# Method 1:
"""
import java.util.*;

class Solution {
    public int[][] highFive(int[][] items) {
        // Using a HashMap to store a min-heap for each student ID
        Map<Integer, PriorityQueue<Integer>> map = new HashMap<>();
        
        // Iterate over each score entry
        for (int[] item : items) {
            int id = item[0];
            int score = item[1];
            
            // Get the min-heap for the student, creating it if necessary
            map.putIfAbsent(id, new PriorityQueue<>());
            PriorityQueue<Integer> minHeap = map.get(id);
            
            // Add the current score to the heap
            minHeap.offer(score);
            
            // If the heap size exceeds 5, remove the smallest score
            if (minHeap.size() > 5) {
                minHeap.poll();
            }
        }
        
        // Prepare the result list
        List<int[]> resList = new ArrayList<>();
        
        // Calculate the average of the top 5 scores for each student
        for (Map.Entry<Integer, PriorityQueue<Integer>> entry : map.entrySet()) {
            int id = entry.getKey();
            PriorityQueue<Integer> minHeap = entry.getValue();
            
            int sum = 0;
            for (int score : minHeap) {
                sum += score;
            }
            
            // Calculate the average and add it to the result
            resList.add(new int[]{id, sum / minHeap.size()});
        }
        
        // Convert the result list to a 2D array
        int[][] res = new int[resList.size()][2];
        for (int i = 0; i < resList.size(); i++) {
            res[i] = resList.get(i);
        }
        
        // Sort the result by student IDs
        Arrays.sort(res, Comparator.comparingInt(a -> a[0]));
        
        return res;
    }
}
"""