# Iterate from minimum to maximum distance and see if we can form square of this much 'side'.
# we can only form square of side 'x' if:
# 1) all the points at this distance 'x' has different tag
# 2) if any of the tag at this distance is not used before i.e for smaller height.

# for this: 
# 1) first store all the tags associated with a given distnace(max_distance) in a map.
# 2) Now iterate the above map in increasing order of distance(keys) and check if we 
# we can make square of this much side(distance).

# Time: O(n*logn + n).
# After sorting traversing will take O(n) only because you will checking every point 
# once only.

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        point_map = defaultdict(list)
        ans = 0
        
        for i in range(len(points)):
            max_distance = max(abs(points[i][0]), abs(points[i][1]))
            point_map[max_distance].append(s[i])
        
        seen_characters = set()
        max_side_possible = 0
        for distance in sorted(point_map.keys()):
            current_set = set()
            
            for char in point_map[distance]:
                if char in current_set or char in seen_characters:
                    #we can't make square of larger side so return 
                    return ans
                current_set.add(char)
            
            # now add all points in answer
            for char in point_map[distance]:
                ans += 1
                seen_characters.add(char)
            
            max_side_possible = distance
        
        return ans


# java
"""
import java.util.*;

class Solution {
    public int maxPointsInsideSquare(int[][] points, String s) {
        // Initialize a map to store distances and corresponding characters
        Map<Integer, List<Character>> pointMap = new TreeMap<>();
        int ans = 0;

        // Populate the map with maximum distances and their corresponding characters
        for (int i = 0; i < points.length; i++) {
            int maxDistance = Math.max(Math.abs(points[i][0]), Math.abs(points[i][1]));
            pointMap.putIfAbsent(maxDistance, new ArrayList<>());
            pointMap.get(maxDistance).add(s.charAt(i));
        }

        Set<Character> seenCharacters = new HashSet<>();

        // Iterate over the sorted keys (distances)
        for (Map.Entry<Integer, List<Character>> entry : pointMap.entrySet()) {
            Set<Character> currentSet = new HashSet<>();

            // Check for duplicate characters in the current set and seen characters
            for (char ch : entry.getValue()) {
                if (currentSet.contains(ch) || seenCharacters.contains(ch)) {
                    return ans;
                }
                currentSet.add(ch);
            }

            // Add valid characters to the seen set and update the answer
            for (char ch : entry.getValue()) {
                ans++;
                seenCharacters.add(ch);
            }
        }

        return ans;
    }
}
"""