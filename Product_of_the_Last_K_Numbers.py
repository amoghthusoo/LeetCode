class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.zero_index = None

    def add(self, num: int) -> None:
        
        if(len(self.arr) == 0 and num != 0):
            self.arr.append(num)
            
        elif(num == 0):
            self.arr.append(num)
            self.zero_index = len(self.arr) - 1
            i = 0
            while(i < len(self.arr)):
                self.arr[i] = 0
                i += 1
        else:
            
            if(self.arr[-1] != 0):
                self.arr.append(self.arr[-1] * num)
            else:
                self.arr.append(num)


    def getProduct(self, k: int) -> int:
        
        if(self.zero_index == None):
            
            if(k == len(self.arr)):
                return self.arr[-1]
            else:
                return self.arr[-1] // self.arr[-k - 1]
        else:

            negative_zero_index = self.zero_index - len(self.arr)

            if(-k > negative_zero_index + 1):
                return self.arr[-1] // self.arr[-k - 1]
            elif(-k == negative_zero_index + 1):
                return self.arr[-1]
            else:
                return 0

