# we only need to keep track of length of last elements which is equal to 'value'.
# for this take two pointer 'i' and 'j' both equal to say value say '0'.
# whenver we will see the num== value then we incr the 'j keep 'i' constant.
# And when we will see num!= value then we will make both pointer equal to any 'value'.

# Any point of time 'j-i' will give the length of last elements which have value== value.

class DataStream:
    
    def __init__(self, value: int, k: int):
        self.i= 0
        self.j= 0
        self.value= value
        self.k= k
        

    def consec(self, num: int) -> bool:
        if num== self.value:
            self.j+= 1
        else:
            self.i= self.j= 0
        return self.j - self.i >= self.k


# Method 2 :
# simplest

# We only need to check whether last 'k' char is equal or not.
# So simply mainitain a count 'cnt' that will tell the no of consecutive 'value' seen.

class DataStream:
    
    def __init__(self, value: int, k: int):
        self.cnt = 0
        self.value= value
        self.k= k
        

    def consec(self, num: int) -> bool:
        if num== self.value:
            self.cnt+= 1
        else:
            self.cnt = 0
        return self.cnt >= self.k