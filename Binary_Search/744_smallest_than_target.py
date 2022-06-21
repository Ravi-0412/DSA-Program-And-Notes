# exactly same as binary search
def nextGreatestLetter(letters, target):
        n= len(letters)
        low= 0
        high= n-1
        while(low<= high):
            mid= int(low+ (high- low)/2)
            # if letters[mid]== target:
            #     return letters[(mid+1)%n]   # this will give the incorrect output 
                                              # if letters will be repeated then we may get
                                              # get the same ele as target at next index also
            if letters[mid]<= target: # in case if equal also then we will search for next greater 

                                      # and for this we have to update low= mid+1
                low= mid+ 1
            else:
                high= mid-1
        # print(letters[high])
        return letters[(low)%n]    # % to handle the case of wrap around 
                                   # in wrap around condition value of low after
                                   # after this loop fails will be n-1 and in 
                                # this case we have to return the '0' index element

# 2nd method:
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n= len(letters)
        low= 0
        high= n-1
        ans= None
        while(low<= high):
            mid= int(low+ (high- low)/2)
            # if letters[mid]== target:
            #     return letters[(mid+1)%n]
            if letters[mid]<=target: 
                low= mid+ 1
            else: # this may give the ans
                ans= letters[mid]
                high= mid-1
        return letters[0] if ans== None else ans   # if ans== None means target is the last ele so in this case return the 1st ele
                                                   # otherwise return the ans

