

def linear_search(list,target):
    """Returns the position of the target value in the list"""
    for i in range(0,len(list)):
        if list[i]==target:
            return i
    return None



def verify(position):
    if position is not None:
        print("The position of the target is:",position)
    else:
        print("The position of the target is not found") 
        

list = [1,2,3,4,5,6,7,8,9,10] 

target = int(input("Whats the target number: "))
verify(linear_search(list,target))              