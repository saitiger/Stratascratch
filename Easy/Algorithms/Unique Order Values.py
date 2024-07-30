def non_duplicate(input):
# Method 1 
    ans = []
    for i in input:
        if i not in seen:
            ans.append(i)
    return ans
      
# Method 2 
    seen = set()
    ans = []
    for num in input:
        if num not in seen:
            seen.add(num)
            ans.append(num)
    return ans
