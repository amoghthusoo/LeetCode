from sortedcontainers import SortedDict

class Solution:
    def smallestPalindrome(self, s: str) -> str:

        occr_dict = SortedDict()
        for ch in s:
            occr_dict[ch] = occr_dict.get(ch, 0) + 1

        odd_length_ch = None
        if(len(s) % 2 != 0):

            for ch, freq in occr_dict.items():
                if(freq % 2 != 0):
                    odd_length_ch = ch
                    break

            occr_dict[odd_length_ch] -= 1

        part1 = ""
        for ch, freq in occr_dict.items():
            part1 += ch * (freq // 2)

        part1_rev = part1[-1::-1]

        if(odd_length_ch == None):
            return part1 + part1_rev
        else:
            return part1 + odd_length_ch + part1_rev
        