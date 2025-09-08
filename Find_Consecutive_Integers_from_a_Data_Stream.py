from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.occr_dict = dict()
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        
        if(len(self.stream) < self.k):
            self.stream.append(num)

            if(num not in self.occr_dict):
                self.occr_dict[num] = 1
            else:
                self.occr_dict[num] += 1

        else:
            popped = self.stream.popleft()
            self.stream.append(num)

            self.occr_dict[popped] -= 1
            if(self.occr_dict[popped] == 0):
                self.occr_dict.pop(popped)
            
            if(num not in self.occr_dict):
                self.occr_dict[num] = 1
            else:
                self.occr_dict[num] += 1

        if(len(self.stream) < self.k):
            return False

        else:
            if(len(self.occr_dict) == 1 and self.value in self.occr_dict and self.occr_dict[self.value] == self.k):
                return True
            else:
                return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)