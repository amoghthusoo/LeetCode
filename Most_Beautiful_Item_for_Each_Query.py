from sortedcontainers import SortedDict
from bisect import bisect
class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:

        max_dict = SortedDict()

        for item in items:
            price = item[0]
            beauty = item[1]

            max_dict[price] = max(max_dict.get(price, -1), beauty)

        cumm_max_dict = dict()
        _max = float("-inf")
        for price, beauty in max_dict.items():
            cumm_max_dict[price] = _max = max(_max, max_dict[price])

        prices = max_dict.keys()

        ans = []
        for query in queries:
            if(query in cumm_max_dict):
                ans.append(cumm_max_dict[query])
            else:
                left_bound_index = bisect(prices, query) - 1
                if(left_bound_index < 0):
                    ans.append(0)
                else:
                    _query = prices[left_bound_index]
                    ans.append(cumm_max_dict[_query])

        return ans


items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]
obj = Solution()
result = obj.maximumBeauty(items, queries)
print(result)