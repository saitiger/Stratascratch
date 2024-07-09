def find_pairs(input):
    k = input["k"]
    arr = input["arr"]
    result = set()  
    seen = set()    
    
    for num in arr:  
        if num - k in seen:  
            result.add((num - k, num))  
        if num + k in seen:  
            result.add((num, num + k))
        seen.add(num)
    
    return list(result)
