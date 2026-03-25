class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:

        time = 0
        i = 0
        while(True):

            if(i != k):
                if(tickets[i] > 0):
                    tickets[i] -= 1
                    time += 1
            else:
                if(tickets[i] == 1):
                    time += 1
                    break
                else:
                    tickets[i] -= 1
                    time += 1

            i = (i + 1) % len(tickets)

        return time