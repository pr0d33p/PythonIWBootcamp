def interSection(arr1, arr2): 
     result = list(filter(lambda x: x in arr1, arr2))  
     print("Intersection : ",result)

arr1 = [1, 3, 5, 7, 9] 
arr2 = [2, 3, 5, 7, 11] 
interSection(arr1,arr2) 