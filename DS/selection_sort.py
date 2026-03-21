

def selection_sort(list):
    
    sorted_list = []
    for i in range(0,len(list)-1):
        if min_value(list[i],list):
            sorted_list.append(list[i])
            pop = list.pop(i)
        else:
            continue    
                 
    return sorted_list 


def min_value(value,list):
    
    if len(list) == 1:
        return True
    for i in range(0,len(list)-1):
        if value in list and value < min(list[i:]):
            return True
        return False


num = [1,5,6,7,2,3,4] 

print(selection_sort(num))      
    
    
    
    
    
    
           