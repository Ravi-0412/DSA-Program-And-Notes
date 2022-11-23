# eaxctly same as 'longest substring with k distinct char'
# only change the condition i.e len(hashmap)<=k

def length_of_longest_substring_k_distinct(s, k):
        hashmap,max_length,i,j,n= {},0,0,0,len(s)
        # len(hashmap) at any point will give the no of distinct char for that window
        while j<n:
            hashmap[s[j]]= 1+ hashmap.get(s[j],0)
            if len(hashmap)<=k:
                max_length= max(max_length,j-i+1)
            elif len(hashmap)> k:
                while len(hashmap)> k:
                    hashmap[s[i]]-= 1
                    if hashmap[s[i]]== 0:
                        hashmap.pop(s[i])
                        if len(hashmap)<= k:
                            max_length= max(max_length,j-i)
                    i+= 1
            j+= 1
        # print("longest substring is: ",s[i:j+1])
        return max_length

