class Solution:
    def closestDivisors(self, num: int) -> list[int]:

        def get_divisors(n):

            divisors = []
            i = 1
            while(i <= int(n ** 0.5)):

                if(n % i == 0):
                    divisors.append(i)
                i += 1

            return divisors


        d1 = get_divisors(num + 1)
        d2 = get_divisors(num + 2)

        diff = float("inf")
        ans = None
        for div1 in d1:

            div2 = (num + 1) // div1
            curr_diff = abs(div1 - div2)
            if(curr_diff < diff):
                ans = [div1, div2]
                diff = curr_diff

        for div1 in d2:

            div2 = (num + 2) // div1
            curr_diff = abs(div1 - div2)
            if(curr_diff < diff):
                ans = [div1, div2]
                diff = curr_diff

        return ans

num = 8
obj = Solution()
result = obj.closestDivisors(num)
print(result)
