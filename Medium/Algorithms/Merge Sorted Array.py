def merge_sorted_arrays(x):
    arr1 = x[0]
    arr2 = x[1]
    res = []
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if(arr1[i]<=arr2[j]):
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i<len(arr1):
        res.append(arr1[i])
        i+=1
    while j<len(arr2):
        res.append(arr2[j])
        j+=1
    return res
