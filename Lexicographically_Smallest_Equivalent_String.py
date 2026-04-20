class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        groups : list[set] = []

        for i in range(len(s1)):
            groups.append({s1[i], s2[i]})

        flag = True
        while(flag):

            flag = False
            break_mem = False
            for i in range(len(groups)):
                for j in range(i + 1, len(groups)):

                    if(len(groups[i].intersection(groups[j])) != 0):
                        groups.append(groups[i].union(groups[j]))
                        groups.pop(i)
                        groups.pop(j - 1)
                        flag = True
                        break_mem = True
                        break
                
                if(break_mem):
                    break
        
        sub_dict = {}

        for group in groups:
            min_element = min(group)
            for e in group:
                sub_dict[e] = min_element
        
        ans = ""
        for e in baseStr:
            try:
                ans += sub_dict[e]
            except:
                ans += e
        
        return ans

s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
obj = Solution()
result = obj.smallestEquivalentString(s1, s2, baseStr)
print(result)
