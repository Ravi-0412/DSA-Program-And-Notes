# time: O(n)

def move(str1):
    m= str1.count('x')   # count the no of 'x' in the string
    ans= ""
    for i in range(len(str1)):  
        if str1[i]!= 'x':  #add when char is not 'x'
            ans+= str1[i]
    ans+= 'x'*m  # at last add 'm' no of 'x' at last
    return ans

print(move("geekxsforgexxeksxx"))


# method 2: By recursion
# just converted the above iterative method into recursive form
def MoveRecursion(str1,ans,count):
    if len(str1)==0:
        ans+= 'x'*count
        return ans
    elif str1[0]== 'x':
        count+= 1
        return MoveRecursion(str1[1:],ans,count)
    else:
        ans+= str1[0]
        return MoveRecursion(str1[1:],ans,count)

print(MoveRecursion("geekxsforgexxeksxx","",0))


# method3:(by recusrion)
# just print first other ele than 'x' and at last
# print all the 'x'
def MoveRecursion2(str1,ans):
    if len(str1)==0:
        return
    if str1[0]!='x':    # if not 'x' then simply print
        print(str1[0],end= "")
    MoveRecursion2(str1[1:],ans)   # else call fn for next index
    if str1[0]=='x':   # if you dont write this then will print everything again
                       # that has been printed in all the above fn calls
        print(str1[0],end= "")
    
MoveRecursion2("geekxsforgexxeksxx","")
print()  # to separate the output of below method

# method3:(by recusrion)(same logic as above one)
def MoveRecursion1(str1,ans):
    if len(str1)==0:
        return
    curr= str1[0]
    if str1[0]!='x':
        print(str1[0],end= "")
    MoveRecursion1(str1[1:],ans)
    if curr=='x':
        print(curr,end= "")
    
MoveRecursion1("geekxsforgexxeksxx","")


