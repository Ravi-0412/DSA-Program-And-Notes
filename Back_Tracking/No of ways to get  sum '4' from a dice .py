# in notes 
def Form_Num(num,ans):
    res= []
    if num==0:
        return [ans]
    if num< 0:
        return []
    for i in range(1,num+1):  # add num <= given and call the fn again for remaining no
        res+= Form_Num(num-i,ans+ str(i))
    return res

print(Form_Num(4,""))
# print(Form_Num(6,""))