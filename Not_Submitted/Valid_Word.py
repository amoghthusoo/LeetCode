class Solution:
    def isValid(self, word: str) -> bool:
        
        if(len(word) < 3):
            return False
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        consonants = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        consonants.remove('a')
        consonants.remove('e')
        consonants.remove('i')
        consonants.remove('o')
        consonants.remove('u')
        
        consonants.remove('A')
        consonants.remove('E')
        consonants.remove('I')
        consonants.remove('O')
        consonants.remove('U')
        
        vowel_mem = False
        consonant_mem = False

        i = 0
        while(i < len(word)):

            if(word[i] in vowels):
                vowel_mem = True
            
            if(word[i] in consonants):
                consonant_mem = True
            
            if(not word[i].isalnum()):
                return False

            i += 1

        
        if(vowel_mem and consonant_mem):
            return True
        else:
            return False