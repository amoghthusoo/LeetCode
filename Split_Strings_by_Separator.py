class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        
        interList = []
        for element in words:
            interList += element.split(sep = separator)

        while ("" in interList):
            interList.pop(interList.index(""))

        return interList

words = ["one.two.three","four.five","six"]
separator = "."
obj = Solution()
solution = obj.splitWordsBySeparator(words, separator)
print(solution)