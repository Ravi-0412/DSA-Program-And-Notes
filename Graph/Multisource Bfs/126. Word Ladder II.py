# Method 1: 

# similar Q as word ladder.
# Differences from word ladder:
# 1) here we have to find the all the shortest path possible. so taking path also in Q.
# 2)VVI:  Here we will mark word as visited level by level i.e all nodes at same level at once.
# Not like one by one after visiting.
# Reason:if we mark visited at 1st tiem then we will not get all the answers.

# Take an example => in queue currently ["dog", "log"] is present and at 
# next level there is one word say "cog" .
# Now we will pop 1st word from 'queue' i.e 'dog' and now will visit its neighbour i.e 'cog'
# you mark 'cog' as visited . 
# Now you pop next word from 'queue' i.e 'log' and neighbour of 'log' is 'cog' but yiu have marked
# 'cog' visited in above step only. so you won't be able to add that but that will also path for one of our possible ans.

# That's why mark nodes visited level by level.

# Note vvi: In question "127.Word Ladder" they were asking only to find the shortest path so there was no need to add
# same node again and again to previous level nodes. But here we need to find all possible paths sowe have to add to all
# nodes to previous level.

# TLE: Time Limit Exceeded

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:   # corner case
            return []
        wordSet= set(wordList) 
        visited = set()  # have to use this since one word can be added many times in the 'Q' 
        Q= collections.deque()
        Q.append((beginWord, [beginWord])) 
        visited.add(beginWord)
        ans = []
        while Q:
            level_visited = set()
            for i in range(len(Q)):
                word , path = Q.popleft()
                # now find all worss that we can get by changing single char of this word which is present in 'wordList'.
                for j in range(len(word)):
                    for k in range(97, 123): 
                        nextWord= word[: j] + chr(k) + word[j+1: ]
                        if nextWord in wordSet and nextWord not in visited:
                            if nextWord == endWord:
                                ans.append(path + [nextWord])
                            Q.append((nextWord, path + [nextWord]))
                            level_visited.add(nextWord)
            visited = visited.union(level_visited) 
        return ans


# Java
"""
import java.util.*;

class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) {  // corner case
            return Collections.emptyList();
        }
        Set<String> wordSet = new HashSet<>(wordList);
        Set<String> visited = new HashSet<>();  // one word can be added many times in the Q
        Deque<Pair<String, List<String>>> Q = new ArrayDeque<>();
        Q.add(new Pair<>(beginWord, new ArrayList<>(List.of(beginWord))));
        visited.add(beginWord);

        List<List<String>> ans = new ArrayList<>();
        while (!Q.isEmpty()) {
            Set<String> levelVisited = new HashSet<>();
            int size = Q.size();
            for (int i = 0; i < size; i++) {
                Pair<String, List<String>> curr = Q.removeFirst();
                String word = curr.getKey();
                List<String> path = curr.getValue();

                // find all words by changing one char
                for (int j = 0; j < word.length(); j++) {
                    char[] arr = word.toCharArray();
                    for (char c = 'a'; c <= 'z'; c++) {
                        arr[j] = c;
                        String nextWord = new String(arr);
                        if (wordSet.contains(nextWord) && !visited.contains(nextWord)) {
                            if (nextWord.equals(endWord)) {
                                List<String> newPath = new ArrayList<>(path);
                                newPath.add(nextWord);
                                ans.add(newPath);
                            }
                            List<String> newPath = new ArrayList<>(path);
                            newPath.add(nextWord);
                            Q.add(new Pair<>(nextWord, newPath));
                            levelVisited.add(nextWord);
                        }
                    }
                }
            }
            visited.addAll(levelVisited);
        }
        return ans;
    }
}


"""


# C++
"""
#include <vector>
#include <string>
#include <unordered_set>
#include <deque>
using namespace std;

class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        // corner case
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if (!wordSet.count(endWord)) return {};

        unordered_set<string> visited; // to prevent re-addition
        deque<pair<string, vector<string>>> Q;
        Q.push_back({beginWord, {beginWord}});
        visited.insert(beginWord);

        vector<vector<string>> ans;
        while (!Q.empty()) {
            unordered_set<string> levelVisited;
            int sz = Q.size();
            for (int i = 0; i < sz; i++) {
                auto [word, path] = Q.front();
                Q.pop_front();

                // find all words by changing one char
                for (int j = 0; j < word.size(); j++) {
                    string nextWord = word;
                    for (char c = 'a'; c <= 'z'; c++) {
                        nextWord[j] = c;
                        if (wordSet.count(nextWord) && !visited.count(nextWord)) {
                            vector<string> newPath = path;
                            newPath.push_back(nextWord);
                            if (nextWord == endWord) {
                                ans.push_back(newPath);
                            }
                            Q.push_back({nextWord, newPath});
                            levelVisited.insert(nextWord);
                        }
                    }
                }
            }
            // expand visited at end of level
            visited.insert(levelVisited.begin(), levelVisited.end());
        }
        return ans;
    }
};

"""

# Method 2: 
# Think what repititive work we are doing in above one.

# repititive work: We are checking from whole wordList for each newWord.
# But we don't need to check words that we have seen till cur_level.

# So we have to removed words from wordList that we have seen at start of each level.
# For this best data structure is set for removing and adding in O(len(word)).

# So store words at each level in set and at each level remove the words that is in cur_level to avoid checking.

# But in set you can't take 'path' also because it won't maintain the order.
# For order add parents of all word in a list and then traverse back from 'endWord' to 'beginWord' to get all ans.

# Here no need to mark visited, if newWord in wordSet then it means they have not been visited till now.


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:   # corner case
            return []
        wordSet= set(wordList)
        parents = collections.defaultdict(list)
        cur_level = {beginWord}
        shortest_path = 1    # will give ans for 1st part "127.Word adder"
        while cur_level:
            # Remove all words from wordList which is inside cur_level
            # To avoid checking less no of  words later
            wordSet -= cur_level 
            next_level = set()  # to store words at next level
            for word in cur_level:
                for j in range(len(word)):
                    for k in range(97, 123): 
                        nextWord= word[: j] + chr(k) + word[j+1: ]
                        if nextWord in wordSet:
                            next_level.add(nextWord)
                            parents[nextWord].append(word)
            if endWord in next_level:
                break
            cur_level = next_level
            shortest_path += 1
        
        # Now backtrack from 'endWord' to 'beginWord' using dfs 
        ans = []

        def dfs(word, path):
            if word == beginWord:
                path.append(beginWord)
                ans.append(path[::-1])
                return
            for parent_word in parents[word]:
                dfs(parent_word, path + [word])
        dfs(endWord, [])
        return ans


# Java
"""
import java.util.*;

class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) {  // corner case
            return Collections.emptyList();
        }
        Set<String> wordSet = new HashSet<>(wordList);
        Map<String, List<String>> parents = new HashMap<>();
        Set<String> curLevel = new HashSet<>();
        curLevel.add(beginWord);
        int shortestPath = 1;  // will give ans for 1st part "127.Word ladder"

        while (!curLevel.isEmpty()) {
            wordSet.removeAll(curLevel);  // Remove all words in curLevel
            Set<String> nextLevel = new HashSet<>();

            for (String word : curLevel) {
                char[] arr = word.toCharArray();
                for (int j = 0; j < arr.length; j++) {
                    char old = arr[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        arr[j] = c;
                        String nextWord = new String(arr);
                        if (wordSet.contains(nextWord)) {
                            nextLevel.add(nextWord);
                            parents.computeIfAbsent(nextWord, k -> new ArrayList<>())
                                   .add(word);
                        }
                    }
                    arr[j] = old;
                }
            }

            if (nextLevel.contains(endWord)) {
                break;
            }
            curLevel = nextLevel;
            shortestPath++;
        }

        List<List<String>> ans = new ArrayList<>();
        dfs(endWord, beginWord, parents, new ArrayList<>(), ans);
        return ans;
    }

    // Backtracking helper (replaces nested dfs)
    private void dfs(String word, String beginWord, Map<String, List<String>> parents,
                     List<String> path, List<List<String>> ans) {
        if (word.equals(beginWord)) {
            path.add(beginWord);
            List<String> built = new ArrayList<>(path);
            Collections.reverse(built);
            ans.add(built);
            return;
        }
        if (!parents.containsKey(word)) return;
        path.add(word);
        for (String p : parents.get(word)) {
            dfs(p, beginWord, parents, path, ans);
        }
        path.remove(path.size() - 1);
    }
}


"""


# C++ 
"""
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        // corner case
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if (!wordSet.count(endWord)) return {};

        unordered_map<string, vector<string>> parents;
        unordered_set<string> curLevel = {beginWord};
        int shortestPath = 1;  // will give ans for 1st part "127.Word ladder"

        while (!curLevel.empty()) {
            for (auto& w : curLevel) wordSet.erase(w);  // Remove all in curLevel
            unordered_set<string> nextLevel;

            for (auto& word : curLevel) {
                string nextWord = word;
                for (int j = 0; j < word.size(); j++) {
                    char orig = nextWord[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        nextWord[j] = c;
                        if (wordSet.count(nextWord)) {
                            nextLevel.insert(nextWord);
                            parents[nextWord].push_back(word);
                        }
                    }
                    nextWord[j] = orig;
                }
            }
            if (nextLevel.count(endWord)) break;
            curLevel.swap(nextLevel);
            shortestPath++;
        }

        vector<vector<string>> ans;
        vector<string> path;
        dfs(endWord, beginWord, parents, path, ans);
        return ans;
    }

private:
    // Backtracking helper (instead of nested function)
    void dfs(const string& word, const string& beginWord,
             unordered_map<string, vector<string>>& parents,
             vector<string>& path, vector<vector<string>>& ans) {
        if (word == beginWord) {
            path.push_back(beginWord);
            vector<string> built(path.rbegin(), path.rend());
            ans.push_back(built);
            path.pop_back();
            return;
        }
        if (!parents.count(word)) return;
        path.push_back(word);
        for (auto& p : parents[word]) {
            dfs(p, beginWord, parents, path, ans);
        }
        path.pop_back();
    }
};

"""