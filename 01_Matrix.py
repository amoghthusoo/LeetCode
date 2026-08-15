from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:

        visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
        distance = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(mat[i][j] == 0):
                    queue.append([i, j, 0])
                    visited[i][j] = True

        while(queue):

            i, j, d = queue.popleft()
            distance[i][j] = d
            for x, y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_i, new_j = i + x, j + y
                if(new_i < 0 or new_i >= len(mat) or new_j < 0 or new_j >= len(mat[0])):
                    continue

                if(visited[new_i][new_j]):
                    continue

                queue.append([new_i, new_j, d + 1])
                visited[new_i][new_j] = True

        return distance

mat = [[0],[0],[0],[0],[0]]
obj = Solution()
result = obj.updateMatrix(mat)
print(result)
