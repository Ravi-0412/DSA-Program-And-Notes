# Note: In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.


# Ans: the minimum number of semesters needed to study all courses is determined by the longest acyclic path, i.e, 
# we are looking for the longest acyclic path with each edge’s weight being 1.

# Observation: prerequisite thing(means topological sort) + maximum path wirth equal weight (multosource bfs)

# Logic: Just topological sort + multisource bfs
# Only converted the code of topogical sort into multisource bfs.

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


