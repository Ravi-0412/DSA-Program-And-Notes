# just same logic as 'count the subarry with sum==k for positive no" as no chance for becoming len(hashamp) < k once it has become equal to 'k' like positiev number
# window size should contain exactly k unique char no matter what your window size is

# longest ke liye jitna se jitna char repeat karne chahiye

# time: O(n)= space
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
            elif len(hashmap)> k:  # means there is more than k distinct ele present in the hashmap and so bring the len(hasmap)==k taki unique char ka count= k ho jaye
                # start decr the count of char from ith position till no of distinct char in hashmap becomes < k
                while len(hashmap)> k:  # because char at 'ith' index can be present more than one times
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
    

# note in this there is no need to update 'i' once you reaches 'j-i+1==k or j+>=k" 
# since we have to find longest then better we will increase the window size as much as possible
# that's why we didn't write the condition like "if j+1>=k" like fixed size window
# here window is variable so we update once reach the condition and update the window not like fixed size sliding window
