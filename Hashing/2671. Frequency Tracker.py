# 1) for add:
# a) first decrease the no of count of the no = freqToNum[freqCount[num]] by '1'
# b) increase the freq of curr number
# c) incr the no of count of no= new freq of number i.e freqToNum[freqCount[num]] by '1'.

# Reason: freq of curr number will change by '1'. so we have to remove from count of pre freq and will add to the new freq.

# 2) for delete:
# same way as above

import collections
class FrequencyTracker:

    def __init__(self):
        self.freqCount = collections.defaultdict(int)
        self.freqToNum = collections.defaultdict(int)

    def add(self, number: int) -> None:
        # phle freq wale se hta do
        self.freqToNum[self.freqCount[number]] -= 1
        self.freqCount[number] += 1
        # nye freq wale me add kar do
        self.freqToNum[self.freqCount[number]] += 1

    def deleteOne(self, number: int) -> None:
        # phle freq wale se hta do
        self.freqToNum[self.freqCount[number]] -= 1
        self.freqCount[number] = max(0,self.freqCount[number] - 1)   # can't be negative 
        # nye freq wale me add kar do
        self.freqToNum[self.freqCount[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqToNum[frequency] > 0