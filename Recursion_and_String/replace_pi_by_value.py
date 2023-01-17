# check for 1st and 2nd ele of the passing string
# if 1st== p and 2nd == i then call the fn after next two position
# else call after next one position
def ReplacePi(str1):
    ans= ""
    if len(str1)<2:
        return str1
    elif str1[0]== 'p' and str1[1]== 'i':
        ans+= "3.14" + ReplacePi(str1[2:])
    else:
        ans+= str1[0] + ReplacePi(str1[1:])
    return ans

print(ReplacePi("pippxxppiixipi"))
print(ReplacePi("pippppiiiipi"))


# you can use the same logic as 'Q no: 1910'.


