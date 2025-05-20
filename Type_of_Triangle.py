class Solution:
    def triangleType(self, nums: list[int]) -> str:
        
        a = nums[0]
        b = nums[1]
        c = nums[2]

        if(a + b > c and b + c > a and a + c > b):
            pass
        else:
            return "none"
        
        if(a == b == c):
            return "equilateral"
        
        elif(
            (a == b and a != c) or
            (b == c and b != a) or
            (a == c and a != b)
        ):
            return "isosceles"
        
        else:
            return "scalene"