from sortedcontainers import SortedSet

class Trie:

    def __init__(self):
        self.set = SortedSet()        

    def insert(self, word: str) -> None:
        self.set.add(word)

    def search(self, word: str) -> bool:
        
        if(word in self.set):
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        
        index = self.set.bisect_left(prefix)

        try:
            if(index == len(self.set)):
                return False
            elif(self.set[index].index(prefix) == 0):
                return True
            else:
                return False
        except:
            return False


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_2 = obj.search("app")
param_3 = obj.startsWith("app")