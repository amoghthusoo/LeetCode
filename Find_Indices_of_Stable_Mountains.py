class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        indices = []

        i = 1
        while(i < len(height)):

            if(height[i - 1] > threshold):
                indices.append(i)
            i += 1

        return indices