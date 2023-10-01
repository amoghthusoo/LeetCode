from collections import Counter
class Solution:
    def validSquare(self, p1: list, p2: list, p3: list, p4: list) -> bool:

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
        
p1 = [0,0]
p2 = [1,1]
p3 = [0,0]
p4 = [1,1]
obj = Solution()
solution = obj.validSquare(p1, p2, p3, p4)
print(solution)