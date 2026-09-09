from collections import Counter
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        if (
                (p1 == p2) or
                (p2 == p3) or
                (p3 == p4) or
                (p1 == p3) or
                (p2 == p4) or
                (p1 == p4)
        ):
            return False
        
        else:
            
            def distanceFormula(P, Q):
                return (((Q[0] - P[0]) ** 2) + ((Q[1] - P[1]) ** 2)) ** 0.5

            lenList : list = []
            lenList.append(distanceFormula(p1, p2))
            lenList.append(distanceFormula(p2, p3))
            lenList.append(distanceFormula(p3, p4))
            lenList.append(distanceFormula(p1, p3))
            lenList.append(distanceFormula(p2, p4))
            lenList.append(distanceFormula(p1, p4))

            occDict : dict = Counter(lenList)
            occList : list = list(occDict.values())

            if ((2 in occList) and (4 in occList)):
                return True
            else:
                return False