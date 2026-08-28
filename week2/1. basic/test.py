def bub(arr):
    n = len(arr)

    for j in range(n, 0, -1):
        for i in range(j-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr
def 