from collections import Counter
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        
        key = list(dict(Counter(key)).keys())
        try:
            key.pop(key.index(" "))
        except:
            pass

        alphabets = [chr(i) for i in range(97, 123)]
        
        encryptionDict = dict(zip(key, alphabets))
        encryptionDict[" "] = " "

        outStr = ""
        for ch in message:
            outStr += encryptionDict[ch]

        return outStr
        

key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
obj = Solution()
solution = obj.decodeMessage(key, message)
print(solution)