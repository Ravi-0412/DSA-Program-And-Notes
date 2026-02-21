# Basic

"""
At any time you see, find the shortest steps/path you should immediately think Breadth-First-Search or dijkastra.
logic: beginword will be at level '0' and now just keep all the words which can be formed by changing one char at level 1 ,
word which can be formed by changing two char at level 2 and so on.
for this type of Q we always use multisource BFS.
"""

# Method 1: 
# Simplest solution
# Logic: word which will differ by single character all those words will come adjacent to each other.
# So 1st make adjacency list by checking the difference and then apply mutisource bfs.

# from two constraints: 
# 1) endWord.length == beginWord.length
# 2) wordList[i].length == beginWord.length
# it is clear that beginWord and all words in wordList are of same length.

# First time when we will see the 'endWOrd' that will be the ans only.

# Time: O(n^2 * m). n= len(wordList) , m = len(each word) => more than 10**8 so TLE

# python
class Solution(object):
    def ladderLength(self, beginWord, endWord, words):
        if endWord not in words:
            return 0
        words.append(beginWord)
        n = len(words)
        adj = collections.defaultdict(list)   # [word: adjacent_words]
        for i in range(n):   # O(N)
            word1 = words[i]
            for j in range(i + 1, n): # O(N)
                word2 = words[j]
                k = 0
                cnt = 0
                while k < len(word1):    # O(M)
                    if word1[k] != word2[k]:
                        cnt += 1
                    k += 1
                if cnt == 1:
                    adj[word1].append(word2)
                    adj[word2].append(word1)
        q= deque()
        q.append((1, beginWord))
        visited = set()
        visited.add(beginWord)
        while q:
            for i in range(len(q)):
                step, word = q.popleft()
                for nei in adj[word]:
                    if nei ==  endWord:
                        return step + 1
                    if nei not in visited:
                        q.append((step + 1, nei))
                        visited.add(nei)
        return 0
    
# Java Code 
"""
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> words) {
        if (!words.contains(endWord)) return 0;
        words.add(beginWord);
        int n = words.size();

        Map<String, List<String>> adj = new HashMap<>();  // [word: adjacent_words]
        for (String word : words) adj.put(word, new ArrayList<>());

        for (int i = 0; i < n; i++) {
            String word1 = words.get(i);
            for (int j = i + 1; j < n; j++) {
                String word2 = words.get(j);
                int k = 0, cnt = 0;
                while (k < word1.length()) {
                    if (word1.charAt(k) != word2.charAt(k)) cnt++;
                    k++;
                }
                if (cnt == 1) {
                    adj.get(word1).add(word2);
                    adj.get(word2).add(word1);
                }
            }
        }

        Queue<Pair<Integer, String>> q = new LinkedList<>();
        q.offer(new Pair<>(1, beginWord));
        Set<String> visited = new HashSet<>();
        visited.add(beginWord);

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                Pair<Integer, String> p = q.poll();
                int step = p.getKey();
                String word = p.getValue();
                for (String nei : adj.get(word)) {
                    if (nei.equals(endWord)) return step + 1;
                    if (!visited.contains(nei)) {
                        q.offer(new Pair<>(step + 1, nei));
                        visited.add(nei);
                    }
                }
            }
        }

        return 0;
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& words) {
        if (find(words.begin(), words.end(), endWord) == words.end()) return 0;
        words.push_back(beginWord);
        int n = words.size();

        unordered_map<string, vector<string>> adj;  // [word: adjacent_words]

        for (int i = 0; i < n; ++i) {
            string word1 = words[i];
            for (int j = i + 1; j < n; ++j) {
                string word2 = words[j];
                int k = 0, cnt = 0;
                while (k < word1.size()) {
                    if (word1[k] != word2[k]) cnt++;
                    k++;
                }
                if (cnt == 1) {
                    adj[word1].push_back(word2);
                    adj[word2].push_back(word1);
                }
            }
        }

        queue<pair<int, string>> q;
        q.push({1, beginWord});
        unordered_set<string> visited;
        visited.insert(beginWord);

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                auto [step, word] = q.front(); q.pop();
                for (const string& nei : adj[word]) {
                    if (nei == endWord) return step + 1;
                    if (!visited.count(nei)) {
                        q.push({step + 1, nei});
                        visited.insert(nei);
                    }
                }
            }
        }

        return 0;
    }
};
"""
# Method 2: 
"""
optimising the above solution:
Logic: Instead of checking character difference between each pair of word
check what all possible words we can get which is in 'wordList' by changing an character of a word.

Time Complexity :- BigO(M^2 * N), where M is size of dequeued word & N is size of our word list
Space Complexity :- BigO(M * N) where M is no. of character that we had in our string & N is the size of our wordList.

Can do using normal bfs also taking extra variable by here multisource bfs is making more sense.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:   # corner case
            return 0
        dic = collections.defaultdict(list)
        # append the 'beginword' into the 'wordlist'
        wordList.append(beginWord)
        # now store the word w.r.t to the pattern they can make by changing one one charater into the dictionary
        for word in wordList:    # O(N)
            for i in range(len(beginWord)):    # O(M)
                # if we change the char at 'i'th index in 'word' then what all words it can form.
                # so skip the character at 'ith' index from 'word' with any special character.
                pattern= word[:i] + "*" + word[i+1:]    # O(M)
                dic[pattern].append(word)  # all words from which we can find this pattern will be at one distance only.
                
        # now do bfs from beginWord and store all the words that can be formed by changing one character in the 'beginWord'
        # all those words will be at level 1 from the "beginWord" and so on do for level word till 'Q' becomes empty
        visited= set()  # have to use this since one word can be added many times in the 'Q' 
        Q= collections.deque()
        Q.append((beginWord)) 
        visited.add(beginWord)
        level = 1
        while Q:
            for i in range(len(Q)): 
                word= Q.popleft()
                # now find the pattern that the curr 'word' can make and append those words that can make that pattern
                for i in range(len(word)):
                    pattern= word[:i] + "*" + word[i+1:]
                    # add all the nei(adjacent) to this word, for this find out the word which is present in the dic w.r.t to all the pattern that this word can generate
                    # that all will have one character diff from 'cur' word i.e one level ahead
                    for nei in dic[pattern]:
                        if nei not in visited:
                            if nei == endWord:
                                return level + 1
                            Q.append((nei))
                            visited.add(nei)
            level += 1
                            
        return 0   # return default if there is no any sequence is present
    
# Java Code 
"""
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord))  // corner case
            return 0;

        Map<String, List<String>> dic = new HashMap<>();
        wordList.add(beginWord);  // append the 'beginWord' into the 'wordList'

        // now store the word w.r.t to the pattern they can make by changing one character into the dictionary
        for (String word : wordList) {
            for (int i = 0; i < beginWord.length(); i++) {
                // if we change the char at 'i'th index in 'word' then what all words it can form.
                // so skip the character at 'i'th index from 'word' with any special character.
                String pattern = word.substring(0, i) + "*" + word.substring(i + 1);
                dic.computeIfAbsent(pattern, k -> new ArrayList<>()).add(word);  // all words that match this pattern
            }
        }

        // now do bfs from beginWord
        // all words one character apart will be at level 1 and so on
        Set<String> visited = new HashSet<>();
        Queue<String> Q = new LinkedList<>();
        Q.add(beginWord);
        visited.add(beginWord);
        int level = 1;

        while (!Q.isEmpty()) {
            int size = Q.size();
            for (int i = 0; i < size; i++) {
                String word = Q.poll();

                for (int j = 0; j < word.length(); j++) {
                    String pattern = word.substring(0, j) + "*" + word.substring(j + 1);

                    for (String nei : dic.getOrDefault(pattern, new ArrayList<>())) {
                        if (!visited.contains(nei)) {
                            if (nei.equals(endWord))
                                return level + 1;
                            Q.add(nei);
                            visited.add(nei);
                        }
                    }
                }
            }
            level++;
        }

        return 0;  // return default if no sequence is present
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (find(wordList.begin(), wordList.end(), endWord) == wordList.end())  // corner case
            return 0;

        unordered_map<string, vector<string>> dic;
        wordList.push_back(beginWord);  // append the 'beginWord' into the 'wordList'

        // now store the word w.r.t to the pattern they can make by changing one character into the dictionary
        for (const string& word : wordList) {
            for (int i = 0; i < beginWord.length(); ++i) {
                // if we change the char at 'i'th index in 'word' then what all words it can form.
                // so skip the character at 'i'th index from 'word' with any special character.
                string pattern = word.substr(0, i) + "*" + word.substr(i + 1);
                dic[pattern].push_back(word);  // all words that match this pattern
            }
        }

        // now do bfs from beginWord
        // all words one character apart will be at level 1 and so on
        unordered_set<string> visited;
        queue<string> Q;
        Q.push(beginWord);
        visited.insert(beginWord);
        int level = 1;

        while (!Q.empty()) {
            int size = Q.size();
            for (int i = 0; i < size; ++i) {
                string word = Q.front(); Q.pop();

                for (int j = 0; j < word.length(); ++j) {
                    string pattern = word.substr(0, j) + "*" + word.substr(j + 1);

                    for (const string& nei : dic[pattern]) {
                        if (!visited.count(nei)) {
                            if (nei == endWord)
                                return level + 1;
                            Q.push(nei);
                            visited.insert(nei);
                        }
                    }
                }
            }
            level++;
        }

        return 0;  // return default if no sequence is present
    }
};
"""

# method 3
"""
Better one. Do by this only
logic: Try to replace each char of each word from 'a' to 'z'.
and check if the new_word formed by replacing exist in wordlist or not.

Did using normal bfs , can do by mutisource bfs also.

Time Complexity :- BigO(M^2 * N *26), where M is size of dequeued word & N is size of our word list
Space Complexity :- BigO(M * N), visited and wordSet . because of space it's more better than method 2 even though exact time is more.

Benefits of this method: 
1) Memory EfficiencyThe Pattern Dictionary approach requires storing every possible pattern for every word. 
For a word list of 5,000 words of length 10, 
you aren't just storing 5,000 strings; you are storing 5,000* 10 = 50,000 patterns.
2) Performance in Large Datasets (N > 26)
If your wordList (N) is massive (e.g., 100,000 words), but the words are short ($M=5$), the alphabet approach is extremely fast.
Total operations approx : N *M * 26.
If N is much larger than 26, the cost of iterating a  to z is negligible compared to the cost of pre-processing and storing a massive dictionary.
3) Avoiding "Hidden" Dictionary Overhead : computing hash, hash collision etc. 

Which one should you use?
1) Use the Pattern Dictionary if the alphabet is huge (e.g., Unicode characters instead of just a to z) or if M(word length) is very small.
2) Use the Alphabet Approach if memory is a concern or if the word list N is very large.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:   # corner case
            return 0
    
        wordSet= set(wordList)   # to check in O(1) after changing each char whether that word exist or not.
        # now do bfs from beginWord and store all the words that can be formed by changing one character in the 'beginWord'
        # all those words will be at level 1 from the "beginWord" and so on do for level word till 'Q' becomes empty .
        visited= set()  # have to use this since one word can be added many times in the 'Q' 
        Q= collections.deque()
        Q.append(beginWord)   # 2nd para: storing no of steps.
        visited.add(beginWord)
        shortest_path = 1
        while Q:
            for i in range(len(Q)):    # O(N)
                word = Q.popleft()
                # now find all worss that we can get by changing single char of this word which is present in 'wordList'.
                for j in range(len(word)):    # O(M)
                    for k in range(97, 123):  # # O(26), replacing each char from 'a' to 'z' and checking if it exist in the words set
                        # word= word[: i] + chr(j) + word[i+1: ]   # my mistake(letter chenged will reflect permanently)
                        nextWord= word[: j] + chr(k) + word[j+1: ]    # O(M)
                        if nextWord in wordSet and nextWord not in visited:
                            if nextWord == endWord:
                                return shortest_path + 1
                            Q.append(nextWord)
                            visited.add(nextWord)
            shortest_path += 1                
        return 0   # return default if there is no any sequence is present
 
# Java Code 
"""
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord))  // corner case
            return 0;

        Set<String> wordSet = new HashSet<>(wordList);  // to check in O(1) after changing each char whether word exists

        // now do bfs from beginWord and store all the words that can be formed by changing one character
        // all those words will be at level 1 from the "beginWord" and so on do for level word till 'Q' becomes empty
        Set<String> visited = new HashSet<>();  // have to use this since one word can be added many times in the 'Q'
        Queue<String> Q = new LinkedList<>();
        Q.add(beginWord);  // 2nd para: storing no of steps
        visited.add(beginWord);
        int shortest_path = 1;

        while (!Q.isEmpty()) {
            int size = Q.size();
            for (int i = 0; i < size; i++) {
                String word = Q.poll();
                // now find all words that we can get by changing single char of this word present in 'wordList'
                for (int j = 0; j < word.length(); j++) {
                    for (char k = 'a'; k <= 'z'; k++) {  // replacing each char from 'a' to 'z'
                        String nextWord = word.substring(0, j) + k + word.substring(j + 1);
                        if (wordSet.contains(nextWord) && !visited.contains(nextWord)) {
                            if (nextWord.equals(endWord))
                                return shortest_path + 1;
                            Q.add(nextWord);
                            visited.add(nextWord);
                        }
                    }
                }
            }
            shortest_path++;
        }

        return 0;  // return default if no sequence is present
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (find(wordList.begin(), wordList.end(), endWord) == wordList.end())  // corner case
            return 0;

        unordered_set<string> wordSet(wordList.begin(), wordList.end());  // to check in O(1) after changing each char

        // now do bfs from beginWord and store all the words that can be formed by changing one character
        // all those words will be at level 1 from the "beginWord" and so on do for level word till 'Q' becomes empty
        unordered_set<string> visited;  // have to use this since one word can be added many times in the 'Q'
        queue<string> Q;
        Q.push(beginWord);  // 2nd para: storing no of steps
        visited.insert(beginWord);
        int shortest_path = 1;

        while (!Q.empty()) {
            int size = Q.size();
            for (int i = 0; i < size; ++i) {
                string word = Q.front(); Q.pop();
                // now find all words that we can get by changing single char of this word present in 'wordList'
                for (int j = 0; j < word.size(); ++j) {
                    for (char k = 'a'; k <= 'z'; ++k) {  // replacing each char from 'a' to 'z'
                        string nextWord = word.substr(0, j) + k + word.substr(j + 1);
                        if (wordSet.count(nextWord) && !visited.count(nextWord)) {
                            if (nextWord == endWord)
                                return shortest_path + 1;
                            Q.push(nextWord);
                            visited.insert(nextWord);
                        }
                    }
                }
            }
            ++shortest_path;
        }

        return 0;  // return default if no sequence is present
    }
};
"""

# Method 4:
"""
Logic : Bi-directional BFS

Bi-directional BFS approach is highly efficient because it reduces the search space by growing two "frontiers"
simultaneously—one from the start word and one from the end word.

When to use Bi-directional BFS?
You should reach for this approach when you see these three conditions:

1) Fixed Start and End: You know exactly where you are starting and exactly where you want to go 
(unlike a search where you are looking for "any" exit).
2) State Space is Large: If the "branching factor" (number of neighbors per word) is high, a standard BFS will explode in size. 
Bi-directional BFS keeps the "search circles" small.
3) Shortest Path: You need the minimum number of steps.

Q) When to use dictionary version and this set version(multisource bfs)? 
The version you wrote using the * patterns (like h*t) is better when you have a huge alphabet or very long words.
Your Dictionary Version: (M^2 * N) time and (M^2 * N) space.This Bi-directional Version: (M^2 * N * 26) time and (M * N) space.
The Bi-directional version is usually the "Gold Standard" for this specific problem because it 
solves the "Time Limit Exceeded" (TLE) issues that occur when the graph becomes too deep.

Real-World Use Cases : 

i) Social Network Analysis: Finding the "Six Degrees of Separation." 
If you want to find the shortest connection between two specific users on LinkedIn, 
searching from both users simultaneously is significantly faster than searching from just one.
ii) Word Games & Solvers: Dictionary-based games where you transform one word to another (like your Word Ladder).
Pathfinding in Games: When an AI character needs to move from Point A to Point B on a grid, bi-directional search can reduce the CPU load.
iii) Rubik's Cube Solvers: The state space for a Rubik's cube is massive. Most computer solvers use a variation of bi-directional search to 
find the minimum moves to solve the cube.

other probelms to solve using this method : 
1. Word Ladder (127) & Word Ladder II (126)
2. Minimum Genetic Mutation (433) (Word Ladder Lite) 
3. Open the Lock (752)
4. Jump Game IV (1346)
5. Shortest Path in a Grid with Obstacles Elimination (1293)

"""

import collections

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # 1. Initialization
        # Convert list to set for O(1) average lookup time.
        wordSet = set(wordList) 
        
        # Corner Case: If the target word isn't in the dictionary, no path exists.
        if endWord not in wordSet:
            return 0
        
        # 2. Set up Bi-directional frontiers
        # We use sets instead of deques because checking if a word exists 
        # in the 'opposite' frontier is O(1) with a set.
        beginSet = {beginWord}
        endSet = {endWord}
        level = 1 # Start counting steps from the first word
        
        # 3. Main BFS Loop
        # Continue as long as both ends have words to explore.
        # If one becomes empty, the start and end are disconnected.
        while beginSet and endSet:
            
            # BI-DIRECTIONAL OPTIMIZATION (The "Switch"):
            # Always expand the smaller set. This drastically minimizes 
            # the number of character-replacement operations we perform.
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            # This will store the words for the next level of the current frontier.
            nextSet = set()
            
            # 4. Explore the Current Frontier
            for word in beginSet:
                # For every character position in the current word...
                for i in range(len(word)):
                    # Try replacing it with every letter from a to z.
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        # Create the new word variant.
                        # Note: String slicing in Python is O(M).
                        nextWord = word[:i] + char + word[i+1:] 
                        
                        # SUCCESS: If the new word is in the OTHER frontier, 
                        # the two searches have met! Return total steps.
                        if nextWord in endSet:
                            return level + 1
                        
                        # VALID MOVE: If the word is in the dictionary (not yet visited)...
                        if nextWord in wordSet:
                            nextSet.add(nextWord)
                            # MARK AS VISITED: Removing it from wordSet prevents 
                            # the other frontier or future steps from reusing it.
                            wordSet.remove(nextWord) 
            
            # 5. Move to the next level
            beginSet = nextSet
            level += 1
            
        # If the loop finishes without meeting, no transformation sequence exists.
        return 0

