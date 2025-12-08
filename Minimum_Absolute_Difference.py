from sortedcontainers import SortedDict
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        
        intr_dict = SortedDict()

        arr.sort()
        i = 1
        while(i < len(arr)):

            diff = arr[i] - arr[i - 1]

            if(diff not in intr_dict):
                intr_dict[diff] = [[arr[i - 1], arr[i]]]
            else:
                intr_dict[diff].append([arr[i - 1], arr[i]])

            i += 1
        
        return intr_dict.peekitem(0)[1]


arr = [4,2,1,3]
obj = Solution()
result = obj.minimumAbsDifference(arr)
print(result)
