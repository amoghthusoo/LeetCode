class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        
        seats.sort()
        students.sort()

        total = 0

        i = 0
        while(i < len(seats)):
            
            total += abs(seats[i] - students[i])
            
            i += 1

        return total
