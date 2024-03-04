
# Here we can throw same dice again and again

# in notes 
def Form_Num(num,ans):
    res= []
    if num==0:
        return [ans]
    for i in range(1,num+1):  # add num <= given and call the fn again for remaining no. This is just like calling the same dice again & again.
        res+= Form_Num(num-i,ans+ str(i))
    return res

print(Form_Num(4,""))
# print(Form_Num(6,""))