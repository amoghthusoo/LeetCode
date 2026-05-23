from collections import Counter
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        
        occr_dict = Counter(s)
        group_dict = dict()

        for ch, freq in occr_dict.items():

            if(freq not in group_dict):
                group_dict[freq] = [ch]
            else:
                group_dict[freq].append(ch)
        
        max_group_size = 0
        for freq, group in group_dict.items():
            if(len(group) > max_group_size):
                max_group_size = len(group)
        
        possible_ans = []

        for freq, group in group_dict.items():

            if(len(group) == max_group_size):
                possible_ans.append([freq, group])

        possible_ans.sort(reverse = True)

        return "".join(possible_ans[0][1])

s = "pfpfgi"
obj = Solution()
result = obj.majorityFrequencyGroup(s)
print(result)