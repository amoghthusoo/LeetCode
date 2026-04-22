class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.ref_string = {}        
        self.capacity = capacity

    def get(self, key: int) -> int:
        
        if(key in self.cache):
            self.ref_string.pop(key)
            self.ref_string[key] = None
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        
        if(key in self.cache):
            self.cache[key] = value
            self.ref_string.pop(key)
            self.ref_string[key] = None
        
        else:
            
            
            if(len(self.cache) == self.capacity):
                target_key = next(iter(self.ref_string))
                self.ref_string.pop(target_key)
                self.cache.pop(target_key)

            self.cache[key] = value
            self.ref_string[key] = None
