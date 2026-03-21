class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.head = None
        self.max_path = 0
        
    def insert(self,data):
        node = Node(data)
        
        if self.head == None:
            self.head = node
        else:
            if data > self.head.data:
                if self.head.right == None:
                    self.head.right = node
                    return
                current = self.head
                while  current:
                    if data > current.data:
                        if current.right == None:
                            current.right = node
                            return
                        current = current.right
                    else:
                        if current.left == None:
                            current.left = node
                            return
                        current = current.left
            if data < self.head.data:
                if self.head.left == None:
                    self.head.left = node
                    return
                current = self.head
                while  current:
                    if data > current.data:
                        if current.right == None:
                            current.right = node
                            return
                        current = current.right
                    else:
                        if current.left == None:
                            current.left = node
                            return
                        current = current.left
                        

    
        
        
        
def maximum_sum(node):                                                                      
    current = node                
    sum_sub_tree = 0                        
    if current == None:
        return 0
    left = maximum_sum(current.left)
    right = maximum_sum(current.right)
    
    if left and right:
        sum_sub_tree = max(sum_sub_tree,left + right + current.data)  
    else:
        return current.data + max(left,right)
    return sum_sub_tree          
  
                         
                         
                         
t1 = Tree()
t1.insert(5) 
t1.insert(8)                                 
t1.insert(3)                          
t1.insert(2)
t1.insert(4)  
t1.insert(10)                            
                                                                     
                                                                                 


print(maximum_sum(t1.head))   
    
                                         
                                         
                     
                     
                                         
                    
        