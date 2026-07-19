class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        index_map = dict()
        for i, ch in enumerate(s):
            index_map[ch] = i
        
        seen = set()
        stack = []

        for i, ch in enumerate(s):

            if(not stack):
                stack.append(ch)
                seen.add(ch)

            elif(ch not in seen):

                while(stack and stack[-1] > ch and index_map[stack[-1]] > i):
                    seen.remove(stack.pop())
                
                stack.append(ch)
                seen.add(ch)
        
        return "".join(stack)