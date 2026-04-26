from collections import deque

class Solution:

    def __init__(self):
        self.adj_list = dict()
        self.visisted = set()
    
    def construct_adj_list(self, adj_mat):
        
        for i in range(len(adj_mat)):
            for j in range(len(adj_mat[0])):

                if(i != j and adj_mat[i][j] == 1):
                    self.adj_list[i + 1].add(j + 1)
                    self.adj_list[j + 1].add(i + 1)

    def bfs(self, s):

        queue = deque([s])

        while(queue):

            popped = queue.popleft()
            self.visisted.add(popped)

            for node in self.adj_list[popped]:

                if(node not in self.visisted):
                    queue.append(node)
                    self.visisted.add(node)
    

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        
        for i in range(1, len(isConnected) + 1):
            self.adj_list[i] = set()
        self.construct_adj_list(isConnected)

        components = 0
        for i in range(1, len(isConnected) + 1):
            if(i not in self.visisted):
                self.bfs(i)
                components += 1

        return components        

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
obj = Solution()
result = obj.findCircleNum(isConnected)
print(result)