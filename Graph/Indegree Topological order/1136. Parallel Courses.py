"""
Note: In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

E.g: in 1st sem you can study all those courses which is not dependent on any course i.e doesn't require any prerequisite.
in other way courses having indegree == 0
in 2nd sem , we can study all those courses whose prerequisite courses has been already studied i.e courses having indegree == 1
and so on.

Note: for better visulation draw diagram.

Ans: the minimum number of semesters needed to study all courses is determined by the longest acyclic path, i.e, 
we are looking for the longest acyclic path with each edge’s weight being 1.

Observation: prerequisite thing(means topological sort) + longest/shortest path with equal weight (bfs)

Note : In other words wew can say it is forming levels and we have to find last level i.e level at which last course exist.

for level wise , we can use multisource bfs.
Can use simple bfs also, in this case take one more vaiable length in queue and one more variable to update the ans.

Only converted the code of topogical sort into multisource bfs.
"""

from collections import defaultdict
import collections

def parallelCourses(n, prerequisites):
        AdjList= defaultdict(list)
        for first,second in prerequisites:
            AdjList[first -1].append(second -1)  # converting to zero based indexing
        
        indegree= [0]*n
        
        # finding the indegree of each vertices
        for i in range(n):
            for k in AdjList[i]:  # if k is adj to 'i' means there is one indegree edge to 'k'
                indegree[k]+= 1
        
        # now applying the BFS to get the topological order
        count , ans= 0 , [] # count :no of nodes taken and ans will store the order
        Q  = collections.deque()
        for i in range(n):
            if indegree[i]==0: 
                Q.append(i)

        semester = 0
        while Q:
            for i in range(len(Q)): 
                u= Q.popleft()
                count += 1 
                ans.append(u)
                # after poping decrease the indegree of all node adjacent to 'u'
                for j in AdjList[u]:
                    indegree[j] -= 1   
                    if indegree[j]== 0:   # the preRequisite of this courses is studied in pre sem so we can study this course in next sem.
                        Q.append(j)
                    
            semester += 1

        if count!= n: 
            return -1
        return semester

# Java
"""
import java.util.*;

public class Solution {
    public int parallelCourses(int n, int[][] prerequisites) {
        Map<Integer, List<Integer>> AdjList = new HashMap<>();
        for (int[] pre : prerequisites) {
            int first = pre[0], second = pre[1];
            AdjList.computeIfAbsent(first - 1, k -> new ArrayList<>()).add(second - 1);  // converting to zero based indexing
        }

        int[] indegree = new int[n];

        // finding the indegree of each vertices
        for (int i = 0; i < n; i++) {
            if (AdjList.containsKey(i)) {
                for (int k : AdjList.get(i)) {  // if k is adj to 'i' means there is one indegree edge to 'k'
                    indegree[k] += 1;
                }
            }
        }

        // now applying the BFS to get the topological order
        int count = 0;
        List<Integer> ans = new ArrayList<>(); // count :no of nodes taken and ans will store the order
        Queue<Integer> Q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                Q.offer(i);
            }
        }

        int semester = 0;
        while (!Q.isEmpty()) {
            int size = Q.size();
            for (int i = 0; i < size; i++) {
                int u = Q.poll();
                count += 1;
                ans.add(u);
                // after poping decrease the indegree of all node adjacent to 'u'
                if (AdjList.containsKey(u)) {
                    for (int j : AdjList.get(u)) {
                        indegree[j] -= 1;
                        if (indegree[j] == 0) {  // the preRequisite of this courses is studied in pre sem so we can study this course in next sem.
                            Q.offer(j);
                        }
                    }
                }
            }
            semester += 1;
        }

        if (count != n) {
            return -1;
        }
        return semester;
    }
}

"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

int parallelCourses(int n, vector<vector<int>>& prerequisites) {
    unordered_map<int, vector<int>> AdjList;
    for (auto& pre : prerequisites) {
        int first = pre[0], second = pre[1];
        AdjList[first - 1].push_back(second - 1);  // converting to zero based indexing
    }

    vector<int> indegree(n, 0);

    // finding the indegree of each vertices
    for (int i = 0; i < n; i++) {
        for (int k : AdjList[i]) {  // if k is adj to 'i' means there is one indegree edge to 'k'
            indegree[k] += 1;
        }
    }

    // now applying the BFS to get the topological order
    int count = 0;
    vector<int> ans; // count :no of nodes taken and ans will store the order
    queue<int> Q;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) {
            Q.push(i);
        }
    }

    int semester = 0;
    while (!Q.empty()) {
        int sz = Q.size();
        for (int i = 0; i < sz; i++) {
            int u = Q.front(); Q.pop();
            count += 1;
            ans.push_back(u);
            // after poping decrease the indegree of all node adjacent to 'u'
            for (int j : AdjList[u]) {
                indegree[j] -= 1;
                if (indegree[j] == 0) {  // the preRequisite of this courses is studied in pre sem so we can study this course in next sem.
                    Q.push(j);
                }
            }
        }
        semester += 1;
    }

    if (count != n) {
        return -1;
    }
    return semester;
}

"""

