# logic: whenever you have to find the sorted sequence for unique things(order of sequence) given nodes, think of topological sort for a while 
# here node will be the char where both word will differ 

# logic: 1st find the all unique char by storing each char in dictionary or set
# here used set(for storing the adjacent char for each distinct char) inside a dictionary
# compare the adjacent word and where they differ make a directed edge between the char(from char1 to char2)
# now apply the topogical sorting alg to find the sequence if possible

# totally correct only
class Solution:
    def alien_order(self, words: List[str]) -> str:
        # find out the each distinct char and make them as key 
        # later we will store the adjacent char in val of these char
        dic= {c:set() for w in words for c in w }  # first it will go to each word then each char inside that word
        
        # now compare the each char of adjacent word to know their order
        for i in range(len(words)-1):
            w1, w2= words[i], words[i+1]
            # check for prefix condition , corner case (invalid one)
            minLength= min(len(w1),len(w2))
            # if w1 is prefix of w2 but w2 is coming before w1
            if len(w1) > len(w2) and w1[:minLength]== w2[:minLength]:
                return "" 
            # now compare the char in both the words
            for j in range(minLength):   # you have to compare till minLength only not till max length of two words..
                # means w2[j] will come later than w1[j]. so make a directed edge from w1[j] to w2[j] i.e add w2[j] in adjacency list of w1[j]
                if w1[j]!= w2[j]: 
                    dic[w1[j]].add(w2[j])
                    break  # no need to check further char

        print(dic)
        # will store each char and 'False' or 'True' value wrt that char
        # False: means that char and all its adjacent char is already visited before(pre cycle) so skip this
        # True: means that char is visited in current cycle only means cycle
        visited={}  
        ans= []
        def iscycle(c):
            if c in visited:
                return visited[c]    # True means cycle, false means to skip
            visited[c]= True
            for nei in dic[c]:
                if iscycle(nei):
                    return True
            visited[c]= False      # means we have visited this node as well as all its adjacent node
            ans.append(c)
            
        # here you can call dfs on any char 
        for c in dic:
            if iscycle(c):
                return ""
        ans.reverse()
        return "".join(ans)
        
