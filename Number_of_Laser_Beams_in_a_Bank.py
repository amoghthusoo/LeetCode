class Solution:
    def numberOfBeams(self, bank: list) -> int:

        interList = []

        for element in bank:

            if (element.count('1') != 0):
                interList.append(element.count('1'))

        beamCount = 0

        if (len(interList) == 1):
            return beamCount
        else:

            i = 0
            while (i < len(interList) - 1):

                beamCount += interList[i] * interList[i + 1]
                i += 1

        return beamCount




bank = ["111000", "000001", "110000", "110000"]
obj = Solution()
solution = obj.numberOfBeams(bank)
print(solution)