# Logic: Exactly same as "253. meeting Rooms II"
# except here in case of same arrival and depart time we will need one platform.
# (Given: At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.)

# Replace platform -> rooms

# Just copied pasted code of "253. meeting Rooms II".

class Solution:    
    def minimumPlatform(self,n,arr,dep):
        start= sorted(arr)
        end=   sorted(dep)
        ans, count= 0, 0
        s, e= 0, 0  # pointer to start and end array
        while s < len(start):  # till we have started all the meetings
            # overlapping so we will need one new room.
            if start[s] <= end[e]:
                count+= 1  # allocated new room for overlapping meeting 
                s+= 1   # started one so incr 's' by '1'.
                ans= max(ans, count)
            else:
                # one meeting ended. now the previous can be used for different meeting so decr total no of room required.
                count -= 1   
                e += 1
        return ans