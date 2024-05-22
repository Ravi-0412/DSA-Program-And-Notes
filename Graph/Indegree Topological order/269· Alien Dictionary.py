# logic: whenever you have to find the sorted sequence (or order of sequence) given distinct node/val and relation between them, 
# just think of topological sorting
# from the relation you can make the directed graph seeing which one should come first and which one should come later
# and after that you can apply the method to find the sequence

# in this q, node will the char where both the word will differ
# and direction will be from word1[i] to word2[i] where word1 and word2 are adjacent word(word2 coming later in lexographic order)

# After making adjacency list this q reduces to: find the order of char .
# For this just use topological sort using bfs and dfs.

# Time complexity:
# Say the number of characters in the dictionary (including duplicates) is n. Building the graph takes O(n). 
# Topological sort takes O(V + E). V <= n. E also can't be larger than n. So the overall time complexity is O(n).

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # first find the distinct char from the given words
        # with wrt to each char, we have intilised one empty set to put its neighbour in the set
        # first it will go to one word and will check all the char in that word, after that it will move to another word repeating the same thing
        adj = {char: set() for word in words for char in word} 
        # now you have got the distinct char and now we have to find the sequence of these char

        # now make the directed graph which char is coming first
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # if word2 is prefix of word1 and word1 is coming before means invalid case, so simply return empty string
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])   # w2[j] will come after w1[j], so make a directed edge from w1[j] to w2[j]
                    break   # once you got any unequal char no need to check further the remaining char. now check the another two word
        
        # in visited, we will store each distinct char, and 'True' or 'False' as value wrt to each char
        # if a char in visited then it means we have visited that (color== gray) and 'False' and 'True' means
        # False: means we have visited that char as well as its neighbour also before only (in pre cycles)
        # True: means we have visited that char only not its neighbour i.e this char is visited in current cycle only
        visited = {}  
        res = []
        def dfs(char):
            if char in visited: 
                # return the value wrt to that char
                # True means, this char is visited in same cycle means cycle and 
                # False means simply skip as this char as well as its adjacent node is already visited
                return visited[char] 
            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):    # means cycle
                    return True

            visited[char] = False
            res.append(char)

        # cycle detection and printing code starts from here
        for char in adj:
            if dfs(char):   # if cycle 
                return ""

        res.reverse()
        return "".join(res)


# Java
"""
public class Solution {
    public String alienOrder(String[] words) {
        // Initialize the adjacency list for each character.
        Map<Character, Set<Character>> adj = new HashMap<>();
        for (String word : words) {
            for (char c : word.toCharArray()) {
                adj.putIfAbsent(c, new HashSet<>());
            }
        }

        // Build the graph.
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i];
            String w2 = words[i + 1];
            int minLen = Math.min(w1.length(), w2.length());

            // If word2 is a prefix of word1 and word1 comes before word2, it's invalid.
            if (w1.length() > w2.length() && w1.substring(0, minLen).equals(w2.substring(0, minLen))) {
                return "";
            }

            for (int j = 0; j < minLen; j++) {
                if (w1.charAt(j) != w2.charAt(j)) {
                    adj.get(w1.charAt(j)).add(w2.charAt(j));
                    break;  // No need to check further characters.
                }
            }
        }

        // Visited map to track characters during DFS.
        Map<Character, Boolean> visited = new HashMap<>();
        List<Character> res = new ArrayList<>();
        
        // DFS function to detect cycles and build the result.
        boolean[] cycleFound = new boolean[1];  // Array to act as a reference for boolean flag.

        for (char c : adj.keySet()) {
            if (dfs(c, adj, visited, res, cycleFound)) {
                return "";
            }
        }

        // Reverse the result to get the correct order.
        Collections.reverse(res);
        StringBuilder sb = new StringBuilder();
        for (char c : res) {
            sb.append(c);
        }
        return sb.toString();
    }

    private boolean dfs(char c, Map<Character, Set<Character>> adj, Map<Character, Boolean> visited, List<Character> res, boolean[] cycleFound) {
        if (visited.containsKey(c)) {
            return visited.get(c);
        }
        visited.put(c, true);
        for (char neigh : adj.get(c)) {
            if (dfs(neigh, adj, visited, res, cycleFound)) {
                return true;
            }
        }
        visited.put(c, false);
        res.add(c);
        return false;
    }
}
"""

# other way:
# Link: https://leetcode.com/problems/alien-dictionary/solutions/70119/java-ac-solution-using-bfs/
