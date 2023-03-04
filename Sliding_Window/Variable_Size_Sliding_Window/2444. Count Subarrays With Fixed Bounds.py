# why this working?
# Ans: agar hmko ek window mil gya h condition ke saath then agar kuch ele ko hta de min(jahan min mila, jahan max mila) h uske phle then wo sb bhi mera ans me count hoga.
# e.g: mera ans subarray ka start_index 4 h and min hmko 7 pe mila h, max hmko 9 pe mila h then agar hm index '4' to '6'(just before min of both) index tak ele hta bhi denge,
# tb bhi ans pe effect nhi padega , wo sb bhi ans me count hoga. and jb hm '7' index ho htayenge tb jake mera ans affect hoga.
# isliye: min(latestMinIndex, latestMaxIndex) - subArrStartIndex + 1) . '1' for actual subarray no extra ele.

# vvi: agar extra ele ata h condition satisfy hone ke bad then kisi bhi subarray ke saath wo ja sakta h jo ki hmara ans ho sakta h. 
# tb tak ja sakta h tjb tak hmko koi invalid element na mile.
# and hmara ans h: min(latestMinIndex, latestMaxIndex) - subArrStartIndex + 1) . jo already calculated h.

# isliye har ele ke liye same formaula lagta rhega jb tak koi invalid ele na mil jaye.
# agar invalid milega tb count+= 0 hoga and samw with agar dono i.e minK and maxK nhi milta h tb.

# time: O(n), space: O(1)
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count= 0
        subArrStartIndex= 0  # denotes the index from which our next desired subarray can start 
        latestMinIndex= -1
        latestMaxIndex= -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:   # if we get any ele out of bound i.e smaller than minK and greater than maxK then we have to initialise all the variable
                latestMinIndex, latestMaxIndex= -1, -1
                subArrStartIndex= i + 1  # our next desired subarray can start only after 'i'
            if nums[i]== minK:
                latestMinIndex= i
            if nums[i]== maxK:
                latestMaxIndex= i
            count+= max(0, min(latestMinIndex, latestMaxIndex) - subArrStartIndex + 1)   # can go in negative also so taking max with '0'.
        return count
