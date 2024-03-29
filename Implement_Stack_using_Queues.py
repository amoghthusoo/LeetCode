class MyStack:

    def __init__(self):
        self.queue_1 = list()
        self.queue_2 = list()
        self.active = 1       

    def push(self, x: int) -> None:

        if(self.active == 1):
            self.queue_1.append(x)
        elif(self.active == 2):
            self.queue_2.append(x)

    def pop(self) -> int:
        
        if(self.active == 1):
            
            self.active = 2

            while(True):

                dequeued = self.queue_1.pop(0)

                if(len(self.queue_1) == 0):
                    return dequeued
                else:
                    self.queue_2.append(dequeued)
        
        elif(self.active == 2):
            
            self.active = 1

            while(True):

                dequeued = self.queue_2.pop(0)

                if(len(self.queue_2) == 0):
                    return dequeued
                else:
                    self.queue_1.append(dequeued)


    def top(self) -> int:
        if(self.active == 1):
            
            self.active = 2

            while(True):

                dequeued = self.queue_1.pop(0)

                if(len(self.queue_1) == 0):
                    self.queue_2.append(dequeued)
                    return dequeued
                else:
                    self.queue_2.append(dequeued)
        
        elif(self.active == 2):
            
            self.active = 1

            while(True):

                dequeued = self.queue_2.pop(0)

                if(len(self.queue_2) == 0):
                    self.queue_1.append(dequeued)
                    return dequeued
                else:
                    self.queue_1.append(dequeued)

    def empty(self) -> bool:

        if(len(self.queue_1) == 0 and len(self.queue_2) == 0):
            return True

        else:
            return False        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()