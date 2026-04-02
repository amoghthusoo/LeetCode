from sortedcontainers import SortedDict

class LFUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.ref_string = {}
        self.key_value = {}
        self.key_count = {}
        self.count_key = SortedDict()

    def get(self, key: int) -> int:
        
        if(key in self.key_value):

            self.ref_string.pop(key)
            self.ref_string[key] = None
            
            self.key_count[key] += 1

            new_freq = self.key_count[key]
            old_freq = new_freq - 1

            if(new_freq not in self.count_key):
                self.count_key[new_freq] = {key}
            else:
                self.count_key[new_freq].add(key)

            self.count_key[old_freq].remove(key)
            if(len(self.count_key[old_freq]) == 0):
                self.count_key.pop(old_freq)
            
            return self.key_value[key]
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        
        if(key in self.key_value):

            self.ref_string.pop(key)
            self.ref_string[key] = None
            
            self.key_value[key] = value

            self.key_count[key] += 1
            new_freq = self.key_count[key]
            old_freq = new_freq - 1 

            if(new_freq not in self.count_key):
                self.count_key[new_freq] = {key}
            else:
                self.count_key[new_freq].add(key)

            self.count_key[old_freq].remove(key)
            if(len(self.count_key[old_freq]) == 0):
                self.count_key.pop(old_freq)

        else:

            if(len(self.key_value) == self.capacity):
                
                deletion_keys = self.count_key[next(iter(self.count_key))]

                if(len(deletion_keys) == 1):
                    target_key = next(iter(deletion_keys))
                
                else:
                    it = iter(self.ref_string)
                    while(True):

                        k = next(it)
                        if(k in deletion_keys):
                            target_key = k
                            break

                self.ref_string.pop(target_key)
                self.key_value.pop(target_key)
                self.count_key[next(iter(self.count_key))].remove(target_key)
                
                
            
            self.ref_string[key] = None
            self.key_value[key] = value
            self.key_count[key] = 1

            if(1 not in self.count_key):
                self.count_key[1] = {key}
            else:
                self.count_key[1].add(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)