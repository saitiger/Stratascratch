def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    common_elements = set1 & set2
    
    result = []
    for elem in common_elements:
        count1 = list1.count(elem)
        count2 = list2.count(elem)
        count = min(count1, count2)  # take the minimum count to handle duplicates
        result.extend([elem] * count)
    
    return result
