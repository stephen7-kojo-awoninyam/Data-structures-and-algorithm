



def insertion(unordered_list):
    
    list_size = len(unordered_list)
    
    for i in range(1,list_size):
        position = i
        insert_value = unordered_list[i]
        
        while position > 0 and insert_value < unordered_list[position-1]:
            unordered_list[position] = unordered_list[position - 1]
            
            position -= 1 
            
        unordered_list[position]  = insert_value 
        
    return unordered_list     
            
            
        
       
        
        
    return unordered_list        
            

            
            
    




unordered_list = [2,4,3,1,8,5,7,9,6]
print(insertion(unordered_list))            
                