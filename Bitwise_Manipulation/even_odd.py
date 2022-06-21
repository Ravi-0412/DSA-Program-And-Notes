# logic: 
# in binary if last bit(LSB) is '1' then it means odd 
# otherewise even

# and 'AND' of any no with all '1' is no itself
# but we only need to check the last bit
# so take the 'AND' of the no with '1' 
# if 'AND'==1 then means odd otherwise means even

def even_odd(n):
    # if n & 1==1:
    #     print("odd")
    # else:
    #     print("even")
    print("even") if n & 1== 0 else print("odd")
even_odd(5)
even_odd(10)

