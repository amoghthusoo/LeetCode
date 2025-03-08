class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        
        index_dict = {}

        i = 0
        while(i < len(s)):
            
            if(s[i] not in index_dict):
                index_dict[s[i]] = [i]
            else:
                index_dict[s[i]].append(i)
            
            i += 1

        for key, value in index_dict.items():

            if(distance[ord(key) - 97] != value[1] - value[0] - 1):
                return False

        return True

s = "aa"
distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
obj = Solution()
out = obj.checkDistances(s, distance)
print(out)