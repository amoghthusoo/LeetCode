class Solution:
    def countMatches(self, items: list, ruleKey: str, ruleValue: str) -> int:
        
        mappingDict = { "type" : 0,
                        "color" : 1,
                        "name" : 2
                       }
        
        count = 0

        for l in items:

            if (l[mappingDict[ruleKey]] == ruleValue):
                count += 1

        return count


items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
obj = Solution()
solution = obj.countMatches(items, ruleKey, ruleValue)
print(solution)