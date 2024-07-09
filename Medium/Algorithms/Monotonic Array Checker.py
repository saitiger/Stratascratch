def is_monotonic(lst):
    flag = 1
    asc,desc = 0,0
# Increasing Monolithic Check
    for i in range(len(lst)-1):
        if(lst[i]<=lst[i+1]):
            pass
        else:
            asc = 1
# Decreasing Monolithic Check
    for i in range(len(lst)-1):
        if(lst[i]>=lst[i+1]):
            pass
        else:
            desc = 1
    if(((asc==0) and (desc==0)) or ((asc==1) and (desc==1))):  # The first condition checks if list is both increasing                                                   # increasing and decreasing
        flag = 0                                               # and decreasing and second condition checks if both increasing 
                                                               # and decreasing conditions fail.
    return flag==1 or (all(x == lst[0] for x in lst)) # The second check is for the 
                                                      # test case when all values in the array are equal
