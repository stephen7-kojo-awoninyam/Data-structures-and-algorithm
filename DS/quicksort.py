

def Quicksort(list):
    if len(list)<=1:
        return list
    
    greater_than_pivot = []
    lesser_than_pivot = []
    
    pivot = list[0]
    
    for i in list[1:]:
        if pivot <= i:
            greater_than_pivot.append(i)
        else:
            lesser_than_pivot.append(i)
    return Quicksort(lesser_than_pivot) + [pivot] +  Quicksort(greater_than_pivot)   


number = [1,3,3,2,5,6,8,9,4,7]    

print(Quicksort(number))   