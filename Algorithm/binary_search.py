


def binary_search(list,target):
    
    first = 0
    last = len(list)-1
    
    while first <= last:
        
        midpoint = (last + first)//2
        if list[midpoint] == target:
            return midpoint
        if list[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1    
    return None
        




def verify(position):
    if position is not None:
        print("The position of the target is:",position)
    else:
        print("The position of the target is not found") 
        

list = [1,2,3,4,5,6,7,8,9,10] 

target = int(input("Whats the target number: "))
verify(binary_search(list,target))  