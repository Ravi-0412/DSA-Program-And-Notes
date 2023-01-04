# exactly same as binary search
# just like we find the last position of an element.
class Solution:
    def nextGreatestLetter(self,letters, target):
        n= len(letters)
        low= 0
        high= n-1
        while(low<= high):
            mid= low+ (high- low)//2
            # if letters[mid]== target:
            #     return letters[(mid+1)%n]   # this will give the incorrect output 
                                              # if letters will be repeated then we may get
                                              # get the same ele as target at next index also
            if letters[mid]<= target: # in case if equal also then we will search for next greater 

                                      # and for this we have to update low= mid+1
                low= mid+ 1
            else:
                high= mid-1
        return letters[(low)%n]   # taking modulus to handle the case when ans doesn't exist.
                                  # in this case low will be= n and we have to return the 0th index letter only and 
                                  # if exist then low will give the ans directly.



