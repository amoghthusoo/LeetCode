class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.stream = sorted(nums)
        self.k = k        

    def add(self, val: int) -> int:
        
        for i, e in enumerate(self.stream):
            if(e >= val):
                self.stream.insert(i, val) 
                break
        else:
            self.stream.append(val)

        return self.stream[-self.k]           


# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
param_1 = obj.add(3)
param_1 = obj.add(5)
param_1 = obj.add(10)
param_1 = obj.add(9)
param_1 = obj.add(4)