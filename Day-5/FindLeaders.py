def FindLeaders(arr):
    output = []
    right_max = 0
    i = len(arr) - 1
    
    while i>=0:
        if arr[i] > right_max:
            right_max = arr[i]
            output.insert(0,arr[i])
        i=i-1
        
    print(output)
            
    
    
arr = [int(x) for x in input().split()]
FindLeaders(arr)
