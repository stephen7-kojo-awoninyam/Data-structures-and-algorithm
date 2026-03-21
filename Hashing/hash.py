
class Hash_item:
    def __init__(self,key, value):
        self.value = value
        self.key = key
        
class Hash_Table:
    def __init__(self):
        self.size = 256
        self.space = [None for i in range(self.size)]
        self.count = 0
        
    def _hash(self,key):
        mult = 1
        hav = 0
        for ch in key:
            hav += mult*ord(ch)
            mult += 1 
        return hav % self.size
    
    def put(self, key,value):
        item = Hash_item(key,value)
        hash_no = self._hash(key)
        while self.space[hash_no] != None:
            if self.space[hash_no].key == key:
                break
            hash_no = (hash_no + 1) % self.size
        if self.space[hash_no] == None:
            self.space[hash_no] = item
            self.count += 1    
            
      
    def get(self, key):
        hash_no = self._hash(key)
        while self.space[hash_no] != None:
            if self.space[hash_no].key == key:
                return self.space[hash_no].value
            hash_no = (hash_no + 1) % self.size
        return None
    def Load_factor(self):
        lf = self.count / self.size
        if lf >= 0.75:
            self.size *= 2
            
     
    def __setitem__(self, key, value):
        self.put(key,value) 
    def __getitem__(self, key):
        return self.get(key)      
        
        


ht = Hash_Table()
ht["good"] = "eggs"
ht["better"] = "ham"
ht["best"] = "spam"
ht["ad"] = "do not"
ht["ga"] = "collide"
    
for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht.get(key)
    print(v)  
print(f"The number of element is {ht.count}")                