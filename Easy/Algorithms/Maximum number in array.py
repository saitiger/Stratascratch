def find_largest_number(arr):
    maxi = float('-inf')
    for n in arr:
        if(n>=maxi):
            maxi = n
    return maxi
