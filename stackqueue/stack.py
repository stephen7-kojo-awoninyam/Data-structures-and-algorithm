
class Node:
    def __init__(self,data=None):
        self.data = data 
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self,data):
        node = Node(data)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1            
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            
            if self.top.next:
                self.top = self.top.next 
            else:
                self.top = None
            return data
        return None   
    
    def peek(self):
        if self.top:
           return self.top.data 
        return None
    
    
def check_brackets(statement):
    stack = Stack()
    
    for ch in statement:
        if ch in ("(","[","{"):
            stack.push(ch)
        if ch in (")","]","}"):
            last = stack.pop()
            if last == "(" and ch == ")":
               continue            
            elif last == "[" and ch == "]":
               continue    
            elif last == "{" and ch == "}":
               continue            
            else:
               return False  
    if stack.size > 0:
        return False
    return True

sl = (
   "{(foo)(bar)}[hello](((this)is)a)test",
   "{(foo)(bar)}[hello](((this)is)atest",
   "{(foo)(bar)}[hello](((this)is)a)test))"
)
for s in sl:
   m = check_brackets(s)
   print("{}: {}".format(s, m))            
    
                            