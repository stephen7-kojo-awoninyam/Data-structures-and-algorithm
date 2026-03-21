class Node:
    def __init__(self,data,next,prev):
        self.data = data 
        self.next = next
        self.prev = prev
class doublyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = None
     
    def append(self,data):
        node = Node(data,None,None)
        
        if self.head == None:
            self.head = node
            self.tail = node
            
        else:
            
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            
            self.count += 1
    def delete(self,data):
    
        
        if data == self.head.data:
            
            self.head.next = self.head
            
            self.head.prev = None
        elif data == self.tail.data:
            
            self.tail.prev = self.tail
            
            self.tail.next = None
        else:
            
            while self.head:
                
                if self.head.data == data:
                    self.head.prev.next = self.head.next
                    self.head.next.prev = self.head.next
                    return True
                self.head = self.head.next
                
                
                    
            
                    
           
            
            
            
        
        
        
            
        
        