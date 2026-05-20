class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        occr_dict = {"L" : 0, "R" : 0, "_" : 0}

        for ch in moves:
            occr_dict[ch] += 1

        l_r_diff = abs(occr_dict["L"] - occr_dict["R"])
        case_1 = abs(l_r_diff + occr_dict["_"])
        case_2 = abs(l_r_diff - occr_dict["_"])
        return max(case_1, case_2)
