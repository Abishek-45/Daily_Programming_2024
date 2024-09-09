def Sort(arr):
    
    i = 0
    j = 0
    k = len(arr)- 1
     
    while j <= k:
        if arr[j] == 0:
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j + 1
        
        elif arr[j] == 1:
            j = j + 1
        
        elif arr[j] == 2:
            arr[j],arr[k] = arr[k],arr[j]
            k = k - 1
            j = j + 1
             
    
    
    

arr = [int(x) for x in input().split()]
Sort(arr)
print(arr)