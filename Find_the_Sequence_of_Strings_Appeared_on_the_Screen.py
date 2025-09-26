class Solution:
    
    def stringSequence(self, target: str) -> list[str]:
        
        result = []
        prefix = ""

        i = 0
        while(i < len(target)):
            
            _ascii = 97
            while(chr(_ascii) != target[i]):
                result.append(prefix + chr(_ascii))
                _ascii += 1

            result.append(prefix + chr(_ascii))
            prefix += chr(_ascii)
            
            i += 1

        return result

target = "he"
solution = Solution()
result = solution.stringSequence(target)
print(result)