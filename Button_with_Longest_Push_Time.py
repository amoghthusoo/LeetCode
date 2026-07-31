class Solution:
    def buttonWithLongestTime(self, events: list[list[int]]) -> int:

        time_dict = {
            events[0][0] : events[0][1]
        }

        prev = events[0][1]
        i = 1
        while(i < len(events)):

            btn = events[i][0]
            time = events[i][1]
            diff = time - prev
            prev = time

            time_dict[btn] = max(time_dict.get(btn, 0), diff)
            i += 1

        intr_ans = []
        max_duration = max(time_dict.values())
        for btn, dur in time_dict.items():
            if(dur == max_duration):
                intr_ans.append(btn)

        return min(intr_ans)

events = [[1,2],[2,5],[3,9],[1,15]]
obj = Solution()
result = obj.buttonWithLongestTime(events)
print(result)