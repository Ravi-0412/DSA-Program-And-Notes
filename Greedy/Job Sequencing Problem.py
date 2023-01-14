# on GFg comparator function was not working. so did in online compipler and giving correct result.
# time: O(n^2)

def JobScheduling(Jobs,n):
    Jobs.sort(key= sortThird, reverse= True)
    # print(Jobs)
    max_deadline_job= max(Jobs, key= f)   # it will return the job information with max deadline
    max_deadline= max_deadline_job[1]     # it will return the job max deadline of all jobs
    # print(max_deadline_job)
    # print(max_deadline)
    
    position= [-1]*max_deadline
    jobs_done, maxProfit= 0, 0
    # now place the job with maximum profit as far as possible.
    for job in Jobs:
        id, deadline, profit= job[0], job[1], job[2]
        for j in range(deadline-1, -1, -1):
            if position[j]== -1:
                position[j]= id
                maxProfit+= profit
                jobs_done+= 1
                break
    return [jobs_done, maxProfit]

def sortThird(val):
    return val[2]    # will sort the list based on 2nd index value.
def f(val):
    # print(val, val[1])
    return val[1]

# Jobs= [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
# Jobs= [(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)]
# Jobs= [(1,3,2),(2,3,4),(3,3,3),(4,4,1),(5,4,10)]
Jobs= [(1,5,200),(2,3,180),(3,3,190),(4,2,300),(5,4,120),(6,2,100)]
n= len(Jobs)
print(JobScheduling(Jobs,n))

# python used function and methods
# https://www.geeksforgeeks.org/python-list-sort-method/
# https://www.askpython.com/python/built-in-methods/python-max-method