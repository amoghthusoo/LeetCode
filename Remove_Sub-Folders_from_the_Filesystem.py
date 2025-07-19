class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        
        folder.sort()
        
        ans = [folder[0]]
        
        curr_folder = folder[0].split("/")
        i = 1
        while(i < len(folder)):

            temp_folder = folder[i].split("/")

            j = 0
            while(j < len(curr_folder)):

                if(curr_folder[j] != temp_folder[j]):
                    ans.append(folder[i])
                    curr_folder = temp_folder
                    break
                
                j += 1
            
            i += 1

        return ans

folder = ["/a/b/c","/a/b/ca","/a/b/d"]
obj = Solution()
result = obj.removeSubfolders(folder)
print(result)
