
def binary_search(arr, target):
    if not arr:
        return -1
    left, middle, right = (0 , len(arr)//2, len(arr)-1)

    for i in range(len(arr)):
        #딱 중간
        if arr[middle] == target:
            return middle
        # 왼쪽
        if(arr[middle] > target):
            temp = middle
            middle=(left + middle)//2
            right = temp
            
        #오른쪽
        else:
            temp = middle
            midde = (right + middle) //2
            left = temp

        
    



