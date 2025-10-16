from sortedcontainers import SortedList
class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        
        for i, response in enumerate(responses):
            responses[i] = set(response)

        occr_dict = dict()

        for response in responses:
            for e in response:
                if(e not in occr_dict):
                    occr_dict[e] = 1
                else:
                    occr_dict[e] += 1

        max_freq = max(occr_dict.values())

        intr_list = SortedList()

        for key, val in occr_dict.items():

            if(val == max_freq):
                intr_list.add(key)

        return intr_list[0]

responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]
obj = Solution()
result = obj.findCommonResponse(responses)
print(result)
