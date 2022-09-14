def palin(arr):
    arr_odd, arr_even= [],[]
    for num in arr:
        if num%2== 0:
            arr_even.append(num)
        else:
            arr_odd.append(num)
    print(arr_odd)
    print(arr_even)
a= [1,2,3,4,5,6,7]
palin(a)