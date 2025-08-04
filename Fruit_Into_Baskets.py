class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        
        freq_dict = dict()
        ans = -1

        i = j = 0
        while(j < len(fruits)):

            if(fruits[j] not in freq_dict):
                freq_dict[fruits[j]] = 1
            else:
                freq_dict[fruits[j]] += 1
            j += 1
            
            if(len(freq_dict) > 2):
                
                if((j - i) > ans):
                    ans = j - i - 1

                while(len(freq_dict) > 2):

                    if(fruits[i] in freq_dict):

                        freq_dict[fruits[i]] -= 1
                        if(freq_dict[fruits[i]] == 0):
                            freq_dict.pop(fruits[i])
                    i += 1
                

        if((j - i) > ans):
            ans = j - i

        return ans

fruits = [1,2,3,2,2]
obj = Solution()
result = obj.totalFruit(fruits)
print(result)