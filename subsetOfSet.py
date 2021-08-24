# print all subsets of given size of a set
 
import itertools
 
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
 
inputset = {1, 2, 3}
for i in range(len(inputset)+1):
    print(findsubsets(inputset, i))
