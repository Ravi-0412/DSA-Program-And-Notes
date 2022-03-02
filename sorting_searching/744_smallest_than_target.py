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
            if letters[mid]<= target: 
                low= mid+ 1
            else:
                high= mid-1
        # print(letters[high])
        return letters[(low)%n]    # % to handle the case of wrap around 
                                   # in wrap around condition value of low after
                                   # after this loop fails will be n-1 and in 
                                # this case we have to return the '0' index element

arr= [2,3,5,9,14,16,18]
print(nextGreatestLetter(arr,14))
print(nextGreatestLetter(arr,15))
print(nextGreatestLetter(arr,4))
print(nextGreatestLetter(arr,9))
print(nextGreatestLetter(arr,8))
