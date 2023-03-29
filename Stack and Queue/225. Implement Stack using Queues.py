# correct only biut giving runtime error.
# tried submitting on coding ninja.
# correct only

# time: all operation O(1) except push : O(n).

import collections
class Stack:
    def __init__(self):
        self.q= collections.deque([])

    def getSize(self):
        return len(self.q)

    def isEmpty(self):
        return len(self.q)== 0

    def push(self,ele):   # move all ele before the curr pushed to last, to bring the last pushed ele at first and so one.
        self.q.append(ele)
        for _ in range(len(self.q) -1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft() if self.q else -1

    def top(self):
        return self.q[0] if self.q else -1


# using two queue same approach only.