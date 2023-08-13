
# https://leetcode.com/problems/parallel-courses-ii/solutions/1373540/detailed-explanations-diagrams-annotated-code/

#Logic: 
# The selection of what you choose to be the first two (since k = 2) has a drastic impact on how you select the rest - and thus the answer. Think of it like the butterfly effect.
# There is no way to tell who is what, and which particular combination is any good. We may not know anything till the very end.

# Note : even if a node is marked 1, it does not mean its in_degree[node] is 0. It only means it needs to be taken - either in the present or in the future.
# Moreover, labelling a node either 0 or 1 allows us to represent the status of the problem in a neat format. What we have done here is called bit masking. 
# mask = 10110 represents the nodes 1, 2, 4 are yet to be considered (aka the course is yet to be taken), and the rest have already been taken.


# Recursion:
# We know that decisions taken now can produce different results later on. This makes the recursive approach favourable. For each particular iteration,
# we consider all the possible combinations of the currently available nodes - in_degree[node] == 0 and mask & 1 << node. The second part is checking if the nodeth bit is set in mask.

# Time: O(n^2*2^n), because we iterate all bitmasks and then we iterate over all pairs of non-zero bit, and we heve O(n^2) of them. Memory is O(2^n * n).

from itertools import combinations # for picking k of n
class Solution:
    @lru_cache(None) # caching for faster lookups
    def recurse(self, mask, in_degrees):
        # if all the bits are 0, we have taken all the courses
        if not mask: return 0
        
        # all the nodes that *can* be taken now, following both the properties
        # we can take those who bit is set.
        nodes = [i for i in range(self.n) if mask & 1 << i and in_degrees[i] == 0]
        
        ans = float('inf')
        # enumerating all the possible combinations
        for k_nodes in combinations(nodes, min(self.k, len(nodes))):
            # 1st Convert the 'indegree' to list and modify the indegree according to the chosen one.
            new_mask, new_in_degrees = mask, list(in_degrees)
            
            # updating what would happen to new_mask and new_in_degrees 
            # if we considered the nodes in k_nodes
            for node in k_nodes:
                # since we know the bit is set, we un-set this bit, to mark it "considered"
                new_mask ^= 1 << node
                # updating each of the in-degrees, since the "parents" have been taken away
                for child in self.graph[node]:
                    new_in_degrees[child] -= 1
            
            # note the +1! . Before passing 'in-degree' into function call convert into tuple to avoid getting modified automatically.
            ans = min(ans, 1 + self.recurse(new_mask, tuple(new_in_degrees))) 
        return ans
    
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # saving n and k for later use
        self.n = n
        self.k = k
        in_degrees = [0]*self.n
        self.graph = defaultdict(list)
        # Make graph and calculate indegree
        for prev_course, next_course in relations:
            # remember, its 0-indexed now!
            in_degrees[next_course - 1] += 1
            self.graph[prev_course - 1].append(next_course - 1)
        
        # start with all the bits set
        return self.recurse((1 << self.n) - 1, tuple(in_degrees))
        
        # Note: converting 'in-degree' into tuple because :
        # 1) we won't be able to cache the list but we can cache the tuple
        # 2) we can't modify tuple and that's what we want i.e we want to modify indegree acc to the course we take.
        # so we take list then it will get modified automatically



# Note: itertools.combinations()
# https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/
# Given an array of size n, generate and print all possible combinations of r elements in array
# arr[] = [1, 2, 3, 4],  r = 2
Output : [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# Note vvi: It returns r length subsequences of elements from the input iterable. 
# Combinations are emitted in lexicographic sort order. So, if the input iterable is sorted, 
# the combination tuples will be produced in sorted order.
