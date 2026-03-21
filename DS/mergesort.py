
def mergesort(list):
    if len(list)<2:
        return list
    
    right,left  = split(list)
    
    right = mergesort(right)
    
    left = mergesort(left)
    
    return merge(right,left)

def split(list):
    
    mid = len(list)//2
    right = list[mid:]
    left = list[:mid]
    
    return right,left

def merge(right,left):
    
    l = []
    i = 0
    j = 0
    
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j]) 
            j += 1
    while i < len(left):
        l.append(left[i])
        i+=1
    while j < len(right):
        l.append(right[j])
        j+=1                 
              

    return l 



num = [1,5,6,7,2,3,4] 

print(mergesort(num))          