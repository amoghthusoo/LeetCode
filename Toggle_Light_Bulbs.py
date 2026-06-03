class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        
        on_set = set()
        for bulb in bulbs:
            if(bulb not in on_set):
                on_set.add(bulb)
            else:
                on_set.remove(bulb)
        
        return sorted(list(on_set))