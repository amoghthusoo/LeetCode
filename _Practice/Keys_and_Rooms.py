class Solution:
    def __init__(self):
        self.adj_list = None
        self.visited = set()

    def bfs(self, s):

        queue = deque([s])

        while(queue):

            popped = queue.popleft()

            for node in self.adj_list[popped]:

                if(node not in self.visited):
                    queue.append(node)
                    self.visited.add(node)

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        self.adj_list = rooms

        components = 0
        for i in range(len(rooms)):
            if(i not in self.visited):
                self.bfs(i)
                components += 1
        
        if(components == 1):
            return True
        else:
            return False
        