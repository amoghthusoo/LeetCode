class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split()

        if(len(pattern) != len(s)):
            return False

        map_dict = {}

        i = 0
        while(i < len(pattern)):

            if(pattern[i] not in map_dict):

                if(s[i] in map_dict.values()):
                    return False
                else:
                    map_dict[pattern[i]] = s[i]
            
            else:

                if(s[i] != map_dict[pattern[i]]):
                    return False

            i += 1

        return True    
        