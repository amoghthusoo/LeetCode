class MagicDictionary:

    def __init__(self):
        self.arr = None

    def buildDict(self, dictionary: list[str]) -> None:
        self.arr = dictionary
        
    def search(self, searchWord: str) -> bool:

        for word in self.arr:

            diff_count = 0
            if(len(word) == len(searchWord)):

                i = 0
                while(i < len(searchWord)):

                    if(word[i] != searchWord[i]):
                        diff_count += 1

                    if(diff_count > 1):
                        break
                    
                    i += 1
        
            if(diff_count == 1):
                return True
        
        return False

# Your MagicDictionary object will be instantiated and called as such:
dictionary = ["hello","hallo","leetcode","judge"]
obj = MagicDictionary()
obj.buildDict(dictionary)
param_2 = obj.search("juage")
print(param_2)
