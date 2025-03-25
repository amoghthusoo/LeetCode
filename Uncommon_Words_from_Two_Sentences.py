class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]: 

        word_dict = {}

        for word in s1.split():
            if(word not in word_dict):
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        
        for word in s2.split():
            if(word not in word_dict):
                word_dict[word] = 1
            else:
                word_dict[word] += 1

        out_arr = []

        for key, value in word_dict.items():
            if(value == 1):
                out_arr.append(key)

        return out_arr
        