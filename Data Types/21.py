list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def accTuple(num): 
    return num[-1]   
   
def sort(tuples): 
    return sorted(tuples, key=accTuple)

print(sort(list))