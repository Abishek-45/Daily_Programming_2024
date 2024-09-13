def MergeSorted(arr1,arr2):
    
    ini_length1 = len(arr1)
    ini_length2 = len(arr2)
    pos = arr1[0]
    if arr1[0] < arr2[0]:
        value = arr1.pop(0)
        arr1.append(value)
    else:
        value = arr2.pop(0)
        arr2.append(value)
        
    while arr1[0] != pos and arr2:
        if arr1[0] < arr2[0]:
            value = arr1.pop(0)
            arr1.append(value)
        else:
            value = arr2.pop(0)
            arr1.append(value)
            
    if arr2:
        while arr2:
            arr1.append(arr2.pop(0))
        
    
    for i in range(ini_length1,len(arr1)):
        arr2.append(arr1[i])
    
    for i in range(ini_length1,len(arr1)):
        arr1.pop(ini_length1)
        
    print(arr1)
    print(arr2)
            
    
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
MergeSorted(arr1,arr2)

