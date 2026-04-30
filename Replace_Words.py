class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:

        ans = ""
    
        temp = ""
        i = 0
        while(i < len(sentence)):

            if(sentence[i] != " "):
                temp += sentence[i]
            else:
                poss_roots = []

                for root in dictionary:
                    if(temp.find(root) == 0):
                        poss_roots.append(root)

                if(len(poss_roots) == 0):
                    ans += temp
                elif(len(poss_roots) == 1):
                    ans += poss_roots[0]
                else:
                    min_len = poss_roots[0]
                    j = 1
                    while(j < len(poss_roots)):

                        if(len(poss_roots[j]) < len(min_len)):
                            min_len = poss_roots[j]

                        j += 1
                    
                    ans += min_len
                
                ans += " "
                temp = ""

            i += 1
        
        poss_roots = []

        for root in dictionary:
            if(temp.find(root) == 0):
                poss_roots.append(root)

        if(len(poss_roots) == 0):
            ans += temp
        elif(len(poss_roots) == 1):
            ans += poss_roots[0]
        else:
            min_len = poss_roots[0]
            j = 1
            while(j < len(poss_roots)):

                if(len(poss_roots[j]) < len(min_len)):
                    min_len = poss_roots[j]

                j += 1
            
            ans += min_len
        
        temp = ""

        return ans  

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
obj = Solution()
result = obj.replaceWords(dictionary, sentence)
print(result)      