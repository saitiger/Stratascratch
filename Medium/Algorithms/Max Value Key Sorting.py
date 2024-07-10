def key_of_highest_value(dct):
  if not dct:
    return None
    
    max_val = max(dct.values())
    # res = []
    # for k,v in dct.items():
    #     if(v==max_val):
    #         res.append(k)
    # return sorted(res)[0]

    max_keys = [key for key, value in dct.items() if value == max_value] # List comprehension of the above loop
    return sorted(max_keys)[0]
