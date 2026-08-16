from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def bfs(board, i, j, visited, temp : set):

            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            region_open = False

            while(queue):

                i, j = queue.popleft()
                temp.add((i, j))

                for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    new_i, new_j = i + x, j + y

                    if(new_i < 0 or new_i >= len(board) or new_j < 0 or new_j >= len(board[0])):
                        region_open = True
                        continue

                    if(board[new_i][new_j] == "X" or visited[new_i][new_j]):
                        continue

                    queue.append((new_i, new_j))
                    visited[new_i][new_j] = True

            if(region_open):
                temp.clear()

        rows = len(board)
        cols = len(board[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        temp = set()

        for i in range(rows):
            for j in range(cols):

                if(board[i][j] == "O" and not visited[i][j]):
                    bfs(board, i, j, visited, temp)
                    for x, y in temp:
                        board[x][y] = "X"
                    temp.clear()

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
obj = Solution()
result = obj.solve(board)
print(board)

                    
