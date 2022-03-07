# time complexity: sqrt(n)
# logic: take n= 20, if 2 divides  20 , then 
# 10 will also divide 20 as 2*10= 20
# so need to check for 10 again & so on for other no

def factors(n):
    i= 1
    upper= []   # to print into sorted and proper order
    while(i*i<=n):
        if n%i== 0:
            j= n/i
            print(i, end=" ")
            # print(int(j), end=" ")  # will print in improper order
            upper.append(j)  # will store in descending order
        i+= 1
    # now print the 'upper' from right side
    for i in range(len(upper)-1,-1,-1):
        print(int(upper[i]),end=" ")

factors(20)

