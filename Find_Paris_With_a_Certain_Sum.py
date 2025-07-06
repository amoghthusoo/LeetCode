from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2    
        self.nums2_freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        
        old_val = self.nums2[index]
        new_val = self.nums2[index] + val

        self.nums2_freq[old_val] -= 1

        if(new_val not in self.nums2_freq):
            self.nums2_freq[new_val] = 1
        else:
            self.nums2_freq[new_val] += 1
        
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        
        cnt = 0
        for e in self.nums1:
            target = tot - e
            if((target) in self.nums2_freq):
                cnt += self.nums2_freq[target]

        return cnt 


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
