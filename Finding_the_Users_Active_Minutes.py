from collections import Counter

class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        
        inter_dict = dict()

        for log in logs:

            if(log[0] in inter_dict):
                inter_dict[log[0]].add(log[1])
            else:
                inter_dict[log[0]] = {log[1]}

        inter_arr = [len(val) for val in inter_dict.values()]
        occr_dict = dict(Counter(inter_arr))
    
        result_arr = [0 for _ in range(k)]

        for key, val in occr_dict.items():
            result_arr[key - 1] = val

        return result_arr

logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
solution = Solution()
result = solution.findingUsersActiveMinutes(logs, k)
print(result)