class Solution:
    def deckRevealedIncreasing(self, deck):
        
        deck.sort()
        result = [None for _ in range(len(deck))]

        skip = False
        i = 0
        while(deck):
            
            if(result[i] == None and not skip):
                result[i] = deck.pop(0)
                skip = True
            
            elif(result[i] == None and skip):
                skip = False

            i = (i + 1) % len(result)

        return result

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
obj = Solution()
result = obj.deckRevealedIncreasing(deck)
print(result)