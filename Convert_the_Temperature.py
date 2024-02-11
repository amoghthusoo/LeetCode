class Solution:
    def convertTemperature(self, celsius: float) -> list:

        return [celsius + 273.15, celsius * 1.80 + 32]

celsius = 122.11
obj = Solution()
solution = obj.convertTemperature(celsius)
print(solution)