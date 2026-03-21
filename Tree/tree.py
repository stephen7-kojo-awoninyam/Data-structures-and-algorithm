from collections import deque


class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.parent = None
                       
    def insert(self,data):
        node = Node(data)     
        if self.parent == None:
            self.parent = node
        else:
            if self.parent.left == None or self.parent.right == None:
                if node.data > self.parent.data:
                    self.parent.right = node
                else:
                    self.parent.left = node  
            else:
                current = self.parent
                while current:
                    if node.data > current.data:
                        if current.right == None:
                            current.right = node
                            return
                        current = current.right    
                    else:
                        
                        if current.left == None:
                            current.left = node 
                            return
                        current = current.left
                            
    def get_parent_with_node(self,data):
        current = self.parent
        parent = None
        if current == None:
            return (parent,None)
        
        while current:
            if current.data == data:
               return (parent,current)
            if data > current.data:
                parent = current
                current = current.right 
            else:
                parent = current
                current = current.left
        return (parent,current)  
                                                                    
    def delete(self,data):
        parent,node = self.get_parent_with_node(data)
        children_count = 0
        
        if node == None and parent == None:
            return False
        if node.right and node.left:
            children_count = 2
        elif node.left == None and node.right == None:
            children_count = 0 
        else:
            children_count = 1
             
        if children_count == 0:
            if parent:
                if parent.left == node:
                    
                   parent.left = None
                else:
                    parent.right = None   
            else:    
               node = None
        elif children_count == 1:
            next_node = None
            if node.right:
                next_node = node.right 
            else:
                next_node =  node.right 
            if parent:
                if parent.left == node:
                    parent.left = next_node
                else:
                    parent.right = next_node
            else:
                self.parent = next_node                

        else:
            
              current = node         
              left =  node.right   
              
              while left:
                  current = left
                  left = left.left
              node.data = left.data
                  
    def search(self,data):
        
        current = self.parent
        
        while current:
            
            if data == current.data:
                break
            if data > current.data:
                current = current.right
            else:
                current = current.left
        if current == None:
            return None
        
        return current.data 
    
    def in_order(self):
        
        current = self.parent
        
        if current == None:
            return 
        self.in_order(current.left)
        print(current.data)
        self.in_order(current.right)
        
    def pre_order(self):
        
        current = self.parent
        
        if current == None:
            return
        
        print(current.data)
        self.pre_order(current.left)
        self.pre_order(current.right)    
                                           
    def post_order(self):
        
        current = self.parent
        
        if current == None:
            return
        self.post_order(current.left)
        self.post_order(current.right)
        print(current.data)
         
    def breadth_first(self):
        node_list = []
        
        traverse_node = deque(self.parent)
        
        while len(traverse_node) > 0:
            node = traverse_node.popleft()
            node_list.append(node)
            if node.left:
                traverse_node.append(node.left)
            if node.right:
                traverse_node.append(node.right)                       
        return node_list     
       
        
tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)        



current = tree.parent


for i in range(1, 10):
    found = tree.search(i)
    print("{}: {}".format(i, found))

        