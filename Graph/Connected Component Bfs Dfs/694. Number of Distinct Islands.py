# Method 1: 

"""
just similar as '200.No of Island'.
We need to keep track of what all cells we covered, when starting from a cell and to check if that is 
structurally same as other one or not .
For checking this we will make the starting cell as (0, 0) and will add value according to direction in which we will move, into a list.
And after each call add this list into set after converting into tuple for avoiding duplicate.

e.g:  if starting index of island is (2,3) then for this we can take pos= (0, 0) and in direction we move from this starting index, 
we will keep adding them into positin say we moved left i.e [-1, 0] then, we will add this value to the pos like (pos -1, pos +0). 
after that we can add this list value into a set by converting them into tuple.
set can't store list.
"""

from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        islands = set()  # we have to return the distinct
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # left, right, up, down
        visited = set()
        
        def dfs(r, c, pos):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and grid[nr][nc] == 1:
                    temp_direction = (pos[0] + dr, pos[1] + dc)  # adding the direction in which we are moving.
                    included_cell.append(temp_direction)
                    dfs(nr, nc, temp_direction)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    included_cell = [(0, 0)]
                    dfs(r, c, (0, 0))
                    islands.add(tuple(included_cell))
        
        return len(islands)


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

