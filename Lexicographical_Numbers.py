class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        
        intr_arr = []
        for i in range(1, n + 1):
            intr_arr.append(str(i))

        intr_arr.sort()

        for i, e in enumerate(intr_arr):
            intr_arr[i] = int(e)
        
        return intr_arr