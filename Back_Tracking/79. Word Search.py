# Methdd 1: 

"""
we are allowed to go in all four directions.

logic: from every cell, we are checking can be get our desired word starting from that cell?

Note: we are not marking visited when we see any cell for 1st time because that cell can be used later for forming another
letter of the word.
so mark only visited when you are going to see all its neighbour like Diskastra Algo.

Here blindly calling dfs so we have to check for invalid cases just after base case.
Good approach. Do like this only.

time: O(m*n.4^(m*n))
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col= len(board), len(board[0])
        path = set()  # will be only empty after each function call.
             # will tell whether we have visited that cell in current cycle or not. just like we are passing this empty path in each call.
        
        def dfs(r,c,word):
            if not word:
                return True
            # if we can;t get ans by curent cell then simply return False
            if r<0 or r>=row or c<0 or c>= col or board[r][c]!= word[0] or (r,c) in path:
                return False   # return    . this will also work since everywhere we are cheking for True not False.
            # it means we have found the matching char at (r,c)
            path.add((r,c))  # added in path so that this cell char doesn't repeat in same cycle
            directions= [[r,c-1], [r, c+1], [r-1, c], [r+1, c]]
            for nr, nc in directions:
                if dfs(nr, nc, word[1: ]):
                    return True
            # now backtrack if we don't ans by adding the char at (r,c)
            # so that this cell can be used in next cycle.
            path.remove((r,c))
            return False
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,word):
                    return True
        return False

# Java Code 
"""
import java.util.*;

public class Solution {

    int row, col;
    Set<String> path = new HashSet<>();  // will be only empty after each function call.
    // will tell whether we have visited that cell in current cycle or not. just like we are passing this empty path in each call.

    public boolean exist(char[][] board, String word) {
        row = board.length;
        col = board[0].length;

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (dfs(r, c, word, board)) return true;
            }
        }
        return false;
    }

    public boolean dfs(int r, int c, String word, char[][] board) {
        if (word.isEmpty()) return true;

        // if we can't get ans by current cell then simply return False
        if (r < 0 || r >= row || c < 0 || c >= col || board[r][c] != word.charAt(0) || path.contains(r + "," + c))
            return false;

        // it means we have found the matching char at (r,c)
        path.add(r + "," + c);  // added in path so that this cell char doesn't repeat in same cycle

        int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        for (int[] dir : directions) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            if (dfs(nr, nc, word.substring(1), board)) return true;
        }

        // now backtrack if we don't get ans by adding the char at (r,c)
        // so that this cell can be used in next cycle.
        path.remove(r + "," + c);
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        char[][] board = {
            {'A','B','C','E'},
            {'S','F','C','S'},
            {'A','D','E','E'}
        };
        String word = "ABCCED";
        System.out.println(sol.exist(board, word));  // true
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
    int row, col;
    unordered_set<string> path;  // will be only empty after each function call.
    // will tell whether we have visited that cell in current cycle or not. just like we are passing this empty path in each call.

public:
    bool exist(vector<vector<char>>& board, string word) {
        row = board.size();
        col = board[0].size();

        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                if (dfs(r, c, word, board)) return true;
            }
        }
        return false;
    }

    bool dfs(int r, int c, string word, vector<vector<char>>& board) {
        if (word.empty()) return true;

        // if we can't get ans by current cell then simply return False
        if (r < 0 || r >= row || c < 0 || c >= col || board[r][c] != word[0] || path.count(to_string(r) + "," + to_string(c)))
            return false;

        // it means we have found the matching char at (r,c)
        path.insert(to_string(r) + "," + to_string(c));  // added in path so that this cell char doesn't repeat in same cycle

        vector<pair<int,int>> directions = {{0,-1}, {0,1}, {-1,0}, {1,0}};
        for (auto [dr, dc] : directions) {
            if (dfs(r + dr, c + dc, word.substr(1), board)) return true;
        }

        // now backtrack if we don't get ans by adding the char at (r,c)
        // so that this cell can be used in next cycle.
        path.erase(to_string(r) + "," + to_string(c));
        return false;
    }
};

int main() {
    Solution sol;
    vector<vector<char>> board = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    string word = "ABCCED";
    cout << boolalpha << sol.exist(board, word) << endl;  // true
}
"""

# Method 2: 
# if we don't want to use the path set for visited then do like this.
# just mark grid value by any char.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col= len(board), len(board[0])
        
        def dfs(r,c,word):
            if not word:
                return True
            if r < 0 or r >= row or c < 0 or c>= col or board[r][c] == "#" or board[r][c] != word[0]:
                return False
            temp = board[r][c]
            board[r][c]= "#"
            directions= [[r,c-1], [r, c+1], [r-1, c], [r+1, c]]
            for nr, nc in directions:
                if dfs(nr, nc, word[1: ]):
                    return True
            # now backtrack if we don't ans by adding the char at (r,c)
            board[r][c]= temp
            return False
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,word):
                    return True
        return False


# Java Code 
"""
public class Solution {

    public boolean exist(char[][] board, String word) {
        int row = board.length, col = board[0].length;

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (dfs(r, c, word, board)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean dfs(int r, int c, String word, char[][] board) {
        if (word.isEmpty()) return true;
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length
                || board[r][c] == '#' || board[r][c] != word.charAt(0)) {
            return false;
        }

        char temp = board[r][c];
        board[r][c] = '#';

        int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        for (int[] dir : directions) {
            int nr = r + dir[0], nc = c + dir[1];
            if (dfs(nr, nc, word.substring(1), board)) return true;
        }

        // now backtrack if we don't get ans by adding the char at (r,c)
        board[r][c] = temp;
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        char[][] board = {
            {'A','B','C','E'},
            {'S','F','C','S'},
            {'A','D','E','E'}
        };
        String word = "ABCCED";
        System.out.println(sol.exist(board, word)); // true
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int row = board.size(), col = board[0].size();

        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                if (dfs(r, c, word, board)) return true;
            }
        }
        return false;
    }

    bool dfs(int r, int c, string word, vector<vector<char>>& board) {
        if (word.empty()) return true;
        if (r < 0 || r >= board.size() || c < 0 || c >= board[0].size()
            || board[r][c] == '#' || board[r][c] != word[0]) {
            return false;
        }

        char temp = board[r][c];
        board[r][c] = '#';

        vector<pair<int, int>> directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        for (auto [dr, dc] : directions) {
            int nr = r + dr, nc = c + dc;
            if (dfs(nr, nc, word.substr(1), board)) return true;
        }

        // now backtrack if we don't get ans by adding the char at (r,c)
        board[r][c] = temp;
        return false;
    }
};

int main() {
    Solution sol;
    vector<vector<char>> board = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    string word = "ABCCED";
    cout << boolalpha << sol.exist(board, word) << endl;  // true
}
"""
# method 3: Another way of doing .
# just same logic only
# Here we are not calling blindly so need to check invalid cases.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col= len(board), len(board[0])
        
        def dfs(r,c,word):
            if not word:
                return True
            # if board[r][c]== "#":  # duplicate. No need of this because we are only calling dfs if that cell is not visited.
            #     return
            temp= board[r][c]
            board[r][c]= "#"  # marking visited
            directions= [[r,c-1], [r, c+1], [r-1, c], [r+1, c]]
            for nr, nc in directions:
                if 0<=nr < row and 0<= nc < col and board[nr][nc]!= "#" and board[nr][nc]== word[0]: 
                    if dfs(nr, nc, word[1: ]):
                        return True
            # now backtrack if we don't ans by adding the char at (r,c)
            board[r][c]= temp
            return False
        
        for r in range(row):
            for c in range(col):
                if board[r][c]== word[0] and dfs(r,c,word[1:]):  # checking if we can get and from current cell
                    return True
        return False


# Java Code 
"""
public class Solution {

    public boolean exist(char[][] board, String word) {
        int row = board.length, col = board[0].length;

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                // checking if we can get ans from current cell
                if (board[r][c] == word.charAt(0) && dfs(r, c, word.substring(1), board, row, col))
                    return true;
            }
        }
        return false;
    }

    public boolean dfs(int r, int c, String word, char[][] board, int row, int col) {
        if (word.isEmpty())
            return true;

        // if board[r][c]== "#" : duplicate. No need of this because we are only calling dfs if that cell is not visited.
        // return;

        char temp = board[r][c];
        board[r][c] = '#';  // marking visited

        int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        for (int[] d : directions) {
            int nr = r + d[0], nc = c + d[1];
            if (0 <= nr && nr < row && 0 <= nc && nc < col &&
                board[nr][nc] != '#' && board[nr][nc] == word.charAt(0)) {
                if (dfs(nr, nc, word.substring(1), board, row, col))
                    return true;
            }
        }

        // now backtrack if we don't get ans by adding the char at (r,c)
        board[r][c] = temp;
        return false;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int row = board.size(), col = board[0].size();

        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                // checking if we can get ans from current cell
                if (board[r][c] == word[0] && dfs(r, c, word.substr(1), board, row, col))
                    return true;
            }
        }
        return false;
    }

    bool dfs(int r, int c, string word, vector<vector<char>>& board, int row, int col) {
        if (word.empty())
            return true;

        // if board[r][c]== "#" : duplicate. No need of this because we are only calling dfs if that cell is not visited.
        // return;

        char temp = board[r][c];
        board[r][c] = '#';  // marking visited

        vector<pair<int, int>> directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        for (auto [dr, dc] : directions) {
            int nr = r + dr, nc = c + dc;
            if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
                board[nr][nc] != '#' && board[nr][nc] == word[0]) {
                if (dfs(nr, nc, word.substr(1), board, row, col))
                    return true;
            }
        }

        // now backtrack if we don't get ans by adding the char at (r,c)
        board[r][c] = temp;
        return false;
    }
};
"""