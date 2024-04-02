# just applied the multisouce bfs like 'jump game 2 and jump game 3'.
# time: O(n)= space

# since we can take the same ele in next step so used hashmap to store indices of same element.

# note vvi: we can used normal bfs instead of multisource bfs in many problem but we will have to push (node, distance) instead of only node in 'Q'.

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        eleIndexes = collections.defaultdict(list)
        for i, num in enumerate(arr):
            eleIndexes[num].append(i)
        visited, visited_groups= set(), set()   
        # visited: just we use in normal bfs. 
        # visited_groups: to avoid chekcing the same list of indices again and again (not more than one.).
        #  Read explanation in the link for more clarity.
        q= collections.deque([0])
        visited.add(0)
        steps= 0
        while q:
            for i in range(len(q)):
                cur= q.popleft()
                if cur== len(arr) -1:
                    return steps
                if arr[cur] not in visited_groups:
                    for ind in eleIndexes[arr[cur]]:
                        if ind not in visited:
                            q.append(ind)
                            visited.add(ind)
                    visited_groups.add(arr[cur])
                if cur + 1 < len(arr) and (cur+1) not in visited:
                    q.append(cur +1)
                    visited.add(cur +1)
                if cur- 1 >=0 and (cur -1) not in visited:
                    q.append(cur -1)
                    visited.add(cur- 1)
            steps+= 1


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


# first to avoid above problem thought to use set inside dictionary instead of list but same problem.
# Because i was not avoid from checking again and again.
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # eleIndexes = collections.defaultdict(list)
        eleIndexes = collections.defaultdict(set)
        for i, num in enumerate(arr):
            eleIndexes[num].add(i)
        # print(eleIndexes)
        visited= set()
        q= collections.deque([0])
        visited.add(0)
        # eleIndexes[arr[0]].remove(0)
        steps= 0
        while q:
            for i in range(len(q)):
                cur= q.popleft()
                if cur== len(arr) -1:
                    return steps
                for ind in eleIndexes[arr[cur]]:
                    if ind not in visited:
                        q.append(ind)
                        visited.add(ind)
                        # eleIndexes[arr[ind]].remove(ind)
                if cur + 1 < len(arr) and (cur+1) not in visited:
                    q.append(cur +1)
                    visited.add(cur +1)
                    # eleIndexes[arr[cur +1]].remove(cur +1)
                if cur- 1 >=0 and (cur -1) not in visited:
                    q.append(cur -1)
                    visited.add(cur- 1)
                eleIndexes[arr[cur]].remove(cur)
            steps+= 1
    
