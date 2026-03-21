from stack import Stack

# implementing queue using doudly linked list

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class LQueue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
        
    def enque(self,data):
        node = Node(data)
        if self.size > 1:
            node.prev = self.back
            self.back.next = node
            self.back = node
        elif self.size == 1:
            node.prev = self.front
            self.front.next = node
            self.back = node
        else:
            self.front = node
            self.back = node
        self.size += 1               
    
    def deque(self):
        if self.top:
            data = self.front.data
            self.front = self.front.next
            self.front.prev = None
            self.size -= 1
            return data
        return None
    
    
    # Implementing queues using stacks 
    
    
    class Squeue:
        def __init__(self):
            self.inbound = Stack()
            self.outbound = Stack()
            self.size = 0
            
        def enque(self,data):
            self.inbound.push(data)
            self.size += 1
            
            
            
        def deque(self):
            while self.inbound:
                self.outbound.push(self.inbound.pop())
            rev = self.outbound.pop()
            self.size -= 1
            return rev    
            
                
                     
            
                   