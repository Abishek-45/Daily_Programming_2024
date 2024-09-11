def FindDuplicate(arr):
    slow = arr[arr[0]]
    fast = arr[arr[arr[0]]]
    
    while slow!=fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    
    fast = arr[0]
    
    while slow!=fast:
        slow = arr[slow]
        fast = arr[fast]
        
    return slow

arr = [int(x) for x in input().split()]
answer = FindDuplicate(arr)
print(answer)