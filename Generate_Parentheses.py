class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        def generate(arr, i, open_cnt, close_cnt, result):
    
            if(i == len(arr)):
                result.append("".join(arr))
                return
            
            if(open_cnt < len(arr)//2):
                arr[i] = "("
                generate(arr, i + 1, open_cnt + 1, close_cnt, result)
            
            if(open_cnt > close_cnt):
                arr[i] = ")"
                generate(arr, i + 1, open_cnt, close_cnt + 1, result)
        

        arr = [None] * (n * 2)
        result = []
        generate(arr, 0, 0, 0, result)  
        return result