def FindNumber(arr,N):
    Total_Sum = N * (N+1) // 2
    arr_sum = 0
    
    for i in range(len(arr)):
        arr_sum += arr[i]
        
    return Total_Sum - arr_sum
    
arr = [int(x) for x in input().split()]
N = int(input())
answer = FindNumber(arr,N)
print(answer)
