class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        
        asteroids.sort()
        for weight in asteroids:
            if(weight <= mass):
                mass += weight
            else:
                return False
        return True