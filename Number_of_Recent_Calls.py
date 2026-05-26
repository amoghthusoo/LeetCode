class RecentCounter:

    def __init__(self):
        self.ds = []
        

    def ping(self, t: int) -> int:
        
        self.ds.append(t)

        cnt = 0
        i = len(self.ds) - 1
        while(i >= 0 and self.ds[i] >= t - 3000):

            cnt += 1

            i -= 1

        return cnt

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)