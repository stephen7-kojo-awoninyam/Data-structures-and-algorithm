import operator
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
        
        


class Express_inter:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self,data):
        node = Node(data)
        if self.head:
            node.prev = self.head
            self.head.next = node
            self.head = node
            self.head.next = None
        else:
            self.head = node
            self.head.next = None
            self.head.prev = None    
        self.size += 1    
        
    def pop(self):
        if self.size == 1:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        elif self.size > 1:
            data = self.head.data
            self.head = self.head.prev 
            self.head.next = None
            self.size -= 1
            return data
      
opera = Express_inter()

number = Express_inter()

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def evaluation(expression):
    for symb in expression:
        if symb.isdigit():
            number.append(int(symb))
        elif symb == "(":
            continue    
        else:
            if symb == ")":
                num1 = number.pop()
                num2 = number.pop()
                symbol = opera.pop()
                result = ops[symbol](num2,num1)
                number.append(result)
                continue    
            opera.append(symb)
    while number.head:
        num1 = number.pop()
        symbol = opera.pop()
        num2 = number.pop()
        if num2 == None and symbol == None:
            return result
        result = ops[symbol](num2,num1)    
        number.append(result)
    return None   
                    
 



expression = "3+(2*(7-4))-5/(1+1)"

print(evaluation(expression))       
            
            
            
                        
                   
               
        
        
            
    