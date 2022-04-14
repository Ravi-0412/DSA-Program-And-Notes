# just same logic as 'count the subarry with sum==k for positive no"
# window size should contain exactly k unique char no matter what your window size is

class Solution:
    def longestKSubstr(self, s, k):
        hashmap,max_length,i,j,n= {},0,0,0,len(s)
        # since we have to store the distint ele 
        # and also their count in case len(hashmap) goes greater than k
        # so we have to use hashmap
        while j<n:
            hashmap[s[j]]= 1+ hashmap.get(s[j],0)  # if char is presnt then incr the count otherwise append that char with count=1
            if len(hashmap)== k: # means you have found one of the ans ,check for max_length
                max_length= max(max_length,j-i+1)
            elif len(hashmap)> k:  # means there is more than k distinct ele present in the hashmap and also in the window
                # start decr the count of char from ith position till no of distinct char in hashmap becomes < k
                while len(hashmap)> k:
                    hashmap[s[i]]-= 1
                    # while decr the count,if count of any char becomes zero then pop that char
                    # as even count will become zero , char will be still there in the hashmap
                    if hashmap[s[i]]== 0:
                        hashmap.pop(s[i])
                        if len(hashmap)== k:  # in case of poping one char from hashmap, its length can become equal to 'k'
                            max_length= max(max_length,j-i)  # here only 'j-i' because 'i' is still pointing to the index of 
                                                             # deleted char that we don't have to include. so no need to add '+1'
                    i+= 1
            j+= 1  # have to incr 'j' so better write outside all the conditions
        print("longest substring is: ",s[i:j+1])  # it will print the last longest possible substring
        return -1 if max_length==0 else max_length
    

