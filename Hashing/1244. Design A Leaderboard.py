# Method 1:
"""
If we take constraint in consideration , we may think that if 'top' wil be cllaed 10000 times then, we will get TLE.
10^3 * 10^4 * log(10^4) = 1.4 * 10^8
But it's not like that :
in reality, LeetCode's test cases mix addScore, reset, and top(K). 
You will never have 1,000 consecutive top(10000) calls on a fully populated list. 
"""
import heapq

class Leaderboard:

    def __init__(self):
        # Maps playerId -> score
        self.scores = {}

    # Time : O(1)
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score

  # Time : O(K * logK)
    def top(self, K: int) -> int:
        # Use a min-heap to keep track of the top K scores
        heap = []
        for score in self.scores.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        
        return sum(heap)

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            del self.scores[playerId]

# Java
"""
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Leaderboard {
    // Declaring the map at the class level so all methods can see it
    private Map<Integer, Integer> scores;

    public Leaderboard() {
        // Initializing the map inside the constructor
        scores = new HashMap<>();
    }
    
    public void addScore(int playerId, int score) {
        // If player exists, add to their score. Otherwise, insert new player.
        scores.put(playerId, scores.getOrDefault(playerId, 0) + score);
    }
    
    public int top(int K) {
        // A standard PriorityQueue in Java acts as a Min-Heap by default
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        // Iterate through all the scores currently in our map
        for (int score : scores.values()) {
            minHeap.add(score);
            // If the heap grows larger than K, discard the smallest score
            if (minHeap.size() > K) {
                minHeap.poll(); 
            }
        }
        
        // Sum up the K largest scores remaining in the heap
        // int sum = 0;
        // while (!minHeap.isEmpty()) {
        //     sum += minHeap.poll();
        // }
        // return sum;
        return minHeap.stream().mapToInt(Integer::intValue).sum();
    }
    
    public void reset(int playerId) {
        // Removes the player completely from the map, resetting them
        scores.remove(playerId);
    }
}
"""

# Method 2:
# Using Sorted Set

from sortedcontainers import SortedList

class Leaderboard:

    def __init__(self):
        # Hash map to map unique player IDs to their current scores.
        # This gives us O(1) lookups to instantly find a player's previous score.
        self.player_scores = {}
        
        # A balanced structure that maintains all active scores in sorted order.
        # Elements are automatically sorted in ascending order upon insertion.
        self.sorted_scores = SortedList()

  # Time : log(N)
    def addScore(self, playerId: int, score: int) -> None:
        # Check if the player already exists on the leaderboard
        if playerId in self.player_scores:
            old_score = self.player_scores[playerId]
            new_score = old_score + score
            
            # Step 1: Remove the outdated score from our sorted tracking
            self.sorted_scores.remove(old_score)
            # Step 2: Insert the newly updated score (automatically re-sorts)
            self.sorted_scores.add(new_score)
            # Step 3: Update our primary lookup map
            self.player_scores[playerId] = new_score
        else:
            # If it's a new player, record the initial score in both tracking structures
            self.player_scores[playerId] = score
            self.sorted_scores.add(score)

  # Time : log(N)
    def top(self, K: int) -> int:
        # Because self.sorted_scores is sorted in ascending order,
        # the largest scores are sitting at the end of the list.
        # self.sorted_scores[-K:] slices out the last K elements in O(K) time.
        return sum(self.sorted_scores[-K:])

  # Time : log(N)
    def reset(self, playerId: int) -> None:
        # Fetch the score of the player to be removed
        old_score = self.player_scores[playerId]
        
        # Erase the score from our sorted list tracking
        self.sorted_scores.remove(old_score)
        
        # Completely delete the player from the primary map
        del self.player_scores[playerId]

# Java : TreeSet
"""
import java.util.*;

class Leaderboard {
    // Standard HashMap for quick O(1) lookup mapping: playerId -> score
    private Map<Integer, Integer> playerScores;
    
    // Balanced Red-Black tree mapping: Score -> Number of players holding that score.
    // Collections.reverseOrder() forces the tree keys to sort in descending order (highest score first).
    private TreeMap<Integer, Integer> scoreCounts;

    public Leaderboard() {
        playerScores = new HashMap<>();
        scoreCounts = new TreeMap<>(Collections.reverseOrder());
    }
    
    public void addScore(int playerId, int score) {
        // If the player is already on the board, we must migrate their score ranking
        if (playerScores.containsKey(playerId)) {
            int oldScore = playerScores.get(playerId);
            
            // Decrement the count of players who hold this old score
            if (scoreCounts.get(oldScore) == 1) {
                scoreCounts.remove(oldScore); // Erase key if no players have this score anymore
            } else {
                scoreCounts.put(oldScore, scoreCounts.get(oldScore) - 1);
            }
            // Accumulate new points onto the existing score
            score += oldScore;
        }
        
        // Record/Update the player's new total score in the primary registry
        playerScores.put(playerId, score);
        
        // Register the updated score inside the TreeMap, incrementing its frequency count
        scoreCounts.put(score, scoreCounts.getOrDefault(score, 0) + 1);
    }
    
    public int top(int K) {
        int sum = 0;
        
        // Iterate through the tree entries. Because of reverseOrder(),
        // we start directly with the highest available scores.
        for (Map.Entry<Integer, Integer> entry : scoreCounts.entrySet()) {
            int score = entry.getKey();
            int count = entry.getValue();
            
            // If the total number of players sharing this score is less than or equal to our remaining K requirement:
            if (K >= count) {
                sum += score * count; // Add all of them to our sum
                K -= count;          // Reduce K by the number of players processed
            } else {
                // If the group is larger than our remaining K requirement, only take the remaining K players
                sum += score * K;
                break; // Our top K quota is entirely fulfilled
            }
            
            if (K == 0) break;
        }
        return sum;
    }
    
    public void reset(int playerId) {
        int oldScore = playerScores.get(playerId);
        
        // Clean up the player's current score out of the TreeMap tracking
        if (scoreCounts.get(oldScore) == 1) {
            scoreCounts.remove(oldScore);
        } else {
            scoreCounts.put(oldScore, scoreCounts.get(oldScore) - 1);
        }
        
        // Wipe the player profile completely out of the database
        playerScores.remove(playerId);
    }
}
"""
