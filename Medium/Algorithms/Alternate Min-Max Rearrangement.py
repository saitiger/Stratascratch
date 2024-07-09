def modify_array(arr): 
  # Brute Force
  incr = sorted(arr)
  decr = sorted(arr,reverse = True)
  temp = []
  n = len(arr)
  i = 0 
  while len(temp)<n:
    temp.append(incr[i])
    temp.append(decr[i])
    i+=1
  return temp

# Two Pointer Approach
  
  arr.sort() 
  n = len(arr)
  temp = [0] * n
  l,r = 0,n - 1
  for i in range(n):
    if i % 2 == 0:
      temp[i] = arr[l]
      l+=1
    else:
      temp[i]=arr[r]
      r-=1
  return temp
    
