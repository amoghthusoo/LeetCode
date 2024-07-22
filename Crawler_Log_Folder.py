class Solution:
    def minOperations(self, logs: list[str]) -> int:
        
        distance = 0

        for op in logs:

            if(op == "../"):

                if(distance != 0):
                    distance -= 1

            elif(op == "./"):
                pass

            else:
                distance += 1

        if(distance < 0):
            return 0
        else:
            return distance

logs = ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]
obj = Solution()
out = obj.minOperations(logs)
print(out)