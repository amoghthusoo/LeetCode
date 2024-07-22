class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        
        group_dict = {}
        unique_int = 0

        i = 0
        while(i < len(groupSizes)):
            
            if(groupSizes[i] not in group_dict):
                group_dict[groupSizes[i]] = [i]
            
            else:

                if(len(group_dict[groupSizes[i]]) == groupSizes[i]):
                    
                    group_dict[str(groupSizes[i]) + str(unique_int)] = group_dict[groupSizes[i]]
                    unique_int += 1

                    group_dict[groupSizes[i]] = [i]

                else:

                    group_dict[groupSizes[i]].append(i)

            i += 1

        return list(group_dict.values())

groupSizes = [3,3,3,3,3,1,3]
obj = Solution()
out = obj.groupThePeople(groupSizes)
# print(out)       