class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        
        players.sort()
        trainers.sort()
        count = 0

        i = 0
        j = 0
        while(i < len(players) and j < len(trainers)):

            while(j < len(trainers) and trainers[j] < players[i]):
                j += 1
            
            if(j < len(trainers)):
                i += 1
                j += 1
                count += 1

        return count

players = [1,1,1]
trainers = [10]
obj = Solution()
result = obj.matchPlayersAndTrainers(players, trainers)
print(result)
