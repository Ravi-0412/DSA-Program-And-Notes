# for num having perfect root
# time complexity= root(n)

# def square_root(n):
#     i=2
#     while(i*i<=n):
#         i+= 1
#     return i-1
# print(square_root(36))


#method2: time- O(logn)
# for perfect square number

# def square_root(n):
#     start,end= 0,n
#     while(start<=end):
#         mid= start+ (end-start)//2
#         if mid*mid==n:
#             return mid
#         elif mid*mid>n:
#             end= mid-1
#         else:
#             start= mid+1
# print(square_root(36))


# if you want to get the decimal places also
#time complexity nearly equal= o(logn) as  time complexity of precision 
# will be very less as compared to 'nlogn'
def square_root(n,precision):
    start,end,root= 0,n, 0.0  # root will store the square root
    while(start<=end):
        mid= start+ (end-start)//2
        if mid*mid==n:
            root= mid   # means integral part is got stored in root
            return mid
        elif mid*mid>n:
            end= mid-1
        else:
            start= mid+1

    # till now we have got the integral part
    # for getting the decimal part run a loop for "precision" times
    # and inc by 1/10 for 1st loop and 1/100 for 2nd for loop and so on

    incr= 0.1  # for getting 1st precision we have to incr by 0.1
    for i in range(precision):
        while(root*root<=n):
            root+= incr
        # to get the actual value of root subtract by 'incr'
        root-= incr
        # now divide the incr by 10 to get more precision
        incr/= 10

    return root

n= int(input("enter the no ou want to find square root: "))
precision= int(input("enter the no of decimal places : "))
print(square_root(n,precision))


# method3: by Newton Raph son method


