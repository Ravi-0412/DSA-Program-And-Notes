# this q is tricky due to :"we have to return duplicates also".

# logic: we have to return duplicates also so will keep track of frequency.
# we will keep two hashmap 'pre' and cur to keep tarck of freq.

# we will only add c in 'cur' hashmap if 'c' is present in prev and cur[c] (freq[c]) < pre[c].
# because we have to find the commmon so we will take the minimum freq.

# time: O(n^2). n= # words= # char in each word.
# space: O(n)
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        pre= Counter(words[0])  
        for word in words[1:]:
            cur= collections.defaultdict(int)
            for c in word:
                if c in pre and cur[c] < pre[c]:   # to take the minimum freq of 'c' in both pre and cur.
                    cur[c]+= 1
            pre= cur

        ans= []
        for key, val in pre.items():
            temp= [key]*val
            ans.extend(temp)
        return ans


# very short way of writing the same logic.
# for thinking purpose and for interview purpose above above one is better.

# how it's working?
# dict 1 & dict 2 will intersect the two counters here, the lowest counts are preserved;
# 'elements()' is Counter's method, it just take the elements as many times as their counts.
# https://docs.python.org/3/library/collections.html#collections.Counter

# time= space= O(n)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res= Counter(words[0])
        for word in words[1:]:
            res= res & Counter(word)
        return list(res.elements())


# note: if would have asked for "only distinct char present in all words ".
# then if 'c' is prsent in pre then add to current.
# no need to check count.

# use hashmap to avoid duplicates. (we can't store string in set like s.add(c) that's why).
