def rotate( arr, n):
    for i in range(n - 1, 0, -1):
        arr[i],arr[i-1] = arr[i - 1],arr[i];
    return arr