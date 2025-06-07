class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:

        count = 0

        i = 0
        while(i < len(colors)):
            
            x = (i - 1) % len(colors)
            y = i
            z = (i + 1) % len(colors)

            if(colors[x] == colors[z] and  colors[x] != colors[y]):
                count += 1

            i += 1

        return count


