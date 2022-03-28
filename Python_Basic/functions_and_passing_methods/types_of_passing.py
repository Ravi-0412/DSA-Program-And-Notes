def update(x):
    print(id(x))  # will have same address as 'a' before update
    x= 8
    print(id(x))  # now will have diff address as 'a' after update
    print("x= ",x)

a= 10
print(id(a))
update(a)
print("a= ",a)

# will print x= 8 and a= 10 value of 'a' will not change 
# when you call a function ny passing a variable value,
# it is passed by value not by reference . here also we are passing 
# x whose value is equal to 8

def update(lst):
    print(id(lst))  # will have same address as 'a' before update
    lst[1]= 25
    print(id(lst))  # now will have diff address as 'a' after update
    print("updated lst= ",lst)

lst = [10,20,30]
print(id(lst))
update(lst)
print(id(lst))
print("lst: ", lst)

# will update the original list also since list is immutable
# in earlier cases it was not changing because that variable
# 'a' was type of int which is immutable


