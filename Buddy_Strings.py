from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if(len(s) != len(goal)):
            return False
        
        freq_dict = Counter(s)
        if(s == goal):

            for key, freq in freq_dict.items():
                if(freq >= 2):
                    return True
            
            return False
        

        freq_dict_goal = Counter(goal)

        if(freq_dict != freq_dict_goal):
            return False
        
        cnt = 0
        for i in range(len(s)):
            if(s[i] != goal[i]):
                cnt += 1

            if(cnt > 2):
                return False
            
        return True

