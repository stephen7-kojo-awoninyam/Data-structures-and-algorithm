
def partition(unordered_list,first,last):
    
    pivot = unordered_list[first]
    
    greater_than_pivot_index = first + 1
    
    smaller_than_pivot_index = last
    
    while True:
        
        while unordered_list[greater_than_pivot_index] < pivot and greater_than_pivot_index < smaller_than_pivot_index:
            greater_than_pivot_index += 1
        while unordered_list[smaller_than_pivot_index] > pivot and smaller_than_pivot_index > greater_than_pivot_index:
            smaller_than_pivot_index -= 1
        if unordered_list[greater_than_pivot_index] > unordered_list[smaller_than_pivot_index]:
            
            temp = unordered_list[greater_than_pivot_index]
            
            unordered_list[greater_than_pivot_index] = unordered_list[smaller_than_pivot_index]
            
            unordered_list[smaller_than_pivot_index] = temp
        else:
            break
    
    
    
    ramp = unordered_list[smaller_than_pivot_index]
    
    unordered_list[smaller_than_pivot_index] = unordered_list[first]
    
    unordered_list[first] = ramp
    
    return smaller_than_pivot_index



def Quick_selection(unordered_list, first,last,k):
    
    split = partition(unordered_list,first,last)  
    
    if split == k:
        return unordered_list[split]
    
    elif split < k:
        
        return Quick_selection(unordered_list, split+1, last, k)
    
    else:
        return Quick_selection(unordered_list,first,split-1,k)                
        
        
        
print(Quick_selection([7,6,5,4,3,2,1],0,6,3))        