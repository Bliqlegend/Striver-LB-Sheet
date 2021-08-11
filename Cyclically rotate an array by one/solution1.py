def rotate( arr, n):
    if len(arr) >1: 
        arr[0],arr[1] = arr[1],arr[0]
        for i in range(1,n-1):
            # Move first element to the last of the array
            arr[0],arr[i+1] = arr[i+1],arr[0]
    else: return arr
    return arr
