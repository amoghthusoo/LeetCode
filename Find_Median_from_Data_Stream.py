from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.sl = SortedList()        

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        
        if(len(self.sl) % 2 == 0):
            return (self.sl[len(self.sl) // 2] + self.sl[len(self.sl) // 2 - 1]) / 2
        else:
            return self.sl[len(self.sl) // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()