
# Logic: we will try to merge(union) a cur ele with its adjacent ele if already merged(present in hashamp).
# At alst we will return the largest size of distinct component.

class DSU:
    def __init__(self, n):
        self.parent= [i for i in range(n)]
        self.size=   [1 for i in range(n)]
    
    def findParent(self, n):
        if n== self.parent[n]:
            return n
        self.parent[n]= self.findParent(self.parent[n])
        return self.parent[n]
    
    def union(self, n1, n2):
        p1, p2= self.findParent(n1), self.findParent(n2)
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2
            self.size[p2]+= self.size[p1]
        else:
            self.parent[p2]= p1
            self.size[p1]+= self.size[p2]
    
    # find the size of the largest component (distinct parent)
    def getLongestSequence(self):
        maxSize= 1 # minimum can be '1'.
        for i in range(len(self.parent)):
            if i== self.parent[i]:  # means parent of one of the component.
                maxSize= max(maxSize, self.size[i])
        return maxSize


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n= len(nums)
        dsu= DSU(n)
        # to avoid repetition we have to keep value of num and to do union we need index of already added ele.
        numToIndex= collections.defaultdict(int) # [num: index]
        for i, num in enumerate(nums):
            if num in numToIndex:  # means we have alreay added this to a component
                continue
            # Try to merge(union) 'num' with any of the adjacent number which is already included i.e 'num+1' and 'num-1'
            # we will do union with the index value.
            if num + 1 in numToIndex:
                dsu.union(i, numToIndex[num + 1])
            if num - 1 in numToIndex:
                dsu.union(i, numToIndex[num - 1])
            # Add this curr num in hashmap
            numToIndex[num]= i
        
        # return dsu.getLongestSequence() if nums else 0
        return max(dsu.size) if nums else 0  # shortcut
    

# Note: other methods in hashing