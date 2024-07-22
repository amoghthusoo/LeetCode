class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        
        out_arr = [first]

        for e in encoded:
            out_arr.append(e ^ out_arr[-1])

        return out_arr