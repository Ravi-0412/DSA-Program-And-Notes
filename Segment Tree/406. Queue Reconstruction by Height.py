# Method 1: Sorting

# Logic: 1)We are fine with passing shorter person than us. 
# So let shorter person com enad choose their desire place.
# 2) for this sort based on height and in case of equal height sort according to 'people having more no taller person allowed should come first'.
# because for which 'no of taller person is less allowed' should choose their desire place so they should come later.

# 3) Now traverse the sorted array and insert people at their own position. 
# Just like insertion sort.

# Time : O(n^2)

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort the people from tall to short
        # insert from tall to short (insert at index = p[1])
        # people.sort(key=lambda p: p[0], reverse = True)   # in case p[0] is equal it will first bring smaller p[1] but we want greater p1[1] in case p[0] is smaller
        people.sort(key = lambda p : (- p[0], p[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


# later optimise uisng segment tree to O(nlogn).
# solution in sheet