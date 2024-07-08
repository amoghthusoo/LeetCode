class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_split = sentence.split()

        if(sentence_split[-1][-1] != sentence_split[0][0]):
            return False

        
        i = 0
        while(i < len(sentence_split) - 1):

            if(sentence_split[i][-1] != sentence_split[i + 1][0]):
                return False

            i += 1

        return True