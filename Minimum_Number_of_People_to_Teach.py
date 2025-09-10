class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:

        languages = [set(lang) for lang in languages]

        intr_friendships = []

        for friendship in friendships:

            p1 = friendship[0]
            p2 = friendship[1]

            if(not languages[p1 - 1].intersection(languages[p2 - 1])):
                intr_friendships.append(friendship)

        ans = 1000

        for lang in range(1, n + 1):
            
            person_set = set()
            for friendship in intr_friendships:

                p1 = friendship[0]
                p2 = friendship[1]

                if(lang not in languages[p1 - 1]):
                    person_set.add(p1)
                
                if(lang not in languages[p2 - 1]):
                    person_set.add(p2)

            if(len(person_set) < ans):
                ans = len(person_set)
        
        return ans
    
n = 2
languages = [[1],[2],[1,2]]
friendships = [[1,2],[1,3],[2,3]]

obj = Solution()
result = obj.minimumTeachings(n, languages, friendships)
print(result)