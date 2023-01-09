# time complexity: sqrt(n)
# logic: take n= 20, if 2 divides  20 , then 
# 10 will also divide 20 as 2*10= 20
# so no need to check for 10 again & so on for other no.. only to check till

def factors(n):
    i= 1
    ans= []   # to print into sorted and proper order
    while(i*i<=n):
        if n%i== 0:
            j= n/i
            print(i, end=" ")  # smaller factor printing and larger factors storing in ans to print at last
            # print(int(j), end=" ")  # will print in improper order
            ans.append(j)  # will store in descending order
        i+= 1
    # now print the 'upper' from right side to get all factors in ascending order
    for i in range(len(ans)-1,-1,-1):
        print(int(ans[i]),end=" ")

factors(20)

