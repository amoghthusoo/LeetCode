class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        k = 1
        substr = word

        while(True):

            if(substr in sequence):
                k += 1
                substr = word * k
            else:
                return k - 1
            

sequence = "ababc"
word = "ac"
obj = Solution()
result = obj.maxRepeating(sequence, word)
print(result)

        