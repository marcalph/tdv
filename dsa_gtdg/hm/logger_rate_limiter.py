# Design a logger system that receives a stream of messages 
# along with their timestamps. 
# Each unique message should only be printed at most every 
# 10 seconds (i.e. a message printed at timestamp t will 
# prevent other identical messages from being printed until 
# timestamp t + 10).

# All messages will come in chronological order. 
# Several messages may arrive at the same timestamp.

# Implement the Logger class:

# Logger() Initializes the logger object.
# bool shouldPrintMessage(int timestamp, string message) 
#     Returns true if the message should be printed in the given timestamp, otherwise returns false.


# O(1) time| O(m)space
class Logger:
    def __init__(self):
        self.previous = {} #msg:timestamp
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.previous:
            if self.previous[message]+10<=timestamp:
                self.previous[message]=timestamp
                return True
            else:
                return False
        else:
            self.previous[message]=timestamp
            return True
        
