class Solution:
    def reverseByType(self, s: str) -> str:
        
        letter_indices = []
        letters = []

        special_indices = []
        special = []

        for i, e in enumerate(s):
            if(e.isalpha()):
                letter_indices.append(i)
                letters.append(e)
            
            else:
                special_indices.append(i)
                special.append(e)
        
        letters.reverse()
        special.reverse()

        intr_arr = [None for _ in range(len(s))]

        while(letter_indices):
            intr_arr[letter_indices.pop(0)] = letters.pop(0)
        
        while(special_indices):
            intr_arr[special_indices.pop(0)] = special.pop(0)
        
        return "".join(intr_arr)