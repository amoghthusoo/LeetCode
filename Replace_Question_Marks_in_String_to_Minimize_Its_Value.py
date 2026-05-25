from sortedcontainers import SortedList
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        occr_map = dict()
        for i in range(97, 123):
            occr_map[chr(i)] = 0
        
        q_count = 0
        for ch in s:
            if(ch != "?"):
                occr_map[ch] += 1
            else:
                q_count += 1
        
        replace_list = SortedList()
        for _ in range(q_count):
            min_ch = None
            min_occr = float("inf")
            for ch, occr in occr_map.items():
                if(occr < min_occr):
                    min_occr = occr
                    min_ch = ch
            
            replace_list.add(min_ch)
            occr_map[min_ch] += 1
        
        i = 0
        ans = ""
        for ch in s:
            if(ch != "?"):
                ans += ch
            else:
                ans += replace_list[i]
                i += 1

        return ans

s = "???"
obj = Solution()
result = obj.minimizeStringValue(s)
print(result)