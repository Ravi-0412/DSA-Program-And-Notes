"""
Q) Interviewer gives me a question on parking lot where I would be given an array of pairs(vehicleType, slots) and another array of pairs(vehicleType, costPerMin)
Three functions were given:
initialize(vector<pair<string, int>> slotsPerType, vector<pair<string, int>> costPerMinPerType);
bool onEnter(string plateNumber);
int onExit(string plateNumber); // returns calculated cost & -1 otherwise

Ans :  Simple, just do whatever they are telling to do.

Tiem : O(T) , T is the number of vehicle types.
"""

import time
import math

class ParkingLot:
    def __init__(self):
        # Maps vehicleType -> count of available slots
        self.availability = {}
        # Maps vehicleType -> cost per minute
        self.rates = {}
        # Maps plateNumber -> (entry_time, vehicle_type)
        self.active_sessions = {}

    def initialize(self, slotsPerType, costPerMinPerType):
        """
        Initializes the parking lot configuration.
        slotsPerType: list of (type, count)
        costPerMinPerType: list of (type, cost)
        """
        for v_type, count in slotsPerType:
            self.availability[v_type] = count
            
        for v_type, cost in costPerMinPerType:
            self.rates[v_type] = cost

    def _get_vehicle_type_from_plate(self, plateNumber):
        """
        Logic to identify vehicle type. In an interview, ask if 
        this is provided or if we should assume a default.
        """
        return "Car" # Mock implementation

    def onEnter(self, plateNumber: str) -> bool:    # O(1)
        v_type = self._get_vehicle_type_from_plate(plateNumber)
        
        # Check if type exists and has available space
        if v_type in self.availability and self.availability[v_type] > 0:
            # Record entry time and decrement slots
            self.active_sessions[plateNumber] = (time.time(), v_type)
            self.availability[v_type] -= 1
            return True
            
        return False

    def onExit(self, plateNumber: str) -> int:    # O(1)
        # Check if the vehicle is actually in the lot
        if plateNumber not in self.active_sessions:
            return -1
            
        entry_time, v_type = self.active_sessions.pop(plateNumber)
        exit_time = time.time()
        
        # Calculate duration in minutes (rounding up)
        duration_seconds = exit_time - entry_time
        duration_minutes = math.ceil(duration_seconds / 60)
        
        # Calculate total cost
        total_cost = duration_minutes * self.rates.get(v_type, 0)
        
        # Free up the slot
        self.availability[v_type] += 1
        
        return total_cost

  # follow ups
  """
  Write unit test case also.

  for this we have modified original code also a bit.
  """

import time
import math

class ParkingLot:
    def __init__(self):
        self.availability = {}
        self.rates = {}
        self.active_sessions = {}

    def initialize(self, slotsPerType, costPerMinPerType):
        self.availability = {v_type: count for v_type, count in slotsPerType}
        self.rates = {v_type: cost for v_type, cost in costPerMinPerType}

    def onEnter(self, plateNumber, vehicleType):
        if self.availability.get(vehicleType, 0) > 0:
            # Logic: Use the ACTUAL system time
            self.active_sessions[plateNumber] = (time.time(), vehicleType)
            self.availability[vehicleType] -= 1
            return True
        return False

    def onExit(self, plateNumber):
        if plateNumber not in self.active_sessions:
            return -1
        
        entry_time, v_type = self.active_sessions.pop(plateNumber)
        # Logic: Use the ACTUAL system time for exit
        duration_min = math.ceil((time.time() - entry_time) / 60)
        
        cost = duration_min * self.rates.get(v_type, 0)
        self.availability[v_type] += 1
        return cost


# Test class
"""
@patch('time.time') working ?

Ans : Inside your code: entry_time = time.time() is called.
Behind the scenes: Python looks at its phone book, sees that time.time has been replaced by your Mock Object, and calls that instead.
The Return: The Mock object returns the return_value you set (e.g., 1000.0).
"""
import unittest
from unittest.mock import patch

class TestParkingLotMock(unittest.TestCase):
    def setUp(self):
        self.pl = ParkingLot()
        self.pl.initialize([("Car", 1)], [("Car", 10)])

    # We "patch" the 'time.time' function inside the test
    @patch('time.time')
    def test_mocked_time_cost(self, mock_time):
        # 1. Simulate entry at T=1000
        mock_time.return_value = 1000.0 
        self.pl.onEnter("MOCK-1", "Car")

        # 2. Simulate exit at T=1121 (121 seconds later = 3 mins)
        mock_time.return_value = 1121.0
        cost = self.pl.onExit("MOCK-1")

        # 3. Validation
        self.assertEqual(cost, 30) # 3 minutes * 10



