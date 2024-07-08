class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        
        time_dict = {}

        time_dict[logs[0][0]] = logs[0][1]

        i = 1
        while(i < len(logs)):

            if(logs[i][0] not in time_dict):
                time_dict[logs[i][0]] = logs[i][1] - logs[i - 1][1]
            else:

                if(logs[i][1] - logs[i - 1][1] > time_dict[logs[i][0]]):
                    time_dict[logs[i][0]] = logs[i][1] - logs[i - 1][1]

            i += 1

        max_time = max(time_dict.values())

        possible_solutions = []

        for key, value in time_dict.items():
            if(value == max_time):
                possible_solutions.append(key)

        possible_solutions.sort()

        return possible_solutions[0]
    
n = 10
logs = logs = [[0,10],[1,20]]
obj = Solution()
out = obj.hardestWorker(n, logs)
print(out)