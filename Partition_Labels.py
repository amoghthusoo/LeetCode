class Solution:
    def partitionLabels(self, s):
        
        last_index_dict = {}
        for i, ch in enumerate(s):
            last_index_dict[ch] = i

        go_till = last_index_dict[s[0]]
        inter_result = [-1]
        i = 0
        while(i < len(s)):
        
            temp_go_till = last_index_dict[s[i]]

            if(temp_go_till > go_till):
                go_till = temp_go_till

            if(go_till == len(s) - 1):
                inter_result.append(go_till)
                break
            
            if(i == go_till):
                inter_result.append(i)

            i += 1

        return [inter_result[i + 1] - inter_result[i] for i in range(len(inter_result) - 1)]   


s = "caedbdedda"
obj = Solution()
result = obj.partitionLabels(s)
print(result)