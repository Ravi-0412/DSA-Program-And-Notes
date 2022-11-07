# 2nd method: 
# just store if you find any negative no in the win arr
# once you will reach the size of the win array
# if win not empty then 1st index of 'win' will be the ans for that window
# if empty means no negative ele present for that window, so print(1)
# after reaching win, check if arr[i] <0 , then you remove the 1st ele from 'win'
# since that can't be the ans for next win as you are moving for the next win
# def printFirstNegativeInteger( A, N, K):
#     win= []
#     i,j= 0,0
#     while(j<N):
#         if A[j]<0:  # append in 'win'
#             win.append(A[j])
#         if j-i+1< K:    # incr 'j' only
#             j+= 1
#         elif j-i+1== K:    # means you have reached the req win size
#             if not win:     # if win empty
#                 print(0, end=" ")
#             else:       # if win not empty
#                 print(win[0], end=" ")
#                 if A[i]<0:   # check for ele at 'i' index before moving to next win
#                     win.pop(0)
#             j+= 1
#             i+= 1

def printFirstNegativeInteger( A, N, K):
    win= []
    start,end= 0,0
    while end <N:
        if A[end]<0:  # append in 'win' 
            win.append(A[end])
            
        if A[j]<0:  
            win.append(A[j])
        if j-i+1< K:    # incr 'j' only
            j+= 1
        elif j-i+1== K:    # means you have reached the req win size
            if not win:     # if win empty
                print(0, end=" ")
            else:       # if win not empty
                print(win[0], end=" ")
                if A[i]<0:   # check for ele at 'i' index before moving to next win
                    win.pop(0)
            j+= 1
            i+= 1

# N = 5
# A = [-8, 2, 3, -6, 10]
# K = 2
# N = 8
# A = [12, -1, -7, 8, -15, 30, 16, 28]
# K = 3
A = [5, -2, 3, 4, -5]
K = 2
N= len(A)
printFirstNegativeInteger(A, N, K)
