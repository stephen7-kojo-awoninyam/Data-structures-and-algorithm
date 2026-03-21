class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.parent = None
        self.tail = None
        
    def insert(self,value):
        node = Node(value)
        if self.parent == None:
            self.parent = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            

class HASHITEM:
    def __init__(self,key,value): 
        self.key = key
        self.value = value
        
class LRUCache:
    def __init__(self):
        self.size = 256
        self.slots =  DoublyLinkedList()
        for _ in range(self.size):
            self.slots.insert(None)
        self.count = 0 

    def _hash(self,key):
        mult = 1    
        hav = 0    
        for ch in key:
            hav += mult * ord(ch)
            mult += 1
        return hav % self.size
    
    def put(self,key,value):
        item = HASHITEM(key,value)   
        hash_no = self._hash(key)
        x = 0
        current = self.slots.parent
        while current:
            if x == hash_no:
                if current.value != None:
                    if current.value.key == key:
                        break
                    current = current.next
                    hash_no = (hash_no + 1) % self.size
                    x += 1
                else:
                    current.value = item
                    break 
            else:    
                current = current.next       
                x += 1    

            
    def get(self,key):
        hash_no = self._hash(key)
        x = 0
        size = 0
        current = self.slots.parent
        while current and size < self.size:
            if x == hash_no:
                if current.value:
                    if current.value.key == key:
                        return current.value.value
                current = current.next
                hash_no = (hash_no + 1) % self.size
                size += 1
                x += 1
            else:        
                current = current.next
                x += 1 
                size += 1
        return -1     
        

    
    
    def __setitem__(self, key, value):
        self.put(key,value)      
    
    def __getitem__(self, key):
        return self.get(key)
    

    
cache = LRUCache()

cache.put("Kojo", 1)
cache.put("Kwame", 2)

print(cache.get("Kojo"))      # returns 1

cache.put("Kofi", 3)   # evicts key 2

print(cache["Kweku"])      # returns -1

cache.put("Kweku", 4)   # evicts key 1

print(cache.get("Yaw"))      # returns -1
print(cache.get("Kofi"))      # returns 3
print(cache.get("Kweku"))      # returns 4    
    
                 
                   