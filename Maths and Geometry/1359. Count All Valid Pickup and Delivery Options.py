# Method 1:
# logic: pick up must be before delivery.
# So first put all the 'n' pick ups.
# no of ways of putting all 'n' pickups = (n!) as order of individual pick up is not mattering.

# Now we have to arrange all 'n' delivery.
# total ways to arrange delivery = 1 * 3 *5 * 7 * (2*n -1).....

# How?
# Denote pickup 1, pickup 2, pickup 3, ... as A, B, C, ...
# Denote delivery 1, delivery 2, delivery 3, ... as a, b, c, ...
# We need to ensure a is behind A, b is behind B, ...

# This solution involves 2 stages.

# Stage 1
# We decide the order of all the pickups.there are n! possibilities

# Stage 2
# Given one possibility. Let's say the pickups are ordered like this A B C
# We can now insert the corresponding deliveries one by one.
# We start with the last pickup we made, namely, insert c, and there is only 1 valid slot.
# A B C c
# We continue with the second last pickup we made, namely, insert b, and there are 3 valid slots.
# A B x C x c x (where x denotes the location of valid slots for b)
# Let's only consider one case A B C c b. We continue with the third last pickup we made, namely, insert a, and there are 5 valid slots.
# A x B x C x c x b x, (where x denotes the location of valid slots for a)
# In conclusion. we have in total 1 * 3 * 5 * ... * (2n-1) possibilities.

# In short:
# for 1st delivery 'c', only : 1 option
# for 2nd delivery 'b' , there is : 3 choice i.e we have put '1' pair at proper place so gaps formed by these pair = 2 * 1 + 1 = 3
# for 3rd delivery, 'a', there is : 5 choice i.e we have put '2' pair at proper place so gaps formed by these pair = 2 *2 + 1 = 5
# And so on till '2n-1'
# Thus, the final solution is n! * (1 * 3 * 5 * ... * (2n-1)) % 1000000007

class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        pickup_permutation = factorial(n) % mod
        delivery_permutation = 1
        for i in range(1, 2*n , 2):
            delivery_permutation = (delivery_permutation * i) % mod
        return (pickup_permutation * delivery_permutation) % mod
    

# Method 2:
# Assume we have already n - 1 pairs, now we need to insert the nth pair.
# To insert the next pickup , we have (n -1)*2 + 1 choice. 
# To insert the next delivery after inserting pick up, (n -1)*2 + 1 + 1 choice. after adding pick up gap will increase by '1'.

# Considering that delivery(i) is always after of pickup(i), we need to divide 2. 
# Because while inserting we are not taking care of this condition.

# Time = space = O(n)

class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        mod = 10**9 + 7
        dp = [1 for i in range(n + 1)]
        dp[1] = 1
        for i in range(2, n+1):
            pickUpWays =  (i - 1)*2 + 1
            deliverWays = pickUpWays + 1  # after adding pick up gap will increase by '1'.
            totalWays = (pickUpWays * deliverWays) //2
            dp[i] = (dp[i - 1] * totalWays) % mod
        return dp[n]


# Optimising space
#  Time = O(n), space = O(1)
class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        mod = 10**9 + 7
        ans = 1
        for i in range(2, n+1):
            pickUpWays =  (i - 1)*2 + 1
            deliverWays = pickUpWays + 1  # '1' after adding pick up.
            totalWays = (pickUpWays * deliverWays) //2
            ans = (ans * totalWays) % mod
        return ans



# Note: Another way of asking same Q .
# Already asked in one company
# Q: https://leetcode.com/discuss/interview-question/846916/Validate-Orders-Path-(Doordash)

# Q:
# Given a set list of pickups and deliveries for order, figure out if the given list is valid or not.
# A delivery cannot happen for an order before pickup.

# Examples below:
# [P1, P2, D1, D2]==>valid
# [P1, D1, P2, D2]==>valid
# [P1, D2, D1, P2]==>invalid
# [P1, D2]==>invalid
# [P1, P2]==>invalid
# [P1, D1, D1]==>invalid
# []==>valid
# [P1, P1, D1]==>invalid
# [P1, P1, D1, D1]==>invalid
# [P1, D1, P1]==>invalid
# [P1, D1, P1, D1]==>invalid


# Solution:

def isValid(orders):
    pickupSet =   set()
    deliverySet = set()
    
    for order in orders:
        taskType = order[0]
        taskNo =   order[1: ]
        if taskType == 'P':
            # if pickup
            if taskNo  in pickupSet or taskNo in deliverySet:
                # if picking up again or got delivered before pick up
                return "Invalid"
            pickupSet.add(taskNo)
        
        elif taskType == 'D':
            # if delivery
            if taskNo in deliverySet or  taskNo not in pickupSet:
                # if already delivered or  not pick up before
                return "Invalid"
            deliverySet.add(taskNo)
        else:
            return "Invalid"
    
    return "Valid" if len(pickupSet) == len(deliverySet) else "Invalid"

list_orders = [
    ['P1', 'P2', 'D1', 'D2'], 
    ['P1', 'D1', 'P2', 'D2'], 
    ['P1', 'D2', 'D1', 'P2'], 
    ['P1', 'D2'], 
    ['P1', 'P2'], 
    ['P1', 'D1', 'D1'], 
    [], 
    ['P1', 'P1', 'D1'], 
    ['P1', 'P1', 'D1', 'D1'], 
    ['P1', 'D1', 'P1'], 
    ['P1', 'D1', 'P1', 'D1']
    ]

for order in list_orders:
    print(order, isValid(order))
