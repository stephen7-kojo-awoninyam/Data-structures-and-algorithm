

def recursive_binary_search(list,target):
    
    if len(list)==0:
        return False
    midpoint = len(list)//2
    
    if list[midpoint] == target:
        return True
    
    if list[midpoint] > target:
        return recursive_binary_search(list[:midpoint],target)
    
    return recursive_binary_search(list[midpoint+1:],target)


def verify(position):
    print("Target is:",position)

list = [1,2,3,4,5,6,7,8,9,10] 

target = int(input("Whats the target number: "))
verify(recursive_binary_search(list,target))  
        
        