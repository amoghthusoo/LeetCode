class MyQueue:

    def __init__(self):
        self.stack_1 = list()
        self.stack_2 = list()      

    def push(self, x: int) -> None:

        self.stack_1.append(x)

    def pop(self) -> int:
        
        popped = None
        while(True):

            popped = self.stack_1.pop()

            if(len(self.stack_1) != 0):
                self.stack_2.append(popped)
            else:
                break

        while(len(self.stack_2) != 0):
            self.stack_1.append(self.stack_2.pop())

        return popped


    def peek(self) -> int:

        popped = None
        while(True):
            popped = self.stack_1.pop()

            if(len(self.stack_1) != 0):
                self.stack_2.append(popped)
            else:
                self.stack_2.append(popped)
                break

        while(len(self.stack_2) != 0):
            self.stack_1.append(self.stack_2.pop())

        return popped

    def empty(self) -> bool:

        if(len(self.stack_1) == 0 and len(self.stack_2) == 0):
            return True

        else:
            return False        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(5)
# obj.push(6)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()