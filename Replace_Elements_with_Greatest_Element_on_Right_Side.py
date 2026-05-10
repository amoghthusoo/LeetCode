class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:

        out = []
        _max = arr[-1]

        if(len(arr) != 1):
            out.append(_max)

        i = len(arr) - 2
        while(i >0):
            if(arr[i] > _max):
                _max = arr[i]

            out.insert(0, _max)

            i -= 1

        
        out.append(-1)

        return out

arr = [17]
obj = Solution()
out = obj.replaceElements(arr)
print(out)