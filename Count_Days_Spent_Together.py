class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        cumm_sum = []
        _total = 0
        for e in months:
            _total += e
            cumm_sum.append(_total)

        a = cumm_sum[int(arriveAlice[0:2]) - 1] + int(arriveAlice[3:])
        b = cumm_sum[int(leaveAlice[0:2]) - 1] + int(leaveAlice[3:])
        c = cumm_sum[int(arriveBob[0:2]) - 1] + int(arriveBob[3:])
        d = cumm_sum[int(leaveBob[0:2]) - 1] + int(leaveBob[3:])

        set_1 = set([i for i in range(a, b + 1)])
        set_2 = set([i for i in range(c, d + 1)])
        return len(set_1.intersection(set_2))



arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
obj = Solution()
result = obj.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
print(result)