def replace_null_values(lst):
    if not lst: 
        return lst
    prev = None
    for i in range(len(lst)):
        if lst[i] is not None:
            prev = lst[i]
        if lst[i] is None:
            lst[i] = prev
    return lst
