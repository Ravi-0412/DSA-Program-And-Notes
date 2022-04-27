# other two methods are by 'Binary Search'
# method3: by Newton Raph son method
# formaula: root= (x +N/x)/2, where root is the actual root and 
# x is the root we have assumed
# logic: take x= n itsef for 1st time, and cal the root
# if fabs(root-x)<precision stop, you can take any value of precision
# else continue and update x= root itself
# time complexity= O((logn)*f(n)), where 
# f(n) is the cost of calculating  f(n)/f'(n) with n-digit precision

import math
def Newton_sqrt(n):
    x= n    # 1st time assume x= n itself
    root= 0.0
    while True:
        root= 0.5*(x+ n/x)
        if math.fabs(root-x)< 0.5:  # 0.5 is the precision or error allowed
            break
        # if precision is not made, update x= root itself
        x= root
    return root 
print(Newton_sqrt(40))


