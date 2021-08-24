# tower of Hanoi problem
# this algorithm represents a recursive function

def towerOfHanoi(n,fromRod,toRod,auxRod):
    if (n==1):
        print("moving disk 1 from rod {} to rod {}".format(fromRod,toRod))
        return
    towerOfHanoi((n-1),fromRod,auxRod,toRod)
    print("moving disk {} from rod {} to rod {}".format(n,fromRod,toRod))
    towerOfHanoi((n-1),auxRod,toRod,fromRod)

towerOfHanoi(3,'A','C','B')
    
