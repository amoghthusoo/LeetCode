from collections import deque
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:

        students = deque(students)
        sandwiches = deque(sandwiches)

        while(students):

            if(students[0] == sandwiches[0]):
                students.popleft()
                sandwiches.popleft()
            
            else:
                students.append(students.popleft())

            try:
                if((sandwiches[0] == 0 and sum(students) == len(students)) or ((sandwiches[0] == 1 and sum(students) == 0))):
                    return len(students)
            except:
                pass

        return 0
    
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
obj = Solution()
result = obj.countStudents(students, sandwiches)
print(result)
