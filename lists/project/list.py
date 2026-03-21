class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.child = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self,data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def __str__(self):
        value = []
        current = self.head
        while current:
            value.append(str(current.data))
            current = current.next
        return "->".join(value)
     
    
class FlattenedList:
    def __init__(self,list1,list2):
        self.main = list1
        self.child = list2
        self.combine = None
        self.flat = []
    def joined(self):
        self.main.head.child = self.child.head
        return self.main  
    
    def flattenedsortedList(self):
        parent = []
        def flattened(node):    
            while node:
                parent.append(node.data)
                if node.child:
                   flattened(node.child)
                node = node.next        
        flattened(self.main.head) 
        parent.sort()       
        
        return "->".join(str(x) for x in parent)
              
   
    
        
    def __str__(self):
        print(type(self.flat))
        return "->".join(self.flat)         
    
# Linked list one 

list1 = LinkedList()  
list1.append(5)
list1.append(6)    
list1.append(7)    
list1.append(30) 
  

# Linked liist 2

list2 = LinkedList()
list2.append(8) 
list2.append(9) 
list2.append(10) 
list2.append(2) 

list3 = FlattenedList(list1,list2)
kofi = list3.joined()
kojo = list3.flattenedsortedList()

print(kojo)


 




                   
                    
                    
