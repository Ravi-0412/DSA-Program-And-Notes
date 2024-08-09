# Brute force: for each flight in range add given seats.
# time: O(n^2), space = O(n)

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Initialize the result array with zeros
        answer = [0] * n

        # Process each booking
        for booking in bookings:
            first, last, seats = booking
            # Update the seat counts for the range of flights
            for i in range(first - 1, last):
                answer[i] += seats

        return answer


# Optimisation using: Sweep line

# Idea:
# For a given booking: [first,last,seats], this could be assumed as 'seats' number of passengers are boarding 
# at the 'first' stop and leaving at the 'last+1' stop.

# For example consider a booking [3,4,10], here 10 passengers boarded the flight at 3rd stop and leaving at the 5th stop.

# So number of passengers at 3rd stop would be +10 and at 5th stop would be -10. Now the problem turns
# into finding the total number of passengers in the flight at each stop.

# According to given testcase, [[1,2,10],[2,3,20],[2,5,25]]
# Our stops array: [0,0,0,0,0,0] )(last =(6th)stop is destination stop and later we observe that it doesn't matter)
# Consider 1st booking: +10 at 1st stop and -10 at 3rd stop => [10,0,-10,0,0]
# Consider 2nd booking: +20 at 2nd stop and -20 at 4th stop => [10,20,-10,-20,0]
# Consider 3rd booking: +25 at 2nd stop and -25 at 6th stop=>[10,45,-10,-20,0,-25]

# So total passengers at each stop: [10,10+45,10+45-10,10+45-10-20,10+45-10-20+0,10+45-10-20+0-25]=[10,55,45,25,25,0]

# in short:
# updating manually each range(first , last) one by one will have same effect if:
# i) we add given seat to first flight and subtract given seats from 'last +1' flight &
# ii) Then take the cumulative sum to get number of reserved seats in each flight.

# Time: O(n) = space
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Initialize the result array with zeros
        answer = [0] * n

        # Process each booking
        for booking in bookings:
            first, last, seats = booking
            answer[first - 1] += seats
            if last < n:
                answer[last] -= seats
        for i in range(1, n):
            answer[i] += answer[i - 1]
        return answer


        