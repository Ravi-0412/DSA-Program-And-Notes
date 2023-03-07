#prime numbers in a range by reducing its time complexity
# logic: only need to check till square root of the given number
# as after this num1*num2= given no will start repeating
# time: root(2) + root(3) + root(4)+ ...+ root(n)

# checking a number prime or not

import math
def isprime(n):
    if n==2:
        return True
    root= int(math.sqrt(n))
    i= 2
    while(i<=root):  # check from 2 to root of that number  
    # or while(i*i<=n):   # if you don't want to find the square root of the num
        if n%i==0:
            return False
        i+= 1
    return True


# for to check in a range, if any number is not prime then
# no need to check its multiple 
# in this way we have only to run loop till 'square_root(range)' 
# as after this no will start repeating if it is not prime
# as any non prime no must have at least one divisor till its square root
# for program: start from 2 and make all its multiple as false(not prime) 
# till root(range)

# True in the array means no is prime
def isprime(num,primes):
    # start from 2 and make all multiples of two as false 
    # all multiples of 2 will not be prime
    # repeat this till for all prime till root(range)
    i=2
    while(i*i<=num):    # make all muliples of prime no like 2,3,5, till root(range) as false
        if primes[i]:  # if true means we haven't visited this no 

            # now make the index multiple of 'i' as False
            j= i*2
            while(j<=num):   # this will also go till root(range)
                primes[j]=False
                j+= i    # incr by 'i' to go to the multiple of 'i'
        i+= 1

num= int(input("enter the range: "))
primes= [True]*(num+1)  # iniliase with True & if no has any multiple then
                        # make the value at index of that num as 'false'
isprime(num,primes)

# now print the number where primes is true
for i in range(num+1):
    if primes[i]:
        print(i,end=" ")

# time complexity: n/2 + n/3 + n/5 +n/7 +.... n/p (where p will be the nearest prime to num)
# n(1/2 + 1/3+ 1/5+ 1/7 +.....)= n(loglogn)


 



      

  
