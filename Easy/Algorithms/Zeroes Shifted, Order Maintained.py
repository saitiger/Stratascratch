def shift_zeroes(arr):
    l = 0 
    for r in range(len(arr)):
        if(arr[r]!=0 and arr[l]==0):
            arr[l],arr[r] = arr[r],arr[l]
            l = l + 1
        while(arr[l]!=0):
            l = l + 1
    return arr
