
# Solution:
# the tower from which you are moving the disc that will the source
# and to which you are moving that will be the destination,
# and tower that will be remaining at any moment that will work as helper.

def toh(n, s, d, h):
    m= 2**n -1  # will print the total no of move at last
    if n==0:  # if n is zero simply return
        return
    else:
        toh(n-1,s,h,d) # 1st move the 'n-1' disc to the helper with the help of destination
        print("{}[{}->{}]".format(n,s,d))   # move the nth disc directly from source to destination as only largest disc will be on
                                            # after this largest disc will be getting placed at the destination
        toh(n-1,h,d,s)      # now move the 'n-1' disc from the helper to the destination with the help of source
    return m
    
print(toh(3,'s','d','h'))   # '3' means [3,2,1] on the first disc , here on source 's'. and we have move first three disc from top .
