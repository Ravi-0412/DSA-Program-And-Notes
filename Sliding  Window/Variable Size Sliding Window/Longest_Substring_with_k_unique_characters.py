# for max ans, longest ke liye jitna se jitna char repeat karne chahiye with 

# Note: To check the number of unique char at any point of time we will use hashmap.
# 

# 

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
    

# shorter way and concise way.
# Note: Try to solve every variable sliding window problem like this only.
# After seeing every char check for valid substring and update ans.
class Solution:
    
    def longestKSubstr(self, s, k):
        freq= {}
        i, j= 0, 0
        ans= -1
        longest= ""  # will give any such string
        while j < len(s):
            freq[s[j]]= 1 + freq.get(s[j], 0)
            while len(freq) > k:
                freq[s[i]]-= 1
                if freq[s[i]]== 0:
                    del freq[s[i]]
                i+= 1
            if len(freq)== k and j - i + 1 > len(longest):
                longest= s[i: j +1]
                ans= max(ans, j- i+ 1)
            j+= 1
        return ans

    


