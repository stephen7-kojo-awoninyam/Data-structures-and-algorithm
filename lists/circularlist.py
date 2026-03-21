class Node:
    def __init__(self,data):
        self.data = data 
        self.next = next



class CircularList:
    def __init__(self,head = None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0
    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        elif self.head:
            self.head.next = node
            self.tail = node
            self.tail.next = self.head    
        else:
            self.tail.next = node
            
            self.tail = node 
            
            self.tail.next = self.head 
        self.size += 1
    def size(self):
        return self.size
    
    
    def delete(self,data):
          
        current = self.head
        prev = self.head   
        while prev == current or prev != self.tail:
            
            if current.data == data:
                current = current.next
                self.tail.next = current
                return True
            
            elif current.data == data:
                prev.next = current.next
                return True
            
            self.size -= 1
            
            current = current.next  
            prev = current
        return False    
            
            
            
                          
               
    