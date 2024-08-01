class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.history = [homepage]


    def visit(self, url: str) -> None:
        del(self.history[self.i + 1 : ])
        self.history.append(url)
        self.i += 1        

    def back(self, steps: int) -> str:
        
        if(self.i - steps < 0):
            self.i = 0
        else:
            self.i -= steps
        
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        
        if(self.i + steps >= len(self.history)):
            self.i = len(self.history) - 1
        else:
            self.i += steps

        return self.history[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)