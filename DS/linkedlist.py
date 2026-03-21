

class Node:
    data=None
    next_node=None
    
    def __init__(self,data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s>" %self.data   
    
class Linkedlist:
    
    def __init__(self):
        self.head = None
        
    def Is_empty():
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node
        return count  
    
    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
         
    def insert(self,data,index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node()
            
            current = self.head
            position = index
            
            while position > 1:
                current = current.next_node
                position -= 1
                        
            prev_node = current
            next_node = prev_node.next_node
            
            prev_node.next_node = new
            new.next_node = next_node
        
                
        
        