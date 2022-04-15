# just same method of finding 'next greater left'
# if no greater then index of arr+1 will be the ans
# since it means that the given ele is the greatest till now
# if any next greater exist then 'index of curr ele- index of next greater ele' will be the ans
# ans will give the 'next greater left'
# final will give the 'actual ans'
def calculateSpan(a,n):
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
print(calculateSpan(price,6))


# concise way of writing the above code
def calculateSpan(a,n):
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
print(calculateSpan(price,7))