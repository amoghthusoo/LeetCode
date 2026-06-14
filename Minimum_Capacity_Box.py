class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        
        supp_result = float("inf")
        idx = -1

        for i in range(len(capacity)):

            diff = capacity[i] - itemSize
            if(diff >= 0 and diff < supp_result):
                supp_result = diff
                idx = i
        
        return idx

    