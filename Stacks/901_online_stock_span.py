# just same method of finding 'next greater left'
# if no greater then index of arr+1 will be the ans
# since it means that the given ele is the greatest till now
# if any next greater exist then 'index of curr ele- index of next greater ele' will be the ans
# ans will give the 'next greater left'
# final will give the 'actual ans'
def calculateSpan1(a,n):
    stack, ans, final= [], [], []
    # ans keep track of next greater ele left
    # final is storing the actual ans
    for i in range(n):
        while stack and stack[-1]<= a[i]:
            stack.pop()
        if stack==[]:  # means all ele  are smaller than current ele
            final.append(i+1)
            ans.append(-1)
            stack.append(a[i])
        else:  # measn you have got the next greater left
            j= i- a.index(stack[-1])
            final.append(j)
            ans.append(stack[-1])
            stack.append(a[i])
    return final

price = [10, 4, 5, 90, 120, 80]
# price= [100,80,60,70,60,75,85]
# print(calculateSpan1(price,6))


# concise way of writing the above code
def calculateSpan2(a,n):
    stack, final= [], []
    for i in range(n):
        while stack and stack[-1]<= a[i]:
            stack.pop()
        span= i+1 if stack==[] else (i-a.index(stack[-1]))
        final.append(span)
        stack.append(a[i])
    return final

# price = [10, 4, 5, 90, 120, 80]
price= [100,80,60,70,60,75,85]
# print(calculateSpan2(price,7))


# better one than all above one
# just push the 'index' itself instead of arr value
# this way you can also solve all the variations of 'next greater/smaller': better way
def calculateSpan3(a,n):
        stack= []
        for i in range(n):
            while stack and a[stack[-1]]<= a[i]:  # compare the value of top index of stack with the curr_val
                stack.pop()
            if stack==[]:  # means no next greater left ele exist so ans= i+1 
                print(i+1,end=" ")
            else:  # means you have found the ans for the curr_ele
                print(i-stack[-1],end=" ")  # diff in index will be the ans
            stack.append(i)  # you have to append it always so better write outside the loop
        

n = 8
a= [100,80,60,70,60,75,85,110]
calculateSpan3(a,n)