# 2nd method:
# just store if you find any negative no in the win arr
# once you will reach the size of the win array
# if win not empty then 1st index of 'win' will be the ans for that window
# if empty means no negative ele present for that window, so print(1)
# after reaching win, check if arr[i] <0 , then you remove the 1st ele from 'win'
# since that can't be the ans for next win as you are moving for the next win

# time = O(n)

from collections import deque
def printFirstNegativeInteger( A, N, K):
    win= deque()
    i,j= 0,0
    while j <N:
        if A[j]<0:  # appj in 'win' 
            win.append(A[j])
        if j+1 >=K:    # means you have reached the req win size
            if not win:     # if win empty
                print(0, end=" ")
            else:       # if win not empty
                print(win[0], end=" ")
                if A[i]<0:   # then remove ele of 'i' index from win i.e first ele from win
                            # tabhi remove kar sakte h jb 'i'th index ele negative ho like jb property ko follow kar rha hoga tabhi remove karenge n
                            # Kyonki remove karte samay property check karke dale the.
                    win.popleft()
            i+= 1
        j+= 1

N = 5
A = [-8, 2, 3, -6, 10]
K = 2

# N = 8
# A = [12, -1, -7, 8, -15, 30, 16, 28]
# K = 3

# A = [5, -2, 3, 4, -5]
# K = 2
# N= len(A)
printFirstNegativeInteger(A, N, K)


# Note VVVI: ek cheez fixed sliding window me hmesha yaad rakho
# 1)agar koi ele ans wala condition ko follow kar rha h tb include karte raho ya ans ke anusar(liye) 
# curr index wala ele here 'j' me operation karte raho..and

# 2) then check karo required window size reach hua h? jb window reach kar jaye to 
# ans update karo and inside this agar pre index wala ele here 'i' 
# agar condition ko follow kar rha ho tb remove kar do ya jo bhi ans ke anusar karna ho 'i'th index wale ele pe operation karo
# yhi do case bnega isme 
# 'i' ko incr kar do.