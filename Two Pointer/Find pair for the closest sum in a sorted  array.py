# just "two sum logic of sorted array".


def twoSum(numbers, target):
        n= len(numbers)
        minDiff= float('inf')
        ele1, ele2= 0, 0
        start, end= 0, n-1
        while start< end:  
            sum= numbers[start] + numbers[end]
            diff= abs(target - sum)
            if diff < minDiff:
                minDiff= min(minDiff, diff)
                ele1, ele2= numbers[start], numbers[end]
            if diff== 0:
                # Can't be better than this 
                break
            
            elif sum > target:
                end-= 1
            else:
                start+= 1
        print("pair is: ", ele1, ele2)

arr= [10, 22, 28, 29, 30, 40]
x= 54

# arr= [1, 3, 4, 7, 10]
# x= 15
twoSum(arr, x)

