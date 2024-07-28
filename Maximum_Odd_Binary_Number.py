from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        occr_dict = dict(Counter(s))

        out_str = ""

        for _ in range(occr_dict["1"] - 1):
            out_str += "1"

        try:
            for _ in range(occr_dict["0"]):
                out_str += "0"
        except:
            pass

        out_str += "1"

        return out_str