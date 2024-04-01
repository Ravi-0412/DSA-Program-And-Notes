# why this working?
# Ans: agar hmko ek window mil gya h condition ke saath then agar kuch ele ko hta de 
# min(jahan min mila, jahan max mila) h uske phle then wo sb bhi mera ans me count hoga.
# e.g: mera ans subarray ka start_index 4 h and min hmko 7 pe mila h, max hmko 9 pe mila h 
# then agar hm index '4' to '6'(just before min of both) index tak ele hta bhi denge,
# tb bhi ans pe effect nhi padega , wo sb bhi ans me count hoga. and jb hm '7' index ho htayenge tb jake mera ans affect hoga.
# isliye: min(latestMinIndex, latestMaxIndex) - subArrStartIndex + 1 .

# How we are arriving to above mathematical formula?
# e.g: [9,5,4,3,5,6,7,5,5, 6,4],. mink = 3, maxk = 7
# suppose we are at index 9. subArrStartIndex = 1, latestMinIndex = 3, latestMaxIndex = 6
# For ele at index 9 i.e '6', what will no of new subarray we will get?
# 1st we have to cover the range 'latestMaxIndex = 6' to 'latestMinIndex = 3' including all the elements 
# in between i.e index 7 and index 8 wihout any choice because that the requirement of q so add '+1' for this subarray ans i.e
# [5,4,3,5,6,7,5,5, 6] index 'latestMinIndex' to current index '8'.
# But for element beyond(left) min('latestMinIndex', 'subArrStartIndex'), we can include one ele, two ele, ...& so on and
# all will be valid answer only . No of such subarray = min(latestMinIndex, latestMaxIndex) - subArrStartIndex

# So total new subarray = min(latestMinIndex, latestMaxIndex) - subArrStartIndex + 1 

# Note: min(latestMinIndex, latestMaxIndex) != -1 will make sure that both minimum and maximum ele is found.

# vvi: agar extra ele ata h condition satisfy hone ke bad then kisi bhi subarray ke saath wo ja sakta h jo ki hmara ans ho sakta h. 
# tb tak ja sakta h tjb tak hmko koi invalid element na mile.
# and hmara ans h: min(latestMinIndex, latestMaxIndex) - subArrStartIndex + 1) . jo already calculated h.

# isliye har ele ke liye same formula lagate rhenge jb tak koi invalid ele na mil jaye.
# agar invalid milega tb count+= 0 hoga and same with agar dono i.e minK and maxK nhi milta h tb.

# time: O(n), space: O(1)
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count= 0
        subArrStartIndex= 0  # denotes the index from which our next desired subarray can start 
        latestMinIndex= -1
        latestMaxIndex= -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                # if we get any ele out of bound i.e smaller than minK and greater than maxK then we have to initialise all the variable  
                latestMinIndex, latestMaxIndex= -1, -1
                subArrStartIndex= i + 1  # our next desired subarray can start only after 'i'
            if nums[i]== minK:
                latestMinIndex= i
            if nums[i]== maxK:
                latestMaxIndex= i
            count+= max(0, min(latestMinIndex, latestMaxIndex) - subArrStartIndex + 1)   # can go in negative also so taking max with '0'.
        return count
