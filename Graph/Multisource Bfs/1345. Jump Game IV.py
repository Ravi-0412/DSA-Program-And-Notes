# Method 1: 

"""
just applied the multisouce bfs like 'jump game 2 and jump game 3'.

since we can take the same all indexes such that arr[i] == arr[j],
So at each index 'i', we need to keep tarck of all indices 'j' we can take.
For this store indexes in hashmap : [arr[i] : indexes_where_arr[i]_is_present]

Note vvi=> e.g: [7, 7, 7,7, 7, 7, 7]
first we visit index '0' and all other indexes have same value as index '0' then we will add all indexes into the queue.
again suppose index '1' is poped then again we will add all the indexes that is not visited (i.e other than '0' & '1') .
in this way it will go like : (n-1) + (n-2) + (n-3) + ... 1 => O(n^2)

To avoid this we will mark 'value at any index' also visited to avoid checking same set of indexes again and again
Because if that 'number'(value) will come for 1st time only then all indexes where value is same will get visited 
So no need of visiting those again.

Therefore we will use two visited set :
1) visited: for marking 'index' as visited
2) visited_groups: marking number(index value) to avoid chekcing the same list of indices again and again (not more than one.).

Note vvi: We will add node in 'visited' when we will see that index for 1sst time only but
we will add 'index value' after poping.

note: we can used normal bfs instead of multisource bfs in many problem 
but we will have to push (node, distance) instead of only node in 'Q'.
time: O(n)= space
"""


# My mistake
# i was getting TLE for case : [7,7,7,7,7,7,........]
# this will go in O(n^2) because every time it will go through through the list of its indices.
# so to avoid this we used one another set in above solution 'visited_groups' to check whether we have visited all indices of an ele or not.
# first time itself we can add all the indices into list no need to check again and again.
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        eleIndexes = collections.defaultdict(list)
        for i, num in enumerate(arr):
            eleIndexes[num].append(i)
        visited= set()
        q= collections.deque([0])
        visited.add(0)
        steps= 0
        while q:
            print(q)
            for i in range(len(q)):
                cur= q.popleft()
                if cur== len(arr) -1:
                    return steps
                for ind in eleIndexes[arr[cur]]:
                    if ind not in visited:
                        q.append(ind)
                        visited.add(ind)
                if cur + 1 < len(arr) and (cur+1) not in visited:
                    q.append(cur +1)
                    visited.add(cur +1)
                if cur- 1 >=0 and (cur -1) not in visited:
                    q.append(cur -1)
                    visited.add(cur- 1)
            steps+= 1


# Correct solution

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        eleIndexes = collections.defaultdict(list)
        for i, num in enumerate(arr):
            eleIndexes[num].append(i)
        visited, visited_groups= set(), set()   
        q= collections.deque([0])
        visited.add(0)
        steps= 0
        while q:
            for i in range(len(q)):
                cur= q.popleft()
                if cur== len(arr) -1:
                    return steps
                if arr[cur] not in visited_groups:
                    # means we have not visited this set of indexes where arr[curr] is equal.
                    for ind in eleIndexes[arr[cur]]:
                        # if index is not visited
                        if ind not in visited:
                            q.append(ind)
                            visited.add(ind)
                    visited_groups.add(arr[cur])  # add value at 'curr' index
                if cur + 1 < len(arr) and (cur+1) not in visited:
                    q.append(cur +1)
                    visited.add(cur +1)
                if cur- 1 >=0 and (cur -1) not in visited:
                    q.append(cur -1)
                    visited.add(cur- 1)
            steps+= 1


# Java
"""
import java.util.*;

class Solution {
    public int minJumps(int[] arr) {
        Map<Integer, List<Integer>> eleIndexes = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            eleIndexes.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }

        Set<Integer> visited = new HashSet<>();
        Set<Integer> visited_groups = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        visited.add(0);
        int steps = 0;

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int cur = q.poll();
                if (cur == arr.length - 1) {
                    return steps;
                }

                if (!visited_groups.contains(arr[cur])) {
                    // means we have not visited this set of indexes where arr[curr] is equal.
                    for (int ind : eleIndexes.get(arr[cur])) {
                        // if index is not visited
                        if (!visited.contains(ind)) {
                            q.add(ind);
                            visited.add(ind);
                        }
                    }
                    visited_groups.add(arr[cur]); // add value at 'curr' index
                }

                if (cur + 1 < arr.length && !visited.contains(cur + 1)) {
                    q.add(cur + 1);
                    visited.add(cur + 1);
                }

                if (cur - 1 >= 0 && !visited.contains(cur - 1)) {
                    q.add(cur - 1);
                    visited.add(cur - 1);
                }
            }
            steps++;
        }

        return -1; // should never reach here
    }
}


"""


# C++
"""
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

class Solution {
public:
    int minJumps(vector<int>& arr) {
        unordered_map<int, vector<int>> eleIndexes;
        for (int i = 0; i < arr.size(); i++) {
            eleIndexes[arr[i]].push_back(i);
        }

        unordered_set<int> visited;
        unordered_set<int> visited_groups;
        queue<int> q;
        q.push(0);
        visited.insert(0);
        int steps = 0;

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int cur = q.front(); q.pop();
                if (cur == arr.size() - 1) {
                    return steps;
                }

                if (visited_groups.find(arr[cur]) == visited_groups.end()) {
                    // means we have not visited this set of indexes where arr[curr] is equal.
                    for (int ind : eleIndexes[arr[cur]]) {
                        // if index is not visited
                        if (visited.find(ind) == visited.end()) {
                            q.push(ind);
                            visited.insert(ind);
                        }
                    }
                    visited_groups.insert(arr[cur]); // add value at 'curr' index
                }

                if (cur + 1 < arr.size() && visited.find(cur + 1) == visited.end()) {
                    q.push(cur + 1);
                    visited.insert(cur + 1);
                }

                if (cur - 1 >= 0 && visited.find(cur - 1) == visited.end()) {
                    q.push(cur - 1);
                    visited.insert(cur - 1);
                }
            }
            steps++;
        }

        return -1; // should never reach here
    }
};


"""

    
