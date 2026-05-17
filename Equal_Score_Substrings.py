class Solution:
    def scoreBalance(self, s: str) -> bool:
        
        intr_arr = []

        for e in s:
            intr_arr.append(ord(e) - 96)

        for i in range(1, len(intr_arr)):
            intr_arr[i] += intr_arr[i - 1]
        
        for i in range(len(intr_arr) - 1):
            
            if(intr_arr[i] == intr_arr[-1] - intr_arr[i]):
                return True
            
        return False

