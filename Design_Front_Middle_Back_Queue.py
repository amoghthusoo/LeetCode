from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.dq = deque()

    def pushFront(self, val: int) -> None:
        self.dq.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        self.dq.insert(len(self.dq) // 2, val)

    def pushBack(self, val: int) -> None:
        self.dq.append(val)

    def popFront(self) -> int:

        if(len(self.dq) == 0):
            return -1 
        
        return self.dq.popleft()
        

    def popMiddle(self) -> int:

        if(len(self.dq) == 0):
            return -1
        
        if(len(self.dq) % 2 == 0):
            target_index = len(self.dq) // 2 - 1
        else:
            target_index = len(self.dq) // 2

        self.dq.rotate(-target_index)
        e = self.dq.popleft()
        self.dq.rotate(target_index)

        return e

    def popBack(self) -> int:
        if(len(self.dq) == 0):
            return -1
        
        return self.dq.pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()