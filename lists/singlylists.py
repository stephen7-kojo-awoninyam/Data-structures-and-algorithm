class Node:
    def __init__(self,data):
        self.data = data 
        self.next = next
        
    def __str__(self):
        return str(self.data)    


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
         
    def append(self,data):
        node = Node(data)
        #if self.tail == None:
            #self.tail= node
        #else:
            #current = self.tail
            #while current.next:
                #current = current.next 
            #current = node 
        if self.tail:
            self.tail.next = node  
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1     
    def size(self):
        return self.size  
    
    
    def iter(self):
        
        current = self.head
        
        while current:
            value = current.data
            current = current.next
            yield value                              
    


    def delete(self,data):
        
        current = self.head
        previous = self.head
        
        while current:
            
            if current.data == data:
                
                if current == self.head:
                    
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1 
            previous = current
            current = current.next
            
    def search(self,data):
        for item in self.iter():
            if item == data:
               return True
        return False  
    
    
    def clear(self):
        self.head = None
        self.tail = None             
                        
        
        