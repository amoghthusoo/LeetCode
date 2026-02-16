class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        
        cities = set()

        for path in paths:
            cities.add(path[0])
            cities.add(path[1])

        for path in paths:
            cities.remove(path[0])

        return cities.pop()