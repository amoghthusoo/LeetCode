class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split(".")
        version2 = version2.split(".")
        

        if(len(version1) <= len(version2)):
            shorter = version1
            longer = version2
        else:
            shorter = version2
            longer = version1

        shorter.extend(["0" for _ in range(len(longer) - len(shorter))])
        
        for i in range(len(shorter)):

            if(len(shorter[i]) <= len(longer[i])):
                shorter[i] = shorter[i].zfill(len(longer[i]))
            else:
                longer[i] = longer[i].zfill(len(shorter[i]))


        i = 0
        while(i < len(version1)):

            if(version1[i] < version2[i]):
                return -1
            elif(version1[i] > version2[i]):
                return 1

            i += 1        

        return 0

version1 = "1.0.1"
version2 = "1"
obj = Solution()
result = obj.compareVersion(version1, version2)
print(result)
