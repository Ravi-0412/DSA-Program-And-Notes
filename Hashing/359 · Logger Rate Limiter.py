# Logic: A message should be printed if and only if it has not been printed in the last 10 seconds i.e
# message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10.

# 1) if message is coming for 1st time then , it will get printed.
# store the timestamp in this case

# 2) if message is already there:
# i) if time difference < 10 then it won't get printed, simply return False. No need to update timestamp in this case.
# ii) else will get printed and update the timestamp.

# Time: O(n)

class Logger:
    
    def __init__(self):
        self.lastPrintedTime = collections.defaultdict(int)

    def could_print_message(self, timestamp: int, message: str) -> bool:
        if message not in self.lastPrintedTime:
            self.lastPrintedTime[message] = timestamp
            return True
        else:
            if timestamp - self.lastPrintedTime[message] < 10:  # q definition is this only.
                return False
            else:
                self.lastPrintedTime[message] = timestamp 
                return True
            