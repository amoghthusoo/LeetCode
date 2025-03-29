class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []
        for num in nums:
            if(num >= 0):
                pos.append(num)
            else:
                neg.append(num)

        out = []
        for i in range(len(pos)):
            out.append(pos[i])
            out.append(neg[i])

        return out