class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        
        prefixes = set()
        con = ""
        for word in words:
            con += word
            prefixes.add(con)
        
        if(s in prefixes):
            return True
        
        return False