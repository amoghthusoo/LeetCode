class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        
        out = []

        i = 1
        while(i < len(mountain) - 1):

            if(mountain[i - 1] < mountain[i] and mountain[i + 1] < mountain[i]):
                out.append(i)

            i += 1

        return out